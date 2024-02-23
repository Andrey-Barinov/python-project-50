from gendiff.formatters.plain import plain_format
from gendiff.formatters.stylish import default_format


def select_format(output_format):
    if output_format == 'stylish':
        return default_format

    elif output_format == 'plain':
        return plain_format
