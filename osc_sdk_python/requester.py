from .retry import Retry


class Requester:
    def __init__(self, session, auth, endpoint, **kwargs):
        self.session = session
        self.auth = auth
        self.endpoint = endpoint
        self.request_kwargs = kwargs

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

        retry_kwargs = self.request_kwargs.copy()
        retry_kwargs.update(
            {"data": payload, "headers": headers, "verify": True, "cert": cert_file}
        )

        response = Retry(self.session, "post", self.endpoint, **retry_kwargs)
        return response.execute().json()
