import json
import os

ORIGINAL_PATH = os.path.join(os.path.expanduser('~'),'.oapi_credentials')
STD_PATH = os.path.join(os.path.expanduser('~'),'.osc/config.json')
DEFAULT_REGION="eu-west-2"
DEFAULT_PROFILE="default"

class Credentials:
    def __init__(self, region, profile, access_key, secret_key):
        if region == None:
            region = DEFAULT_REGION
        if profile == None:
            profile = DEFAULT_PROFILE
        # Set defaults
        self.region = region
        self.profile = profile
        self.access_key = access_key
        self.secret_key = secret_key
        # Overide with old configuration if available
        self.load_credentials_from_file(profile, ORIGINAL_PATH)
        # Overide with standard configuration if available
        self.load_credentials_from_file(profile, STD_PATH)
        # Overide with environmental configuration if available
        self.load_credentials_from_env()
        # Overide with app parameters if provided
        if access_key != None:
            self.access_key = access_key
        if secret_key != None:
            self.secret_key = secret_key
        if region != None:
            self.region = DEFAULT_REGION

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

    def get_region(self):
        return self.region

    def get_ak(self):
        return self.access_key

    def get_sk(self):
        return self.secret_key

    def get_profile(self):
        return self.profile

    def get_url_extension(self):
        return 'hk' if 'cn' in self.region else 'com'
