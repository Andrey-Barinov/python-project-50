from gendiff.parser import parser


def generate_list_of_diff(file1, file2):
    data_from_file1 = parser(file1)

    data_from_file2 = parser(file2)

    def walk(curr_data1, curr_data2):
        result = []
        for key in sorted(curr_data1.keys() | curr_data2.keys()):
            if (key in curr_data1) and (key in curr_data2) \
                    and curr_data1[key] == curr_data2[key]:
                result.append({'key': key,
                               'type': 'unchanged',
                               'value': curr_data1[key]
                               })

            elif not (key in curr_data1):
                result.append({'key': key,
                               'type': 'added',
                               'value': curr_data2[key]
                               })

            elif not (key in curr_data2):
                result.append({'key': key,
                               'type': 'deleted',
                               'value': curr_data1[key]
                               })

            elif not isinstance(curr_data1[key], dict) \
                    or not isinstance(curr_data2[key], dict):
                result.append({'key': key,
                               'type': 'deleted',
                               'value': curr_data1[key]
                               })
                result.append({'key': key,
                               'type': 'added',
                               'value': curr_data2[key]
                               })
            else:
                result.append({'key': key,
                               'type': 'changed',
                               'children': walk(
                                   curr_data1[key], curr_data2[key]
                               )
                               })

        return result

    return walk(data_from_file1, data_from_file2)
