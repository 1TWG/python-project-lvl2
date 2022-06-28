from gendiff.parsing_cli import parsing_cli
from gendiff import generate_diff


def main():
    args = parsing_cli()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
