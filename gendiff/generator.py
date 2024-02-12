from gendiff.parser import parser


def change_key(val):
    def walk(values):
        dict_of_changed_keys = {}
        if not isinstance(val, dict):
            return val
        for key, value in values.items():
            dict_of_changed_keys[f"  {key}"] = change_key(value)

        return dict_of_changed_keys
    return walk(val)


def generate_dict_of_diff(file1, file2):

    data1 = parser(file1)

    data2 = parser(file2)

    def walk(curr_data1, curr_data2):
        dict_of_diff = {}
        for key in sorted(curr_data1.keys() | curr_data2.keys()):
            if (key in curr_data1) and (key in curr_data2)\
                    and curr_data1[key] == curr_data2[key]:
                dict_of_diff[f"  {key}"] = change_key(curr_data1[key])

            elif not (key in curr_data1):
                dict_of_diff[f"+ {key}"] = change_key(curr_data2[key])

            elif not (key in curr_data2):
                dict_of_diff[f"- {key}"] = change_key(curr_data1[key])

            elif not isinstance(curr_data1[key], dict) \
                    or not isinstance(curr_data2[key], dict):
                dict_of_diff[f"- {key}"] = change_key(curr_data1[key])
                dict_of_diff[f"+ {key}"] = change_key(curr_data2[key])

            else:
                dict_of_diff[f"  {key}"] = walk(
                    curr_data1[key], curr_data2[key]
                )

        return dict_of_diff

    return walk(data1, data2)
