import requests
import time
import random
from requests.exceptions import JSONDecodeError
from .problem import ProblemDecoder, LegacyProblemDecoder, LegacyProblem, Problem

MAX_RETRIES = 3
RETRY_BACKOFF_FACTOR = 1.0
RETRY_BACKOFF_JITTER = 3.0
RETRY_BACKOFF_MAX = 30.0


class Retry:
    """
    Hold a request attempt and try to execute it
    """

    def __init__(self, session: requests.Session, method: str, url: str, **kwargs):
        self.session = session
        self.method: str = method
        self.url: str = url
        self.request_kwargs = kwargs

        # Extract all retry parameters
        self.attempt: int = int(self.request_kwargs.pop("attempt", 0))
        self.max_retries: int = int(
            self.request_kwargs.get("max_retries", MAX_RETRIES)
        )
        self.backoff_factor: float = float(
            self.request_kwargs.get("backoff_factor", RETRY_BACKOFF_FACTOR)
        )
        self.backoff_jitter: float = float(
            self.request_kwargs.get("backoff_jitter", RETRY_BACKOFF_JITTER)
        )
        self.backoff_max: float = float(
            self.request_kwargs.get("backoff_max", RETRY_BACKOFF_MAX)
        )

    def execute_once(self) -> requests.Response:
        """
        Execute the request without retry
        """
        return self.session.request(self.method, self.url, **self.request_kwargs)

    def increment(self) -> "Retry":
        """
        Return a copy of the retry with an incremented attempt count
        """
        new_kwargs = self.request_kwargs.copy()
        new_kwargs["attempt"] = self.attempt + 1
        return Retry(self.session, self.method, self.url, **new_kwargs)

    def should_retry(self, e: requests.exceptions.RequestException) -> bool:
        if isinstance(e, requests.exceptions.TooManyRedirects):
            return False

        if isinstance(e, requests.exceptions.URLRequired):
            return False

        if isinstance(e, ValueError):
            # can be raised on bogus request
            return False

        if e.response is not None:
            if 400 <= e.response.status_code < 500 and e.response.status_code != 429:
                return False

        return self.attempt < self.max_retries

    def get_backoff_time(self) -> float:
        """
        {backoff factor} * (2 ** ({number of previous retries}))
        random.uniform(0, {backoff jitter})
        """

        backoff: float = self.backoff_factor * (2**self.attempt)
        backoff += random.uniform(0, self.backoff_jitter)
        return min(backoff, self.backoff_max)

    def execute(self) -> requests.Response:
        try:
            res = self.execute_once()
            raise_for_status(res)
            return res
        except requests.exceptions.RequestException as e:
            if self.should_retry(e):
                sleep_time = self.get_backoff_time()
                time.sleep(sleep_time)
                return self.increment().execute()
            else:
                raise e


def raise_for_status(response: requests.Response):
    http_error_msg = ""
    problem = None
    reason = get_default_reason(response)

    try:
        ct = response.headers.get("content-type") or ""
        if "application/json" in ct:
            problem = response.json(cls=LegacyProblemDecoder)
            problem.status = problem.status or str(response.status_code)
            problem.url = response.url
        elif "application/problem+json" in ct:
            problem = response.json(cls=ProblemDecoder)
            problem.status = problem.status or str(response.status_code)
    except JSONDecodeError:
        pass
    else:
        if 400 <= response.status_code < 500:
            if isinstance(problem, LegacyProblem) or isinstance(problem, Problem):
                http_error_msg = f"Client Error --> {problem.msg()}"
            else:
                http_error_msg = f"{response.status_code} Client Error: {reason} for url: {response.url}"

        elif 500 <= response.status_code < 600:
            if isinstance(problem, LegacyProblem) or isinstance(problem, Problem):
                http_error_msg = f"Server Error --> {problem.msg()}"
            else:
                http_error_msg = f"{response.status_code} Server Error: {reason} for url: {response.url}"

        if http_error_msg:
            raise requests.HTTPError(http_error_msg, response=response)


def get_default_reason(response):
    if isinstance(response.reason, bytes):
        # We attempt to decode utf-8 first because some servers
        # choose to localize their reason strings. If the string
        # isn't utf-8, we fall back to iso-8859-1 for all other
        # encodings. (See PR #3538)
        try:
            return response.reason.decode("utf-8")
        except UnicodeDecodeError:
            return response.reason.decode("iso-8859-1")
    else:
        return response.reason
