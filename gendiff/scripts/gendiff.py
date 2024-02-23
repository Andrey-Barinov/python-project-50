from gendiff.gen_diff import generate_diff
from gendiff.cli import args
'#!/usr/bin/env python3'


def main():
    diff = generate_diff(args.first_file, args.second_file, args.format)

    print(diff)


if __name__ == '__main__':
    main()
