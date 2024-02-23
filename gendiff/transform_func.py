import itertools


def trans_value(value):
    if value is True:
        return 'true'

    elif value is False:
        return 'false'

    elif value is None:
        return 'null'

    else:
        return value


def trans_nested_value(nested_value, spaces_count, replacer=' '):
    def iter_(current_value, spaces_count1):

        lines = []

        for key, value in current_value.items():
            if not isinstance(value, dict):
                lines.append(
                    f"{replacer * spaces_count1}{key}: "
                    f"{trans_value(value)}"
                )

            else:
                lines.append(
                    f"{replacer * spaces_count1}{key}: "
                    f"{iter_(value, spaces_count1 + 4)}"
                )

        result = itertools.chain(
            "{", lines, [(replacer * (spaces_count1 - 4)) + "}"]
        )

        return '\n'.join(result)

    return iter_(nested_value, spaces_count)


def trans_type(type_of_key):
    if type_of_key == 'added':
        return '+ '

    elif type_of_key == 'deleted':
        return '- '

    else:
        return '  '
