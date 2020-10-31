import json
import os


class Credentials:
    def __init__(self, profile=None, access_key=None, secret_key=None, region=None, osc_cli_profile=None):
        if not self.load_credentials_from_env():
            if access_key is not None and secret_key is not None and region is not None:
                self.access_key = access_key
                self.secret_key = secret_key
                self.region = region
            elif osc_cli_profile is not None:
                self.load_credentials_from_file(profile, True)
            elif profile is not None:
                self.load_credentials_from_file(profile, False)

    def load_credentials_from_env(self):
        self.access_key = os.environ.get('OSC_ACCESS_KEY')
        self.secret_key = os.environ.get('OSC_SECRET_KEY')
        self.region = os.getenv('OSC_REGION', 'us-west-1')
        return self.access_key and self.secret_key

    def load_credentials_from_file(self, profile, is_osc_cli_profile):
        path = '.osc_sdk/config.json' if is_osc_cli_profile else '.oapi_credentials'
        region_field = 'region_name' if is_osc_cli_profile else 'region'
        try:
            with open(os.path.join(os.path.expanduser('~'), path)) as f:
                try:
                    credentials = json.load(f)
                    if not profile in credentials:
                        self.access_key = ''
                        self.secret_key = ''
                        self.region = 'eu-west-2'
                    else:
                        self.access_key = credentials.get(profile).get('access_key', '')
                        self.secret_key = credentials.get(profile).get('secret_key', '')
                        self.region = credentials.get(profile).get(region_field, 'us-west-1')
                except ValueError:
                    print ('Decoding json of "', path, '" has failed.')
                    raise
                except AttributeError as e:
                    print ('{}'.format(e))
                    raise
        except IOError:
            print ('"', path, '" not found.')
            raise

    def get_region(self):
        return self.region

    def get_ak(self):
        return self.access_key

    def get_sk(self):
        return self.secret_key

    def get_url_extension(self):
        return 'hk' if 'cn' in self.region else 'com'
