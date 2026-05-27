from .retry import AsyncRetry


class AsyncRequester:
    def __init__(self, client, auth, endpoint, **kwargs):
        self.client = client
        self.auth = auth
        self.endpoint = endpoint
        self.request_kwargs = kwargs

    async def send(self, method, uri, payload, query_params=None, canonical_querystring=""):
        if self.auth.service == "oks":
            headers = self.auth.forge_headers_oks()
        elif self.auth.is_basic_auth_configured():
            headers = self.auth.get_basic_auth_header()
        else:
            headers = self.auth.forge_headers_signed(
                uri, payload, canonical_querystring=canonical_querystring
            )

        retry_kwargs = self.request_kwargs.copy()
        retry_kwargs.update(
            {
                "content": payload,
                "headers": headers,
                "params": query_params or {},
            }
        )

        response = AsyncRetry(self.client, method, self.endpoint, **retry_kwargs)
        return await response.execute()
