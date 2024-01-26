from gendiff.parser import parser


def generate_str_of_diff(list_of_diff):
    result = ''

    for item in list_of_diff:

        if len(item) == 3:
            result += f" {item[2]} {item[0]}: {item[1]}\n"

        elif len(item) == 4:
            result += f" - {item[0]}: {item[1]}\n"
            result += f" + {item[0]}: {item[2]}\n"

        else:
            result += f" + {item[0]}: {item[1]}\n"

    result = '{\n' + result + '}'

    return result


def generate_diff(file1, file2):

    data1 = parser(file1)

    data2 = parser(file2)

    list_of_diff = []

    for key, value in data1.items():

        if key in data2 and value == data2[key]:
            list_of_diff.append([key, value])

        elif key in data2 and value != data2[key]:
            list_of_diff.append([key, value, data2[key], 'diff_values'])

        else:
            list_of_diff.append([key, value, '-'])

    for key, value in data2.items():

        if key not in data1.keys():

            list_of_diff.append([key, value, '+'])

    return generate_str_of_diff(sorted(list_of_diff))
