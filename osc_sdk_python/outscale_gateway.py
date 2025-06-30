import os
import sys
import threading
from .call import Call
from .credentials import Credentials
import ruamel.yaml
from osc_sdk_python import __version__

type_mapping = {'boolean': 'bool',
                'string': 'str',
                'integer': 'int',
                'array': 'list'}

# Logs Output Options
LOG_NONE = 0
LOG_STDERR = 1
LOG_STDIO = 2
LOG_MEMORY = 4

# what to Log
LOG_ALL = 0
LOG_KEEP_ONLY_LAST_REQ = 1

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
            self.type=type
        if what is not None:
            self.what=what
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


class OutscaleGateway:

    def __init__(self, **kwargs):
        self._load_gateway_structure()
        self._load_errors()
        self.log = Logger()
        self.call = Call(logger=self.log, **kwargs)

    def update_credentials(self, region=None, profile=None, access_key=None,
                           secret_key=None, email=None, password=None,
                           x509_client_cert=None, proxy=None):
        """
        destroy and create a new credential map use for each call.
        so you can change your ak/sk, region without having to recreate the whole Gateway
        as the object is recreate, you can't expect to keep parameter from the old configuration
        example: just updating the password, without renter the login will fail
        """
        self.call.update_credentials(region=region, profile=profile, access_key=access_key,
                                     secret_key=secret_key, email=email, password=password,
                                     x509_client_cert=x509_client_cert, proxy=x509_client_cert)

    def access_key(self):
        return Credentials(**self.call.credentials).access_key

    def secret_key(self):
        return Credentials(**self.call.credentials).secret_key

    def region(self):
        return Credentials(**self.call.credentials).region

    def email(self):
        return Credentials(**self.call.credentials).email

    def password(self):
        return Credentials(**self.call.credentials).password

    def _convert(self, input_file):
        structure = {}
        try:
            with open(input_file, 'r') as fi:
                yaml = ruamel.yaml.YAML(typ='safe')
                content = yaml.load(fi.read())
        except Exception as err:
            print('Problem reading {}:{}'.format(input_file, str(err)))
        self.api_version = content['info']['version']
        for action, params in content['components']['schemas'].items():
            if action.endswith('Request'):
                action_name = action.split('Request')[0]
                structure[action_name] = {}
                for propertie_name, properties in params['properties'].items():
                    if propertie_name == 'DryRun':
                        continue
                    if 'type' not in properties.keys():
                        action_type = None
                    else:
                        action_type = type_mapping[properties['type']]
                    structure[action_name][propertie_name] =  {'type': action_type, 'required': False}

                if 'required' in params.keys():
                    for required in params['required']:
                        structure[action_name][required]['required'] = True
        return structure

    def _load_gateway_structure(self):
        dir_path = os.path.join(os.path.dirname(__file__))
        yaml_file = os.path.abspath('{}/osc-api/outscale.yaml'.format(dir_path))
        self.gateway_structure = self._convert(yaml_file)

    def _load_errors(self):
        dir_path = os.path.join(os.path.dirname(__file__))
        yaml_file = os.path.abspath('{}/resources/gateway_errors.yaml'.format(dir_path))
        with open(yaml_file, 'r') as yam:
            yaml=ruamel.yaml.YAML(typ='safe')
            self.gateway_errors = yaml.load(yam.read())

    def _check_parameters_type(self, action_structure, input_structure):
        for i_param, i_value in input_structure.items():
            if i_param != 'Filters' and \
               action_structure[i_param]['type'] is not None and \
               action_structure[i_param]['type'] != i_value.__class__.__name__:
                raise ParameterHasWrongType('{} is <{}> instead of <{}>'.format(i_param, i_value.__class__.__name__,
                                                                                action_structure[i_param]['type']))

    def _check_parameters_required(self, action_structure, input_structure):
        action_mandatory_params = [param for param in action_structure if action_structure[param]['required']]
        difference = set(action_mandatory_params).difference(set(input_structure.keys()))
        if difference:
            raise ParameterIsRequired('Missing {}. Required parameters are {}'.format(', '.join(list(difference))
                                                                                ,', '.join(action_mandatory_params)))

    def _check_parameters_valid(self, action_name, params):
        structure_parameters = self.gateway_structure[action_name].keys()
        input_parameters = set(params)
        different_parameters = list(input_parameters.difference(set(structure_parameters)))
        if different_parameters:
            raise ParameterNotValid("""{}. Available parameters on sdk: {} api: {} are: {}.""".format(
                ', '.join(different_parameters),
                __version__, self.api_version,
                ', '.join(structure_parameters)))

    def _check(self, action_name, **params):
        if action_name not in self.gateway_structure:
            raise ActionNotExists('Action {} does not exists for python sdk: {} with api: {}'.format(action_name, __version__, self.api_version))
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
            result = self.call.api(action_name,**kwargs)
            return result
        return action

    def __getattr__(self, attr):
        return self._get_action(attr)

    def raw(self, action_name, **kwargs):
        return self.call.api(action_name, **kwargs)


def test():
    a = OutscaleGateway()
    a.CreateVms(ImageId='ami-xx', BlockDeviceMappings=[{'/dev/sda1': {'Size': 10}}], SecurityGroupIds=['sg-aaa', 'sg-bbb'])
    try:
        a.CreateVms(ImageId='ami-xx', BlockDeviceMappings=[{'/dev/sda1': {'Size': 10}}], SecurityGroupIds=['sg-aaa', 'sg-bbb'], Wrong='wrong')
    except ParameterNotValid:
        pass
    else:
        raise AssertionError()
    try:
        a.CreateVms(BlockDeviceMappings=[{'/dev/sda1': {'Size': 10}}], SecurityGroupIds=['sg-aaa', 'sg-bbb'])
    except ParameterIsRequired :
        pass
    else:
        raise AssertionError()
    try:
        a.CreateVms(ImageId=['ami-xxx'], BlockDeviceMappings=[{'/dev/sda1': {'Size': 10}}], SecurityGroupIds=['sg-aaa', 'sg-bbb'])
    except ParameterHasWrongType :
        pass
    else:
        raise AssertionError()
    try:
        a.CreateVms(ImageId='ami-xxx', BlockDeviceMappings=[{'/dev/sda1': {'Size': 10}}], SecurityGroupIds='wrong')
    except ParameterHasWrongType :
        pass
    else:
        raise AssertionError()
    try:
        a.CreateVms(ImageId=['ami-wrong'], BlockDeviceMappings=[{'/dev/sda1': {'Size': 10}}], SecurityGroupIds='wrong')
    except ParameterHasWrongType :
        pass
    else:
        raise AssertionError()


if __name__ == '__main__':
    test()
