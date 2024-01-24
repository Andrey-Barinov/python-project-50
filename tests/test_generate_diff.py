from gendiff.gendiff_json import generate_diff
import pytest


json_file1 = "tests/fixtures/file1.json"

json_file2 = "tests/fixtures/file2.json"

result_file = "tests/fixtures/result_json_files.txt"


def test_generate_diff():
    right_result = open(result_file, 'r')
    assert generate_diff(json_file1, json_file2) == right_result.read()

