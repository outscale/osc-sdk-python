import requests

class Requester:
    def __init__(self, auth, endpoint):
        self.auth = auth
        self.endpoint = endpoint

    def send(self, uri, payload):
        headers = None
        if self.auth.is_basic_auth_configured():
            headers = self.auth.get_basic_auth_header()
        else:
            headers = self.auth.forge_headers_signed(uri, payload)

        response = requests.post(self.endpoint, data=payload, headers=headers, verify=True)
        response.raise_for_status()
        return response.json()
