import asyncio
import json
import random

import httpx

from ...problem import LegacyProblem, LegacyProblemDecoder, Problem, ProblemDecoder
from ..sync.retry import (
    MAX_RETRIES,
    RETRY_BACKOFF_FACTOR,
    RETRY_BACKOFF_JITTER,
    RETRY_BACKOFF_MAX,
    get_default_reason,
    Retry,
)


class AsyncRetry:
    """
    Hold an async request attempt and try to execute it.
    """

    def __init__(self, client: httpx.AsyncClient, method: str, url: str, **kwargs):
        self.client = client
        self.method: str = method
        self.url: str = url
        self.request_kwargs = kwargs

        self.attempt: int = int(self.request_kwargs.pop("attempt", 0))
        self.max_retries: int = int(
            self.request_kwargs.pop("max_retries", MAX_RETRIES)
        )
        self.backoff_factor: float = float(
            self.request_kwargs.pop("backoff_factor", RETRY_BACKOFF_FACTOR)
        )
        self.backoff_jitter: float = float(
            self.request_kwargs.pop("backoff_jitter", RETRY_BACKOFF_JITTER)
        )
        self.backoff_max: float = float(
            self.request_kwargs.pop("backoff_max", RETRY_BACKOFF_MAX)
        )

    async def execute_once(self) -> httpx.Response:
        """
        Execute the request without retry.
        """
        return await self.client.request(
            self.method, self.url, **self.request_kwargs
        )

    def increment(self) -> "AsyncRetry":
        """
        Return a copy of the retry with an incremented attempt count.
        """
        new_kwargs = self.request_kwargs.copy()
        new_kwargs["attempt"] = self.attempt + 1
        new_kwargs["max_retries"] = self.max_retries
        new_kwargs["backoff_factor"] = self.backoff_factor
        new_kwargs["backoff_jitter"] = self.backoff_jitter
        new_kwargs["backoff_max"] = self.backoff_max
        return AsyncRetry(self.client, self.method, self.url, **new_kwargs)

    def should_retry(self, e: httpx.HTTPError) -> bool:
        if isinstance(e, httpx.TooManyRedirects):
            return False

        response = getattr(e, "response", None)
        if response is not None:
            if 400 <= response.status_code < 500 and response.status_code != 429:
                return False

        return self.attempt < self.max_retries

    def get_backoff_time(self) -> float:
        backoff: float = self.backoff_factor * (2**self.attempt)
        backoff += random.uniform(0, self.backoff_jitter)
        return min(backoff, self.backoff_max)

    def get_retry_after_time(self, e: httpx.HTTPError):
        return Retry.get_retry_after_time(self, e)

    async def execute(self) -> httpx.Response:
        try:
            res = await self.execute_once()
            raise_for_status(res)
            return res
        except httpx.HTTPError as e:
            if self.should_retry(e):
                sleep_time = self.get_retry_after_time(e)
                if sleep_time is None:
                    sleep_time = self.get_backoff_time()
                await asyncio.sleep(sleep_time)
                return await self.increment().execute()
            raise e


def raise_for_status(response: httpx.Response):
    http_error_msg = ""
    problem = None
    reason = get_default_reason(response) if hasattr(response, "reason") else response.reason_phrase

    try:
        ct = response.headers.get("content-type") or ""
        if "application/problem+json" in ct:
            problem = json.loads(response.text, cls=ProblemDecoder)
            problem.status = problem.status or str(response.status_code)
        elif "application/json" in ct:
            problem = json.loads(response.text, cls=LegacyProblemDecoder)
            problem.status = problem.status or str(response.status_code)
            problem.url = str(response.url)
    except json.JSONDecodeError:
        pass
    else:
        if 400 <= response.status_code < 500:
            if isinstance(problem, LegacyProblem) or isinstance(problem, Problem):
                http_error_msg = f"Client Error --> {problem.msg()}"
            else:
                http_error_msg = (
                    f"{response.status_code} Client Error: {reason} "
                    f"for url: {response.url}"
                )

        elif 500 <= response.status_code < 600:
            if isinstance(problem, LegacyProblem) or isinstance(problem, Problem):
                http_error_msg = f"Server Error --> {problem.msg()}"
            else:
                http_error_msg = (
                    f"{response.status_code} Server Error: {reason} "
                    f"for url: {response.url}"
                )

        if http_error_msg:
            raise httpx.HTTPStatusError(
                http_error_msg,
                request=response.request,
                response=response,
            )
