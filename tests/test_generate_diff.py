from gendiff.gen_diff import generate_diff
from gendiff.generator import generate_list_of_diff
from gendiff.parser import determine_format, parser
from gendiff.transform_func import trans_nested_value, trans_value, trans_type
from gendiff.formatters.stylish import default_format
from gendiff.formatters.plain import plain_format, complex_or_str
from gendiff.formatters.plain import disassemble, assemble, create_dict
from gendiff.formatters.json import json_format
from gendiff.formatters.select_format import select_format
import json
import yaml

json_file1 = "tests/fixtures/file1.json"

json_file2 = "tests/fixtures/file2.json"

json_file_small = "tests/fixtures/small_file.json"

yaml_file1 = "tests/fixtures/file1.yaml"

yaml_file2 = "tests/fixtures/file2.yaml"

yaml_file_small = "tests/fixtures/small_file.yaml"

result_file = "tests/fixtures/right_result.txt"

result_file_plain = "tests/fixtures/right_result_plain.txt"

result_file_json = "tests/fixtures/right_result_json.txt"



def test_generate_diff():
    right_result = open(result_file, 'r')

    right_result = str(right_result.read())

    assert generate_diff(json_file1, yaml_file2) == right_result


def test_generate_list_of_diff():
    right_result = [
        {'key': 'common', 'type': 'changed', 'children': [
            {'key': 'follow', 'type': 'added', 'value': False},
            {'key': 'setting1', 'type': 'unchanged', 'value': 'Value 1'},
            {'key': 'setting3', 'type': 'deleted', 'value': True},
            {'key': 'setting3', 'type': 'added', 'value': None}]},
        {'key': 'group2', 'type': 'deleted', 'value': {'abc': 12345}},
        {'key': 'group3', 'type': 'added', 'value': {'fee': 100500}}]

    assert generate_list_of_diff(
        json_file_small, yaml_file_small
    ) == right_result


def test_default_format():
    right_result = open(result_file, 'r')

    right_result = str(right_result.read())

    assert default_format(
        generate_list_of_diff(json_file1, json_file2)
    ) == right_result

    assert default_format(
        generate_list_of_diff(yaml_file1, yaml_file2)
    ) == right_result


def test_plain():
    right_result = open(result_file_plain, 'r')

    right_result = str(right_result.read())

    assert plain_format(
        generate_list_of_diff(json_file1, json_file2)
    ) == right_result[:-1]

    assert plain_format(
        generate_list_of_diff(yaml_file1, yaml_file2)
    ) == right_result[:-1]


def test_complex_or_str():
    assert complex_or_str({'a': '1', 'b': 2}) == "[complex value]"

    assert complex_or_str('hello') == "'hello'"

    assert complex_or_str(25) == 25


def test_disassemble():
    example_value = [
        {'key': 'common', 'type': 'changed', 'children': [
            {'key': 'follow', 'type': 'added', 'value': False},
            {'key': 'setting1', 'type': 'unchanged', 'value': 'Value 1'}]}]

    right_result = ['common.follow', 'added', 'false']

    assert disassemble(example_value) == right_result


def test_assemble():
    assert assemble([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]


def test_create_dict():
    example_value = [
        ['common.follow', 'added', 'false'],
        ['common.setting3', 'removed', 200],
        ['common.setting3', 'removed', 'true']
    ]

    right_result = {
        'common.follow': ['added', 'false'],
        'common.setting3': ['updated', 200, 'true']
    }

    assert create_dict(example_value) == right_result


def test_json_format():
    right_result = open(result_file_json, 'r')

    right_result = str(right_result.read())

    assert json_format(
        generate_list_of_diff(json_file1, json_file2)
    ) == right_result

    assert json_format(
        generate_list_of_diff(yaml_file1, yaml_file2)
    ) == right_result


def test_select_format():
    assert select_format('stylish') == default_format

    assert select_format('plain') == plain_format

    assert select_format('json') == json_format


def test_trans_value():
    assert trans_value(True) == 'true'

    assert trans_value(False) == 'false'

    assert trans_value(None) == 'null'

    assert trans_value('120.120') == '120.120'


def test_trans_type():
    assert trans_type('added') == '+ '

    assert trans_type('deleted') == '- '

    assert trans_type('changed') == '  '


def test_trans_nested_value():
    nested_value = {'2': {'3': '#'}, 'x': 1}
    right_result = '{\n  2: {\n      3: #\n  }\n  x: 1\n}'
    assert trans_nested_value(nested_value, 2) == right_result


def test_determine_format():
    assert determine_format("tests/fixtures/file1.json") == 'json'

    assert determine_format("tests/fixtures/file1.yaml") == 'yaml'


right_result = open(json_file1, 'r')
right_result1 = open(yaml_file1, 'r')


def test_parser():

    with open(json_file1, 'r') as file_json:
        assert parser(file_json, 'json') == json.load(right_result)

    with open(yaml_file1, 'r') as file_yaml:
        assert (parser(file_yaml, 'yaml') == yaml.load(
            right_result1, Loader=yaml.FullLoader
        ))
