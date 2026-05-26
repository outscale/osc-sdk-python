import os
import sys
from .runtime.async_.call import AsyncCall
from .runtime.sync.call import Call
from .runtime.request import RequestSpec

# Bootstrap logic for generated mixins. 
# This allows the SDK to load even if specific service code isn't generated yet.
try:
    from .generated.oks import AsyncOksTypedMixin
except (ImportError, ModuleNotFoundError):
    class AsyncOksTypedMixin: pass

try:
    from .generated.osc import AsyncOscTypedMixin
except (ImportError, ModuleNotFoundError):
    class AsyncOscTypedMixin: pass

# Replicate this pattern here for future services (e.g., EIM, FCU) 
# if they are generated into separate mixins.

from .limiter import RateLimiter
import ruamel.yaml
from .version import get_version
import warnings
from datetime import timedelta

type_mapping = {"boolean": "bool", "string": "str", "integer": "int", "array": "list"}

# Logs Output Options
LOG_NONE = 0
LOG_STDERR = 1
LOG_STDIO = 2
LOG_MEMORY = 4

# what to Log
LOG_ALL = 0
LOG_KEEP_ONLY_LAST_REQ = 1

# Default
DEFAULT_LIMITER_WINDOW = timedelta(seconds=1)  # 1 second
DEFAULT_LIMITER_MAX_REQUESTS = 5  # 5 requests / sec
RESOURCE_DIR = os.path.join(os.path.dirname(__file__), "resources")
OSC_SPEC = os.path.join(RESOURCE_DIR, "osc/api.yaml")
OKS_SPEC = os.path.join(RESOURCE_DIR, "oks/api.yaml")
# Replicate this pattern here for future services (e.g., EIM, FCU)
# if they are generated into separate mixins.


class ActionNotExists(NotImplementedError):
    pass


class ParameterNotValid(NotImplementedError):
    pass


class ParameterIsRequired(NotImplementedError):
    pass


class ParameterHasWrongType(NotImplementedError):
    pass


class Logger:
    string = ""
    type = LOG_NONE
    what = LOG_ALL

    def config(self, type=None, what=None):
        if type is not None:
            self.type = type
        if what is not None:
            self.what = what

    def str(self):
        if self.type == LOG_MEMORY:
            return self.string
        return None

    def do_log(self, s):
        if self.type & LOG_MEMORY:
            if self.what == LOG_KEEP_ONLY_LAST_REQ:
                self.string = s
            else:
                self.string = self.string + "\n" + s

        if self.type & LOG_STDIO:
            print(s)
        if self.type & LOG_STDERR:
            print(s, file=sys.stderr)


