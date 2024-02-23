from gendiff.gen_diff import generate_diff
from gendiff.formatters.select_format import select_format
from gendiff.cli import args
'#!/usr/bin/env python3'


def main():
    output_format = select_format(args.format)
    diff = generate_diff(args.first_file, args.second_file, output_format)

    print(diff)


if __name__ == '__main__':
    main()
