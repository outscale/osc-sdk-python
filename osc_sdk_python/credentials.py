import json
import os

ORIGINAL_PATH = os.path.join(os.path.expanduser("~"), ".oapi_credentials")
STD_PATH = os.path.join(os.path.expanduser("~"), ".osc/config.json")
DEFAULT_REGION = "eu-west-2"
DEFAULT_PROFILE = "default"
MAX_RETRIES = 3
RETRY_BACKOFF_FACTOR = 1
RETRY_BACKOFF_JITTER = 3


class Credentials:
    def __init__(
        self,
        region,
        profile,
        access_key,
        secret_key,
        email,
        password,
        x509_client_cert=None,
        proxy=None,
        max_retries=None,
        retry_backoff_factor=None,
        retry_backoff_jitter=None,
    ):
        self.region = None
        self.access_key = access_key
        self.secret_key = secret_key
        self.email = email
        self.password = password
        self.x509_client_cert = x509_client_cert
        self.proxy = proxy
        self.max_retries = max_retries
        self.retry_backoff_factor = retry_backoff_factor
        self.retry_backoff_jitter = retry_backoff_jitter

        if profile is None:
            profile = os.environ.get("OSC_PROFILE")
        else:
            # Override with environmental configuration if available
            self.load_credentials_from_env()
        # Override with old configuration if available
        self.load_credentials_from_file(profile, ORIGINAL_PATH)
        # Override with standard configuration if available
        self.load_credentials_from_file(profile, STD_PATH)
        # Override with environmental configuration if available
        if profile is None:
            profile = DEFAULT_PROFILE
            self.load_credentials_from_env()

        # Set defaults
        if region is not None:
            self.region = region

        if self.region is None:
            self.region = DEFAULT_REGION

        self.profile = profile
        # Override with app parameters if provided
        if access_key is not None:
            self.access_key = access_key
        if secret_key is not None:
            self.secret_key = secret_key

        if self.max_retries is None:
            self.max_retries = MAX_RETRIES
        if self.retry_backoff_factor is None:
            self.retry_backoff_factor = RETRY_BACKOFF_FACTOR
        if self.retry_backoff_jitter is None:
            self.retry_backoff_jitter = RETRY_BACKOFF_JITTER

        self.check_options()

    def load_credentials_from_file(self, profile, file_path):
        try:
            with open(file_path) as f:
                config = json.load(f)
                profile = config.get(profile)

                if profile is None:
                    return

                ak = profile.get("access_key")
                if ak is not None:
                    self.access_key = ak

                sk = profile.get("secret_key")
                if sk is not None:
                    self.secret_key = sk

                region = profile.get("region")
                if region is not None:
                    self.region = region

                max_retries = profile.get("max_retries")
                if max_retries is not None:
                    self.max_retries = max_retries

                retry_backoff_factor = profile.get("retry_backoff_factor")
                if retry_backoff_factor is not None:
                    self.retry_backoff_factor = retry_backoff_factor

                retry_backoff_jitter = profile.get("retry_backoff_jitter")
                if retry_backoff_jitter is not None:
                    self.retry_backoff_jitter = retry_backoff_jitter

        except IOError:
            pass

    def load_credentials_from_env(self):
        ak = os.environ.get("OSC_ACCESS_KEY")
        if ak is not None:
            self.access_key = ak
        sk = os.environ.get("OSC_SECRET_KEY")
        if sk is not None:
            self.secret_key = sk
        region = os.environ.get("OSC_REGION")
        if region is not None:
            self.region = region
        max_retries = os.environ.get("OSC_MAX_RETRIES")
        if max_retries is not None:
            self.max_retires = int(max_retries)
        retry_backoff_factor = os.environ.get("OSC_RETRY_BACKOFF_FACTOR")
        if retry_backoff_factor is not None:
            self.retry_backoff_factor = float(retry_backoff_factor)
        retry_backoff_jitter = os.environ.get("OSC_RETRY_BACKOFF_JITTER")
        if retry_backoff_jitter is not None:
            self.retry_backoff_factor = float(retry_backoff_jitter)

    def check_options(self):
        if self.access_key is not None or self.secret_key is not None:
            if self.access_key is None or len(self.access_key) == 0:
                raise Exception("Invalid Outscale access key")
            if self.secret_key is None or len(self.secret_key) == 0:
                raise Exception("Invalid Outscale secret key")
        elif self.email is not None or self.password is not None:
            if self.email is None or len(self.email) == 0:
                raise Exception("Invalid email option")
            if self.password is None and self.password == 0:
                raise Exception("Invalid password option")
        if self.region is None or len(self.region) == 0:
            raise Exception("Invalid Outscale region")

    def get_url_extension(self):
        return "hk" if "cn" in self.region else "com"