class OpenAPIActionAPI:
    def __init__(self, spec, service="api", **kwargs):
        self.service = service
        self._load_gateway_structure(spec)
        self.log = Logger()
        self.limiter = RateLimiter(DEFAULT_LIMITER_WINDOW, DEFAULT_LIMITER_MAX_REQUESTS)
        self.call = Call(
            logger=self.log,
            version=self.endpoint_api_version,
            limiter=self.limiter,
            **kwargs,
        )

    def update_credentials(self, **kwargs):
        warnings.warn(
            "update_credentials in deprecated. Use update_profile instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        self.update_profile(**kwargs)

    def update_profile(self, **kwargs):
        """
        destroy and create a new credential map use for each call.
        so you can change your ak/sk, region without having to recreate the whole Gateway
        as the object is recreate, you can't expect to keep parameter from the old configuration
        example: just updating the password, without renter the login will fail
        """
        self.call.update_profile(**kwargs)

    def access_key(self):
        return self.call.profile.access_key

    def secret_key(self):
        return self.call.profile.secret_key

    def region(self):
        return self.call.profile.region

    def email(self):
        warnings.warn(
            "email in deprecated. Use login instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.login()

    def login(self):
        return self.call.profile.login

    def password(self):
        return self.call.profile.password

    def _convert(self, input_file):
        structure = {}
        try:
            with open(input_file, "r") as fi:
                yaml = ruamel.yaml.YAML(typ="safe")
                content = yaml.load(fi.read())
        except Exception as err:
            print("Problem reading {}:{}".format(input_file, str(err)))
        self.api_version = content["info"]["version"]
        self.endpoint_api_version = content["servers"][0]["url"].split("/")[-1]
        for action, params in content["components"]["schemas"].items():
            if action.endswith("Request"):
                action_name = action.split("Request")[0]
                structure[action_name] = {}
                for propertie_name, properties in params["properties"].items():
                    if propertie_name == "DryRun":
                        continue
                    if "type" not in properties.keys():
                        action_type = None
                    else:
                        action_type = type_mapping[properties["type"]]
                    structure[action_name][propertie_name] = {
                        "type": action_type,
                        "required": False,
                    }

                if "required" in params.keys():
                    for required in params["required"]:
                        structure[action_name][required]["required"] = True
        return structure

    def _load_gateway_structure(self, spec):
        self.gateway_structure = self._convert(spec)

    def _check_parameters_type(self, action_structure, input_structure):
        for i_param, i_value in input_structure.items():
            if (
                i_param != "Filters"
                and action_structure[i_param]["type"] is not None
                and action_structure[i_param]["type"] != i_value.__class__.__name__
            ):
                raise ParameterHasWrongType(
                    "{} is <{}> instead of <{}>".format(
                        i_param,
                        i_value.__class__.__name__,
                        action_structure[i_param]["type"],
                    )
                )

    def _check_parameters_required(self, action_structure, input_structure):
        action_mandatory_params = [
            param for param in action_structure if action_structure[param]["required"]
        ]
        difference = set(action_mandatory_params).difference(
            set(input_structure.keys())
        )
        if difference:
            raise ParameterIsRequired(
                "Missing {}. Required parameters are {}".format(
                    ", ".join(list(difference)), ", ".join(action_mandatory_params)
                )
            )

    def _check_parameters_valid(self, action_name, params):
        structure_parameters = self.gateway_structure[action_name].keys()
        input_parameters = set(params)
        different_parameters = list(
            input_parameters.difference(set(structure_parameters))
        )
        if different_parameters:
            raise ParameterNotValid(
                """{}. Available parameters on sdk: {} api: {} are: {}.""".format(
                    ", ".join(different_parameters),
                    get_version(),
                    self.api_version,
                    ", ".join(structure_parameters),
                )
            )

    def _check(self, action_name, **params):
        if action_name not in self.gateway_structure:
            raise ActionNotExists(
                "Action {} does not exists for python sdk: {} with api: {}".format(
                    action_name, get_version(), self.api_version
                )
            )
        self._check_parameters_valid(action_name, params)
        self._check_parameters_required(self.gateway_structure[action_name], params)
        self._check_parameters_type(self.gateway_structure[action_name], params)

    @staticmethod
    def _remove_none_parameters(**params):
        """
        Remove parameters having None as value
        to perform CreateVolumes(Iops=None, Size=10)
        """
        return {key: value for key, value in params.items() if value is not None}

    def _get_action(self, action_name):
        def action(**kwargs):
            kwargs = self._remove_none_parameters(**kwargs)
            self._check(action_name, **kwargs)
            result = self.call.api(action_name, service=self.service, **kwargs)
            return result

        return action

    def __getattr__(self, attr):
        return self._get_action(attr)

    def __dir__(self):
        return self.gateway_structure.keys()

    def raw(self, action_name, **kwargs):
        return self.call.api(action_name, service=self.service, **kwargs)

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.call.close()

    def close(self):
        self.call.close()


class AsyncOpenAPIActionAPI(OpenAPIActionAPI):
    def __init__(self, spec, service="api", **kwargs):
        self.service = service
        self._load_gateway_structure(spec)
        self.log = Logger()
        self.limiter = RateLimiter(DEFAULT_LIMITER_WINDOW, DEFAULT_LIMITER_MAX_REQUESTS)
        self.call = AsyncCall(
            logger=self.log,
            version=self.endpoint_api_version,
            limiter=self.limiter,
            **kwargs,
        )

    def _get_action(self, action_name):
        async def action(**kwargs):
            kwargs = self._remove_none_parameters(**kwargs)
            self._check(action_name, **kwargs)
            result = await self.call.api(action_name, service=self.service, **kwargs)
            return result

        return action

    async def raw(self, action_name, **kwargs):
        return await self.call.api(action_name, service=self.service, **kwargs)

    async def __aenter__(self):
        return self

    async def __aexit__(self, type, value, traceback):
        await self.call.close()

    def __enter__(self):
        raise TypeError("AsyncGateway must be used with 'async with'")

    def __exit__(self, type, value, traceback):
        return None

    async def close(self):
        await self.call.close()


class OpenAPIPathAPI:
    def __init__(self, spec, service, **kwargs):
        self.service = service
        self.operations = self._load_operations(spec)
        self.log = Logger()
        self.limiter = RateLimiter(DEFAULT_LIMITER_WINDOW, DEFAULT_LIMITER_MAX_REQUESTS)
        self.call = Call(logger=self.log, limiter=self.limiter, **kwargs)

    def _load_operations(self, spec):
        with open(spec, "r") as fi:
            yaml = ruamel.yaml.YAML(typ="safe")
            content = yaml.load(fi.read())

        self.api_version = content["info"]["version"]
        operations = {}
        for path, path_item in content.get("paths", {}).items():
            path_parameters = path_item.get("parameters", [])
            for method in ["get", "post", "put", "patch", "delete"]:
                operation = path_item.get(method)
                if operation is None:
                    continue

                parameters = path_parameters + operation.get("parameters", [])
                operation_id = operation.get("operationId")
                if operation_id:
                    operations[operation_id] = {
                        "method": method.upper(),
                        "path": path,
                        "parameters": parameters,
                        "request_body": operation.get("requestBody"),
                    }
        return operations

    def _build_request(self, operation_name, kwargs):
        if operation_name not in self.operations:
            raise ActionNotExists(
                "Operation {} does not exists for python sdk: {} with api: {}".format(
                    operation_name, get_version(), self.api_version
                )
            )

        operation = self.operations[operation_name]
        kwargs = OpenAPIActionAPI._remove_none_parameters(**kwargs)
        path_params = {}
        query_params = {}

        for parameter in operation["parameters"]:
            name = parameter["name"]
            location = parameter["in"]
            if location == "path":
                if name not in kwargs and parameter.get("required"):
                    raise ParameterIsRequired("Missing {}.".format(name))
                if name in kwargs:
                    path_params[name] = kwargs.pop(name)
            elif location == "query":
                if name in kwargs:
                    query_params[name] = kwargs.pop(name)

        body = kwargs.pop("body", None)
        if operation["request_body"] is not None and body is None:
            body = kwargs
            kwargs = {}

        if kwargs:
            raise ParameterNotValid(
                "{}. Available parameters are path/query parameters or body.".format(
                    ", ".join(kwargs.keys())
                )
            )

        return RequestSpec(
            service=self.service,
            method=operation["method"],
            path=operation["path"],
            json_body=body,
            query_params=query_params,
        ), path_params

    def _get_operation(self, operation_name):
        def operation(**kwargs):
            request, path_params = self._build_request(operation_name, kwargs)
            return self.call.request(request, path_params=path_params)

        return operation

    def __getattr__(self, attr):
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
    def __init__(self, spec, service, **kwargs):
        self.service = service
        self.operations = self._load_operations(spec)
        self.log = Logger()
        self.limiter = RateLimiter(DEFAULT_LIMITER_WINDOW, DEFAULT_LIMITER_MAX_REQUESTS)
        self.call = AsyncCall(logger=self.log, limiter=self.limiter, **kwargs)

    def _get_operation(self, operation_name):
        async def operation(**kwargs):
            request, path_params = self._build_request(operation_name, kwargs)
            return await self.call.request(request, path_params=path_params)

        return operation

    async def close(self):
        await self.call.close()

    async def __aenter__(self):
        return self

    async def __aexit__(self, type, value, traceback):
        await self.close()

    def __enter__(self):
        raise TypeError("Async service client must be used with 'async with'")

    def __exit__(self, type, value, traceback):
        return None


class OutscaleGateway(OpenAPIActionAPI):
    def __init__(self, **kwargs):
        super().__init__(OSC_SPEC, service="api", **kwargs)


class AsyncOutscaleGateway(AsyncOscTypedMixin, AsyncOpenAPIActionAPI):
    def __init__(self, **kwargs):
        super().__init__(OSC_SPEC, service="api", **kwargs)


class OksGateway(OpenAPIPathAPI):
    def __init__(self, **kwargs):
        super().__init__(OKS_SPEC, service="oks", **kwargs)


class AsyncOksGateway(AsyncOksTypedMixin, AsyncOpenAPIPathAPI):
    def __init__(self, **kwargs):
        super().__init__(OKS_SPEC, service="oks", **kwargs)


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
        raise TypeError("AsyncClient must be used with 'async with'")

    def __exit__(self, type, value, traceback):
        return None


def test():
    a = OutscaleGateway()
    a.CreateVms(
        ImageId="ami-xx",
        BlockDeviceMappings=[{"/dev/sda1": {"Size": 10}}],
        SecurityGroupIds=["sg-aaa", "sg-bbb"],
    )
    try:
        a.CreateVms(
            ImageId="ami-xx",
            BlockDeviceMappings=[{"/dev/sda1": {"Size": 10}}],
            SecurityGroupIds=["sg-aaa", "sg-bbb"],
            Wrong="wrong",
        )
    except ParameterNotValid:
        pass
    else:
        raise AssertionError()
    try:
        a.CreateVms(
            BlockDeviceMappings=[{"/dev/sda1": {"Size": 10}}],
            SecurityGroupIds=["sg-aaa", "sg-bbb"],
        )
    except ParameterIsRequired:
        pass
    else:
        raise AssertionError()
    try:
        a.CreateVms(
            ImageId=["ami-xxx"],
            BlockDeviceMappings=[{"/dev/sda1": {"Size": 10}}],
            SecurityGroupIds=["sg-aaa", "sg-bbb"],
        )
    except ParameterHasWrongType:
        pass
    else:
        raise AssertionError()
    try:
        a.CreateVms(
            ImageId="ami-xxx",
            BlockDeviceMappings=[{"/dev/sda1": {"Size": 10}}],
            SecurityGroupIds="wrong",
        )
    except ParameterHasWrongType:
        pass
    else:
        raise AssertionError()
    try:
        a.CreateVms(
            ImageId=["ami-wrong"],
            BlockDeviceMappings=[{"/dev/sda1": {"Size": 10}}],
            SecurityGroupIds="wrong",
        )
    except ParameterHasWrongType:
        pass
    else:
        raise AssertionError()


if __name__ == "__main__":
    test()
