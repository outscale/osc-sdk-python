import os
import typing as t

from .runtime.call import AsyncCall, Call

# Bootstrap logic for generated mixins.
# This allows the SDK to load even if specific service code isn't generated yet.
if t.TYPE_CHECKING:
    from .generated.oks import AsyncOksTypedMixin
else:
    try:
        from .generated.oks import AsyncOksTypedMixin
    except (ImportError, ModuleNotFoundError):

        class AsyncOksTypedMixin:
            pass


if t.TYPE_CHECKING:
    from .generated.osc import AsyncOscTypedMixin
else:
    try:
        from .generated.osc import AsyncOscTypedMixin
    except (ImportError, ModuleNotFoundError):

        class AsyncOscTypedMixin:
            pass

# Replicate this pattern here for future services (e.g., EIM, FCU)
# if they are generated into separate mixins.

import warnings
from datetime import timedelta

from .exceptions import (
    SdkOperationError,
    SdkUsageError,
    SdkValidationError,
)
from .runtime.transport import RateLimiter

# Default
DEFAULT_LIMITER_WINDOW = timedelta(seconds=1)  # 1 second
DEFAULT_LIMITER_MAX_REQUESTS = 5  # 5 requests / sec
# Replicate this pattern here for future services (e.g., EIM, FCU)
# if they are generated into separate mixins.


class ActionNotExists(SdkOperationError):
    pass


class ParameterNotValid(SdkValidationError):
    pass


class ParameterIsRequired(SdkValidationError):
    pass


class ParameterHasWrongType(SdkValidationError):
    pass


class OpenAPIActionAPI:
    def __init__(self, service="api", *, _call_cls=Call, **kwargs):
        self.service = service
        self.limiter = RateLimiter(DEFAULT_LIMITER_WINDOW, DEFAULT_LIMITER_MAX_REQUESTS)
        self.call = _call_cls(
            limiter=self.limiter,
            **kwargs,
        )

    def update_credentials(self, **kwargs):
        warnings.warn(
            "update_credentials is deprecated. Use update_profile instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        self.update_profile(**kwargs)

    def update_profile(self, **kwargs):
        """
        Rebuild the service client profile so credentials, region, and endpoints
        can be changed without recreating the parent SDK client.

        Profile updates replace the previous configuration. For example, updating
        only the password without also providing the login will fail.
        """
        self.call.update_profile(**kwargs)

    @property
    def profile(self):
        return self.call.profile

    def access_key(self):
        return self.call.profile.access_key

    def secret_key(self):
        return self.call.profile.secret_key

    def region(self):
        return self.call.profile.region

    def email(self):
        warnings.warn(
            "email is deprecated. Use login instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.login()

    def login(self):
        return self.call.profile.login

    def password(self):
        return self.call.profile.password

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.call.close()

    def close(self):
        self.call.close()


class AsyncOpenAPIActionAPI(OpenAPIActionAPI):
    def __init__(self, service="api", **kwargs):
        super().__init__(service=service, _call_cls=AsyncCall, **kwargs)

    async def raw(self, action_name, **kwargs):
        return await self.call.api(action_name, service=self.service, **kwargs)

    async def __aenter__(self):
        return self

    async def __aexit__(self, type, value, traceback):
        await self.call.close()

    def __enter__(self):
        raise SdkUsageError("AsyncGateway must be used with 'async with'")

    def __exit__(self, type, value, traceback):
        return None

    async def close(self):
        await self.call.close()


class OpenAPIPathAPI:
    def __init__(self, service, *, _call_cls=Call, **kwargs):
        self.service = service
        self.limiter = RateLimiter(DEFAULT_LIMITER_WINDOW, DEFAULT_LIMITER_MAX_REQUESTS)
        self.call = _call_cls(limiter=self.limiter, **kwargs)

    @property
    def profile(self):
        return self.call.profile

    def __getattr__(self, attr):
        if attr not in self.operations:
            raise AttributeError(attr)
        return self._get_operation(attr)

    def __dir__(self):
        return self.operations.keys()

    def close(self):
        self.call.close()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()


class AsyncOpenAPIPathAPI(OpenAPIPathAPI):
    def __init__(self, service, **kwargs):
        super().__init__(service, _call_cls=AsyncCall, **kwargs)

    async def close(self):
        await self.call.close()

    async def __aenter__(self):
        return self

    async def __aexit__(self, type, value, traceback):
        await self.close()

    def __enter__(self):
        raise SdkUsageError("Async service client must be used with 'async with'")

    def __exit__(self, type, value, traceback):
        return None


class OutscaleGateway(OpenAPIActionAPI):
    def __init__(self, **kwargs):
        super().__init__(service="api", **kwargs)


class AsyncOutscaleGateway(AsyncOscTypedMixin, AsyncOpenAPIActionAPI):
    def __init__(self, **kwargs):
        super().__init__(service="api", **kwargs)


class OksGateway(OpenAPIPathAPI):
    def __init__(self, **kwargs):
        super().__init__(service="oks", **kwargs)


class AsyncOksGateway(AsyncOksTypedMixin, AsyncOpenAPIPathAPI):
    def __init__(self, **kwargs):
        super().__init__(service="oks", **kwargs)


# Replicate this pattern here for future services (e.g., EIM, FCU)
# if they are generated into separate mixins.


class Client:
    def __init__(self, **kwargs):
        self.osc = OutscaleGateway(**kwargs)
        self.oks = OksGateway(**kwargs)
        # Replicate this pattern here for future services (e.g., EIM, FCU)
        # if they are generated into separate mixins.

    def close(self):
        self.osc.close()
        self.oks.close()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()


class AsyncClient:
    def __init__(self, **kwargs):
        self.osc = AsyncOutscaleGateway(**kwargs)
        self.oks = AsyncOksGateway(**kwargs)
        # Replicate this pattern here for future services (e.g., EIM, FCU)
        # if they are generated into separate mixins.

    async def close(self):
        await self.osc.close()
        await self.oks.close()

    async def __aenter__(self):
        return self

    async def __aexit__(self, type, value, traceback):
        await self.close()

    def __enter__(self):
        raise SdkUsageError("AsyncClient must be used with 'async with'")

    def __exit__(self, type, value, traceback):
        return None
