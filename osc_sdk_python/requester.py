import requests

# TO REMOVE FOR PRODUCTION ///
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# TO REMOVE FOR PRODUCTION ///


class Requester:
    def __init__(self, auth, endpoint):
        self.auth = auth
        self.endpoint = endpoint

    def send(self, uri, payload):
        response = requests.post(self.endpoint, data=payload,
                          headers=self.auth.forge_headers_signed(uri, payload),
                          verify=False)
        response.raise_for_status()
        return response.json()
