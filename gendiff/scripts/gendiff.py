# -*- coding:utf-8 -*-

from gendiff import parsing_cli
from gendiff import generate_diff


def main():
    args = parsing_cli()
    # poetry run gendiff tests/files/file1.json tests/files/file2.json
    # poetry run gendiff tests/files/filepath1.json tests/files/filepath2.json
    # poetry run gendiff -f plain tests/files/file1.json tests/files/file2.json
    # poetry run gendiff -f plain tests/files/filepath1.json tests/files/filepath2.json
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()
