import json
import os

ORIGINAL_PATH = os.path.join(os.path.expanduser('~'),'.oapi_credentials')
STD_PATH = os.path.join(os.path.expanduser('~'),'.osc/config.json')
DEFAULT_REGION="eu-west-2"

class Credentials:
    def __init__(self, profile=None, access_key=None, secret_key=None, region=None):
        if not self.load_credentials_from_env():
            if access_key is not None and secret_key is not None and region is not None:
                self.access_key = access_key
                self.secret_key = secret_key
                self.region = region
            elif profile is not None:
                self.load_credentials_from_file(profile)
        self.check_options()

    def check_options(self):
        if self.access_key is None or len(self.access_key) == 0:
            raise Exception("Invalid Outscale access key")
        if self.secret_key is None or len(self.secret_key) == 0:
            raise Exception("Invalid Outscale secret key")

    def load_credentials_from_env(self):
        self.access_key = os.environ.get('OSC_ACCESS_KEY')
        self.secret_key = os.environ.get('OSC_SECRET_KEY')
        self.region = os.getenv('OSC_REGION', DEFAULT_REGION)
        return self.access_key and self.secret_key

    def load_credentials_from_file_(self, profile, f):
        try:
            credentials = json.load(f)
            if not profile in credentials:
                self.access_key = ''
                self.secret_key = ''
                self.region = DEFAULT_REGION
            else:
                self.access_key = credentials.get(profile).get('access_key', '')
                self.secret_key = credentials.get(profile).get('secret_key', '')
                self.region = credentials.get(profile).get('region', DEFAULT_REGION)
        except ValueError:
            print ('Decoding json of "{}" has failed.'.format(f))
            raise
        except AttributeError as e:
            print ('{}'.format(e))
            raise

    def load_credentials_from_file(self, profile):
        try:
            with open(STD_PATH) as f:
                self.load_credentials_from_file_(profile, f)
        except IOError:
            try:
                with open(ORIGINAL_PATH) as f:
                    self.load_credentials_from_file_(profile, f)
            except IOError:
                print ('nor "', STD_PATH, '" nor "' ,ORIGINAL_PATH,'" found.')
                raise

    def get_region(self):
        return self.region

    def get_ak(self):
        return self.access_key

    def get_sk(self):
        return self.secret_key

    def get_url_extension(self):
        return 'hk' if 'cn' in self.region else 'com'
