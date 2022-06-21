# -*- coding:utf-8 -*-

from gendiff.core import parsing_cli
from gendiff.core import generate_diff


def main():
    args = parsing_cli()
    # poetry run gendiff tests/files/file1.json tests/files/file2.json
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == '__main__':
    main()
