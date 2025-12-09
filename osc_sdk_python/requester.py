from requests import HTTPError
from requests.exceptions import JSONDecodeError
from .problem import ProblemDecoder, LegacyProblemDecoder, LegacyProblem, Problem


class Requester:
    def __init__(
        self,
        session,
        auth,
        endpoint,
    ):
        self.session = session
        self.auth = auth
        self.endpoint = endpoint

    def send(self, uri, payload):
        headers = None
        if self.auth.is_basic_auth_configured():
            headers = self.auth.get_basic_auth_header()
        else:
            headers = self.auth.forge_headers_signed(uri, payload)

        if self.auth.x509_client_cert is not None:
            cert_file = self.auth.x509_client_cert
        else:
            cert_file = None

        response = self.session.post(
            self.endpoint,
            data=payload,
            headers=headers,
            verify=True,
            cert=cert_file,
        )
        self.raise_for_status(response)
        return response.json()

    def raise_for_status(self, response):
        http_error_msg = ""
        problem = None
        reason = self.get_default_reason(response)

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
                raise HTTPError(http_error_msg, response=response)

    def get_default_reason(self, response):
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
