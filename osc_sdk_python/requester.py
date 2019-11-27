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
        if response.status_code != 200:
             raise requests.HTTPError('url:{}. {}: {}'.format(response.url, response.status_code, response.text))
        return response.json()

