from gendiff.gendiff_json import generate_diff



json_file1 = "/mnt/c/python-project-50/tests/fixtures/file1.json"

json_file2 = "/mnt/c/python-project-50/tests/fixtures/file2.json"

result_file = "/mnt/c/python-project-50/tests/fixtures/result_json_files.txt"


def test_generate_diff():
    right_result = open(result_file, 'r')
    assert generate_diff(json_file1, json_file2) == right_result.read()

test_generate_diff()

