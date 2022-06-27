# -*- coding:utf-8 -*-

from gendiff import parsing_cli
from gendiff import generate_diff


def main():
    args = parsing_cli()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()
