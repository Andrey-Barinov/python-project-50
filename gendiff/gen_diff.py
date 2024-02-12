from generator import generate_dict_of_diff
from stylish import default_format


def generate_diff(file1, file2, format_=default_format):
    diff = generate_dict_of_diff(file1, file2)

    return format_(diff)
