import json
import yaml


def determine_format(file):
    if file[-4:] == 'json':
        with open(file, 'r') as file_json:
            return json.load(file_json)
    elif file[-4:] in ['yaml', '.yml']:
        with open(file, 'r') as file_yaml:
            data = yaml.load(file_yaml, Loader=yaml.FullLoader)
            return data[0]


def parser(file):
    data = determine_format(file)
    return data
