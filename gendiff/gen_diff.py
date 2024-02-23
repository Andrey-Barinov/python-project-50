from gendiff.generator import generate_list_of_diff
from gendiff.formatters.select_format import select_format


def generate_diff(file1, file2, format_='stylish'):
    output_format = select_format(format_)
    diff = generate_list_of_diff(file1, file2)

    return output_format(diff)
