def generate_list_of_diff(data1, data2):
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

            elif isinstance(curr_data1[key], dict) \
                    and isinstance(curr_data2[key], dict):
                result.append({'key': key,
                               'type': 'nested',
                               'children': walk(
                                   curr_data1[key], curr_data2[key]
                               )
                               })
            else:
                result.append({'key': key,
                               'type': 'updated',
                               'value1': curr_data1[key],
                               'value2': curr_data2[key]
                               })
        return result

    return walk(data1, data2)
