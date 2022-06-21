# -*- coding:utf-8 -*-

from gendiff.core import parsing_cli
from gendiff.core import find_diff


def main():
    args = parsing_cli()
    # poetry run gendiff tests/files/file1.json tests/files/file2.json
    diff = find_diff(args.first_file, args.second_file)
    print(diff)

def generate_diff(file1, file2):
    diff = find_diff(file1, file2)
    print(diff)

if __name__ == '__main__':
    main()
