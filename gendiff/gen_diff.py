from gendiff.generator import generate_list_of_diff
from gendiff.formatters.stylish import default_format


def generate_diff(file1, file2, format_=default_format):
    diff = generate_list_of_diff(file1, file2)

    return format_(diff)
