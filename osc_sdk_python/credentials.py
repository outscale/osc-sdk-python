import json
import os

ORIGINAL_PATH = os.path.join(os.path.expanduser('~'),'.oapi_credentials')
STD_PATH = os.path.join(os.path.expanduser('~'),'.osc/config.json')
DEFAULT_REGION="eu-west-2"
DEFAULT_PROFILE="default"

class Credentials:
    def __init__(self, region, profile, access_key, secret_key, email, password):
        self.region = None

        if profile is None:
            profile = os.environ.get('OSC_PROFILE')
        if profile != None:
            # Overide with environmental configuration if available
            self.load_credentials_from_env()
        # Overide with old configuration if available
        self.load_credentials_from_file(profile, ORIGINAL_PATH)
        # Overide with standard configuration if available
        self.load_credentials_from_file(profile, STD_PATH)
        # Overide with environmental configuration if available
        if profile is None:
            profile = DEFAULT_PROFILE
            self.load_credentials_from_env()

        # Set defaults
        if region != None:
            self.region = region

        if self.region is None:
            self.region = DEFAULT_REGION

        self.profile = profile
        # Overide with app parameters if provided
        if access_key != None:
            self.access_key = access_key
        if secret_key != None:
            self.secret_key = secret_key
        self.email = email
        self.password = password

        self.check_options()

    def load_credentials_from_file(self, profile, file_path):
        try:
            with open(file_path) as f:
                config = json.load(f)
                profile = config.get(profile)
                if profile == None:
                    return
                ak = profile.get("access_key")
                if ak != None:
                    self.access_key = ak
                sk = profile.get("secret_key")
                if sk != None:
                    self.secret_key = sk
                region = profile.get("region")
                if region != None:
                    self.region = region
        except IOError:
            pass

    def load_credentials_from_env(self):
        ak = os.environ.get('OSC_ACCESS_KEY')
        if ak != None:
            self.access_key = ak
        sk = os.environ.get('OSC_SECRET_KEY')
        if sk != None:
            self.secret_key = sk
        region = os.environ.get('OSC_REGION')
        if region != None:
            self.region = region

    def check_options(self):
        if self.access_key == None or len(self.access_key) == 0:
            raise Exception("Invalid Outscale access key")
        if self.secret_key == None or len(self.secret_key) == 0:
            raise Exception("Invalid Outscale secret key")
        if self.region == None or len(self.region) == 0:
            raise Exception("Invalid Outscale region")
        if self.email is None and self.password is not None:
            raise Exception("Missing email option with password option")
        if self.email is not None and self.password is None:
            raise Exception("Missing password option with email option")

    def get_url_extension(self):
        return 'hk' if 'cn' in self.region else 'com'
