from .async_retry import AsyncRetry


class AsyncRequester:
    def __init__(self, client, auth, endpoint, **kwargs):
        self.client = client
        self.auth = auth
        self.endpoint = endpoint
        self.request_kwargs = kwargs

    async def send(self, uri, payload):
        if self.auth.is_basic_auth_configured():
            headers = self.auth.get_basic_auth_header()
        else:
            headers = self.auth.forge_headers_signed(uri, payload)

        retry_kwargs = self.request_kwargs.copy()
        retry_kwargs.update({"content": payload, "headers": headers})

        response = AsyncRetry(self.client, "POST", self.endpoint, **retry_kwargs)
        return await response.execute()
