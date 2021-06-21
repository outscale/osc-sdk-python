import requests

class Requester:
    def __init__(self, auth, endpoint):
        self.auth = auth
        self.endpoint = endpoint

    def send(self, uri, payload):
        response = requests.post(self.endpoint, data=payload,
                                 headers=self.auth.forge_headers_signed(uri, payload),
                                 verify=True)
        response.raise_for_status()
        return response.json()
