from requests import Session, HTTPError
from requests import Session
from requests.adapters import HTTPAdapter
from requests.exceptions import JSONDecodeError
from urllib3.util.retry import Retry

class Requester:
    def __init__(self, auth, endpoint, max_retries=0, backoff_factor=0.5, status_forcelist=[400, 500]):
        self.auth = auth
        self.endpoint = endpoint
        if max_retries > 0:
            retry = Retry(total=max_retries, backoff_factor=backoff_factor, status_forcelist=status_forcelist)
            self.adapter = HTTPAdapter(max_retries=retry)
        else:
            self.adapter = HTTPAdapter()

    def send(self, uri, payload):
        headers = None
        if self.auth.is_basic_auth_configured():
            headers = self.auth.get_basic_auth_header()
        else:
            headers = self.auth.forge_headers_signed(uri, payload)

        if self.auth.x509_client_cert is not None:
            cert_file=self.auth.x509_client_cert
        else:
            cert_file=None
        if self.auth.proxy:
            if self.auth.proxy.startswith("https"):
                proxy= { "https": self.auth.proxy }
            else:
                proxy= { "http": self.auth.proxy }
        else:
            proxy=None

        print(proxy, cert_file)
        with Session() as session:
            session.mount("https://", self.adapter)
            session.mount("http://", self.adapter)
            response = session.post(self.endpoint, data=payload, headers=headers, verify=True,
                                    proxies=proxy, cert=cert_file)
            self.raise_for_status(response)
            return response.json()

    def raise_for_status(self, response):
        http_error_msg = ""
        error_code = None
        request_id = None
        reason = self.get_default_reason(response)
        code_type = None

        try:
            error = response.json()
        except JSONDecodeError:
            pass
        else:
            if "__type" in error:
                error_code = error.get("__type")
                reason = error.get("message")
                request_id = response.headers.get("x-amz-requestid")
            else:
                request_id = (error.get("ResponseContext") or {}).get("RequestId")
                errors = error.get("Errors")
                if errors:
                    error = errors[0]
                    error_code = error.get("Code")
                    reason = error.get("Type")
                    if error.get("Details"):
                        code_type = reason
                        reason = error.get("Details")
                    else:
                        code_type = None

            if 400 <= response.status_code < 500:
                if error_code and request_id:
                    http_error_msg = (
                        f"Client Error --> status = {response.status_code}, "
                        f"code = {error_code}, "
                        f'{"code_type = " if code_type is not None else ""}'
                        f'{code_type + ", " if code_type is not None else ""}'
                        f"Reason = {reason}, "
                        f"request_id = {request_id}, "
                        f"url = {response.url}"
                    )
                else:
                    http_error_msg = (
                        f"{response.status_code} Client Error: {reason} for url: {response.url}"
                    )

            elif 500 <= response.status_code < 600:
                if error_code and request_id:
                    http_error_msg = (
                        f"Server Error --> status = {response.status_code}, "
                        f"code = {error_code}, "
                        f'{"code_type = " if code_type is not None else ""}'
                        f'{code_type + ", " if code_type is not None else ""}'
                        f"Reason = {reason}, "
                        f"request_id = {request_id}, "
                        f"url = {response.url}"
                    )
                else:
                    http_error_msg = (
                        f"{response.status_code} Server Error: {reason} for url: {response.url}"
                    )

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
