import json
import os


class Credentials:
    def __init__(self, profile):
        if not self.load_credentials_from_env():
            self.load_credentials_from_file(profile)

    def load_credentials_from_env(self):
        self.access_key = os.environ.get('OSC_ACCESS_KEY')
        self.secret_key = os.environ.get('OSC_SECRET_KEY')
        self.region = os.getenv('OSC_REGION', 'us-west-1')
        return self.access_key and self.secret_key

    def load_credentials_from_file(self, profile):
        try:
            with open(os.path.join(os.path.expanduser('~'),'.oapi_credentials')) as f:
                try:
                    credentials = json.load(f)
                    if not profile in credentials:
                        raise AttributeError('Profil "{}" not found in "~/.oapi_credentials".'.format(profile))
                except ValueError:
                    print ('Decoding json of "~/.oapi_credentials" has failed.')
                    raise
                except AttributeError as e:
                    print ('{}'.format(e))
                    raise
                self.access_key = credentials.get(profile).get('access_key', '')
                self.secret_key = credentials.get(profile).get('secret_key', '')
                self.region = credentials.get(profile).get('region', 'us-west-1')
        except IOError:
            print ('"~/.oapi_credentials" not found.')
            raise

    def get_region(self):
        return self.region

    def get_ak(self):
        return self.access_key

    def get_sk(self):
        return self.secret_key

    def get_url_extension(self):
        return 'hk' if 'cn' in self.region else 'com'
