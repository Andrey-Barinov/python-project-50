from gendiff.gendiff import generate_diff



json_file1 = "tests/fixtures/file1.json"

json_file2 = "tests/fixtures/file2.json"

yaml_file1 = "tests/fixtures/file1.yaml"

yaml_file2 = "tests/fixtures/file2.yaml"

result_file = "tests/fixtures/right_result.txt"


def test_generate_diff_json():
    right_result = open(result_file, 'r')

    assert generate_diff(json_file1, json_file2) == right_result.read()


def test_generate_diff_yaml():
    right_result = open(result_file, 'r')

    assert generate_diff(yaml_file1, yaml_file2) == right_result.read()
