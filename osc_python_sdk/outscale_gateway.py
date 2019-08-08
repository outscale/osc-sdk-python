import os
import time
from .call import Call
from ruamel.yaml import YAML

type_mapping = {'boolean': 'bool',
                'string': 'str',
                'integer': 'int',
                'array': 'list'}


class ActionNotExists(NotImplementedError):
    pass


class ParameterNotValid(NotImplementedError):
    pass


class ParameterIsRequired(NotImplementedError):
    pass


class ParameterHasWrongType(NotImplementedError):
    pass


class OutscaleGateway:

    def __init__(self, retry=True, **kwargs):
        self._load_gateway_structure()
        self.call = Call(**kwargs)
        if retry is True:
            self.retry = 5
        else:
            self.retry = 1

    def _convert(self, input_file):
        structure = {}
        try:
            with open(input_file, 'r') as fi:
                yaml = YAML(typ='safe')
                content = yaml.load(fi.read())
        except Exception as err:
            print('Problem reading {}:{}'.format(input_file, str(err)))
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
        yaml_file = os.path.abspath('{}/outscale.yaml'.format(dir_path))
        self.gateway_structure = self._convert(yaml_file)

    def _check_parameters_type(self, action_structure, input_structure):
        for i_param, i_value in input_structure.items():
            if i_param != 'Filters' and \
               action_structure[i_param]['type'] is not None and \
               action_structure[i_param]['type'] != i_value.__class__.__name__:
                raise ParameterHasWrongType('{} is <{}> instead of <{}>'.format(i_param, i_value.__class__.__name__,
                                                                                action_structure[i_param]['type']))

    def _check_parameters_required(self, action_structure, input_structure):
        action_mandatory_params = [param for param in action_structure if action_structure[param]['required'] == True]
        difference = set(action_mandatory_params).difference(set(input_structure.keys()))
        if difference:
            raise ParameterIsRequired('Missing {}. Required parameters are {}'.format(', '.join(list(difference))
                                                                                ,', '.join(action_mandatory_params)))

    def _check_parameters_valid(self, action_name, params):
        structure_parameters = self.gateway_structure[action_name].keys()
        input_parameters = set(params)
        different_parameters = list(input_parameters.difference(set(structure_parameters)))
        if different_parameters:
            raise ParameterNotValid("""{}. Available parameters are: {}.""".format(', '.join(different_parameters),
                                                                                   ', '.join(structure_parameters)))

    def _check(self, action_name, **params):
        if action_name not in self.gateway_structure.keys():
            raise ActionNotExists('Action {} does not exists'.format(self.action_name))
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

    def _action(self, **kwargs):
        kwargs = self._remove_none_parameters(**kwargs)
        self._check(self.action_name, **kwargs)
        for i in range(0, self.retry):
            result = self.call.api(self.action_name, **kwargs)
            if 'Error' not in result:
                break
            time.sleep(1)
        self.action_name = None
        return result

    def __getattr__(self, attr):
        self.action_name = attr
        return self._action

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

