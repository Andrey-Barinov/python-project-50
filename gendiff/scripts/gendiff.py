import argparse
from gendiff.generator import generate_dict_of_diff
from gendiff.stylish import default_format
'#!/usr/bin/env python3'


parser = argparse.ArgumentParser(
    description="Compares two configuration files and shows a difference.",
    usage="gendiff [-h] [-f FORMAT] first_file second_file",
)


parser.add_argument('first_file')

parser.add_argument('second_file')

parser.add_argument('-f', '--format', help="set format of output")


args = parser.parse_args()


def main():
    diff = generate_dict_of_diff(args.first_file, args.second_file)

    print(default_format(diff))


if __name__ == '__main__':
    main()
