import itertools


def trans_value(value):
    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    else:
        return str(value)


def default_format(value, replacer=' '):

    def iter_(current_value, spaces_count):
        if not isinstance(current_value, dict):
            return trans_value(current_value)
        lines = []
        for key, val in current_value.items():
            lines.append(
                f'{replacer * spaces_count}{key}: '
                f'{iter_(val, spaces_count + 4)}'
            )
        result = itertools.chain(
            "{", lines, [(replacer * (spaces_count - 2)) + "}"]
        )
        return '\n'.join(result)

    return iter_(value, 2)
