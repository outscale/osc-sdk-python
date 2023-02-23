from requests import Session
from requests.adapters import HTTPAdapter
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

        with Session() as session:
            session.mount("https://", self.adapter)
            session.mount("http://", self.adapter)
            response = session.post(self.endpoint, data=payload, headers=headers, verify=True,)
            response.raise_for_status()
            return response.json()
