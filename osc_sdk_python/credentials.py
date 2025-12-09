import json
import os
import warnings

ORIGINAL_PATH = os.path.join(os.path.expanduser("~"), ".oapi_credentials")
STD_PATH = os.path.join(os.path.expanduser("~"), ".osc/config.json")
DEFAULT_REGION = "eu-west-2"
DEFAULT_PROFILE = "default"




class Endpoint:
    def __init__(self, **kwargs):
        self.api: str = kwargs.pop("api", None)
        self.oks: str = kwargs.pop("oks", None)
        self.lbu: str = kwargs.pop("lbu", None)
        self.oos: str = kwargs.pop("oos", None)
        self.fcu: str = kwargs.pop("fcu", None)
        self.eim: str = kwargs.pop("eim", None)
        self.direct_link: str = kwargs.pop("direct_link", None)

        if kwargs:
            unexpected = ", ".join(f"'{k}'" for k in kwargs.keys())
            raise TypeError(
                f"Endpoint() got unexpected keyword arguments: {unexpected}"
            )


class Profile:
    def __init__(self, **kwargs):
        self.access_key: str = kwargs.pop("access_key", None)
        self.secret_key: str = kwargs.pop("secret_key", None)
        self.access_key_v2: str = kwargs.pop("access_key_v2", None)
        self.secret_key_v2: str = kwargs.pop("secret_key_v2", None)
        self.iam_v2_services: list[str] = kwargs.pop("iam_v2_services", [])
        self.x509_client_cert: str = kwargs.pop("x509_client_cert", None)
        self.x509_client_cert_b64: str = kwargs.pop("x509_client_cert_b64", None)
        self.x509_client_key: str = kwargs.pop("x509_client_key", None)
        self.x509_client_key_b64: str = kwargs.pop("x509_client_key_b64", None)
        self.tls_skip_verify: bool = kwargs.pop("tls_skip_verify", False)
        self.login: str = kwargs.pop("login", None) or kwargs.pop("email", None)
        self.password: str = kwargs.pop("password", None)
        self.protocol: str = kwargs.pop("protocol", None)
        self.region: str = kwargs.pop("region", None)
        self.endpoints: "Endpoint" = kwargs.pop(
            "endpoints", Endpoint()
        )  # Forward reference

        if kwargs:
            unexpected = ", ".join(f"'{k}'" for k in kwargs.keys())
            raise TypeError(f"Profile() got unexpected keyword arguments: {unexpected}")

    @property
    def email(self) -> str:
        # For some reason, login is called email
        return self.login

    def get_endpoint(self, service: str) -> str:
        endpoint = getattr(self.endpoints, service)
        if not endpoint:
            endpoint = self.get_default_endpoint(service)

        return endpoint

    def get_default_endpoint(self, service: str) -> str:
        if service == "oks":
            return f"{self.protocol}://api.{self.region}.oks.outscale.com/api/v2"
        elif service == "api":
            return f"{self.protocol}://api.{self.region}.outscale.com/api/v1"
        elif service == "lbu":
            return f"{self.protocol}://lbu.{self.region}.outscale.com"
        elif service == "oos":
            return f"{self.protocol}://oos.{self.region}.outscale.com"
        elif service == "fcu":
            return f"{self.protocol}://fcu.{self.region}.outscale.com"
        elif service == "eim":
            return f"{self.protocol}://eim.{self.region}.outscale.com"
        elif service == "directlink":
            return f"{self.protocol}://directlink.{self.region}.outscale.com"
        else:
            raise ValueError("Unknown service")

    @staticmethod
    def from_env() -> "Profile":
        endpoint_kwargs = {
            "api": os.environ.get("OSC_ENDPOINT_API"),
            "oks": os.environ.get("OSC_ENDPOINT_OKS"),
            "lbu": os.environ.get("OSC_ENDPOINT_LBU"),
            "oos": os.environ.get("OSC_ENDPOINT_OOS"),
            "fcu": os.environ.get("OSC_ENDPOINT_FCU"),
            "eim": os.environ.get("OSC_ENDPOINT_EIM"),
            "direct_link": os.environ.get("OSC_ENDPOINT_DIRECT_LINK"),
        }

        profile_kwargs = {
            "access_key": os.environ.get("OSC_ACCESS_KEY"),
            "secret_key": os.environ.get("OSC_SECRET_KEY"),
            "access_key_v2": os.environ.get("OSC_ACCESS_KEY_V2"),
            "secret_key_v2": os.environ.get("OSC_SECRET_KEY_V2"),
            "x509_client_cert": os.environ.get("OSC_X509_CLIENT_CERT"),
            "x509_client_cert_b64": os.environ.get("OSC_X509_CLIENT_CERT_B64"),
            "x509_client_key": os.environ.get("OSC_X509_CLIENT_KEY"),
            "x509_client_key_b64": os.environ.get("OSC_X509_CLIENT_KEY_B64"),
            "tls_skip_verify": os.environ.get("OSC_TLS_SKIP_VERIFY", "False").lower() in ("true"),
            "login": os.environ.get("OSC_LOGIN"),
            "password": os.environ.get("OSC_PASSWORD"),
            "protocol": os.environ.get("OSC_PROTOCOL"),
            "region": os.environ.get("OSC_REGION"),
            "endpoints": Endpoint(**endpoint_kwargs),
        }

        iam_v2_services_env = os.environ.get("OSC_IAM_V2_SERVICES", "")
        if iam_v2_services_env:
            profile_kwargs["iam_v2_services"] = [
                s.strip() for s in iam_v2_services_env.split(",")
            ]

        return Profile(**profile_kwargs)

    @staticmethod
    def __from_file(path: str, profile: str) -> "Profile":
        with open(path) as f:
            config = json.load(f)
            kwargs_profile = config.get(profile)
            kwargs_endpoints = kwargs_profile.get("endpoints", {})
            kwargs_profile["endpoints"] = Endpoint(**kwargs_endpoints)
            return Profile(**kwargs_profile)

    def merge(self, other: "Profile"):
        self.__dict__.update(
            {
                k: v
                for k, v in other.__dict__.items()
                if v is not None and k != "endpoints"
            }
        )
        self.endpoints.__dict__.update(
            {k: v for k, v in other.endpoints.__dict__.items() if v is not None}
        )

    @staticmethod
    def from_standard_configuration(path: str, profile: str) -> "Profile":
        # 1. Load profile from environmental
        merged_profile = Profile.from_env()

        # 2. Load additional config from environment
        if not profile:
            value = os.environ.get("OSC_PROFILE")
            if value:
                profile = value
            else:
                profile = "default"

        if not path:
            value = os.environ.get("OSC_CONFIG_FILE")
            if value:
                path = value
            else:
                path = STD_PATH

        # 3. Load profile for config file
        try:
            file_profile = Profile.__from_file(path, profile)
            merged_profile.merge(file_profile)
        except Exception as e:
            if path != STD_PATH or profile != "default":
                raise e

        # 4. Load default
        if not merged_profile.protocol:
            merged_profile.protocol = "https"

        if not merged_profile.region:
            merged_profile.region = "eu-west-2"

        return merged_profile

class Credentials(Profile):
    def __init__(self, **kwargs):
        warnings.warn("Credentials class is deprecated. Use Profile class instead.",
            DeprecationWarning,
            stacklevel=2
        )
        super().__init__(**kwargs) 
