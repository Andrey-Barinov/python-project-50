from gendiff.generator import generate_dict_of_diff, change_key
from gendiff.parser import determine_format
from gendiff.stylish import default_format, trans_value
import json
import yaml


json_file1 = "tests/fixtures/file1.json"

json_file2 = "tests/fixtures/file2.json"

yaml_file1 = "tests/fixtures/file1.yaml"

yaml_file2 = "tests/fixtures/file2.yaml"

result_file = "tests/fixtures/right_result.txt"


def test_change_key():
    assert change_key({'2': {'3': '#', '4': 2}}) == {'  2': {'  3': '#', '  4': 2}}

    assert change_key({'2': 2, 'x': 1}) == {'  2': 2, '  x': 1}

def test_generate_dict_of_diff():
    right_result = {
        '  common': {'+ follow': False,
                     '  setting1': 'Value 1',
                     '- setting2': 200,
                     '- setting3': True,
                     '+ setting3': None,
                     '+ setting4': 'blah blah',
                     '+ setting5': {'  key5': 'value5'},
                     '  setting6': {'  doge': {'- wow': '', '+ wow': 'so much'},
                                    '  key': 'value', '+ ops': 'vops'
                                    }
                     },
        '  group1': {'- baz': 'bas',
                     '+ baz': 'bars',
                     '  foo': 'bar',
                     '- nest': {'  key': 'value'}, '+ nest': 'str'
                     },
        '- group2': {'  abc': 12345, '  deep': {'  id': 45}},
        '+ group3': {'  deep': {'  id': {'  number': 45}}, '  fee': 100500}
    }

    assert generate_dict_of_diff(json_file1, json_file2) == right_result

    assert generate_dict_of_diff(yaml_file1, yaml_file2) == right_result


def test_default_format():
    right_result = open(result_file, 'r')

    right_result = str(right_result.read())

    assert default_format(
        generate_dict_of_diff(json_file1, json_file2)
    ) == right_result

    assert default_format(
        generate_dict_of_diff(yaml_file1, yaml_file2)
    ) == right_result


def test_trans_value():
    assert trans_value(True) == 'true'

    assert trans_value(False) == 'false'

    assert trans_value(None) == 'null'

    assert trans_value('120.120') == '120.120'


def test_determine_format():
    file_json = open("tests/fixtures/file1.json", 'r')

    assert determine_format(json_file1) == json.load(file_json)

    file_yaml = open("tests/fixtures/file1.yaml", 'r')

    assert determine_format(yaml_file1) == yaml.load(file_yaml, Loader=yaml.FullLoader)
