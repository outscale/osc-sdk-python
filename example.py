from osc_python_sdk import Gateway


if __name__ == '__main__':
    gw = Gateway(**{'profile': 'my-profile'})
    print(gw.ReadVms())
    print(gw.ReadVolumes())
