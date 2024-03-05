import itertools
from gendiff.transform_func import trans_value


def complex_or_str(value):
    if isinstance(value, dict):
        return "[complex value]"
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return value


def disassemble(list_of_diff):
    def iter_(keys, path=''):
        lines = []

        for key in keys:
            name = f"{key['key']}"

            if key['type'] == 'added':
                lines.append(
                    [path + name,
                     'added',
                     trans_value(complex_or_str(key['value']))
                     ]
                )

            elif key['type'] == 'deleted':

                lines.append(
                    [path + name,
                     'removed',
                     trans_value(complex_or_str(key['value']))]
                )

            elif key['type'] == 'updated':

                lines.append(iter_(key['children'], path + name + '.'))

        result = itertools.chain(lines)

        return sum(list(result), [])

    return iter_(list_of_diff)


def assemble(list_of_keys, n=3):
    result = [
        list_of_keys[i:i + n] for i in range(0, len(list_of_keys), n)
    ]
    return result


def create_dict(assembled_keys):
    result = {}

    for key in assembled_keys:
        if result.get(key[0], False):
            result[key[0]][0] = 'updated'
            result[key[0]].append(key[2])
        else:
            result[key[0]] = [key[1], key[2]]

    return result


def plain_format(list_of_diff):
    disassembled_keys = disassemble(list_of_diff)
    assembled_keys = assemble(disassembled_keys)
    dict_of_keys = create_dict(assembled_keys)

    result = ''

    for key, val in dict_of_keys.items():

        if val[0] == 'added':
            result += f"Property '{key}' "
            result += f"was added with value: {val[1]}\n"

        elif val[0] == 'removed':
            result += f"Property '{key}' was removed\n"

        else:
            result += f"Property '{key}' "
            result += f"was updated. From {val[1]} to {val[2]}\n"
    return result[:-1]
