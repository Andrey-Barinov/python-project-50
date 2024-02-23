import itertools
from gendiff.transform_func import trans_value, trans_type, trans_nested_value


def default_format(list_of_diff, replacer=' '):
    def iter_(current_value, spaces_count):
        lines = []

        for key in current_value:

            if 'value' in key.keys():
                if isinstance(key['value'], dict):
                    lines.append(
                        f"{replacer * spaces_count}{trans_type(key['type'])}"
                        f"{key['key']}: "
                        f"{trans_nested_value(key['value'], spaces_count + 6)}"
                    )

                else:
                    lines.append(
                        f"{replacer * spaces_count}{trans_type(key['type'])}"
                        f"{key['key']}: "
                        f"{trans_value(key['value'])}"
                    )

            elif 'children' in key.keys():
                lines.append(
                    f"{replacer * spaces_count}{trans_type(key['type'])}"
                    f"{key['key']}: "
                    f"{iter_(key['children'], spaces_count + 4)}"
                )

        result = itertools.chain(
            "{", lines, [(replacer * (spaces_count - 2)) + "}"]
        )
        return '\n'.join(result)

    return iter_(list_of_diff, 2)
