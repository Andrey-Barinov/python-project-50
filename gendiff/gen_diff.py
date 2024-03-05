from gendiff.generator import generate_list_of_diff
from gendiff.parser import determine_format, parser
from gendiff.formatters.select_format import select_format


def generate_diff(file1, file2, format_='stylish'):
    with open(file1, 'r') as data1, open(file2, 'r') as data2:

        parser_data1 = parser(data1, determine_format(file1))

        parser_data2 = parser(data2, determine_format(file2))

        output_format = select_format(format_)

        diff = generate_list_of_diff(parser_data1, parser_data2)

        return output_format(diff)
