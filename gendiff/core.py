# -*- coding:utf-8 -*-

import argparse
import json


def parsing_cli():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('-f', '--format', help='set format of output')
    parser.add_argument('first_file')
    parser.add_argument('second_file')

    args = parser.parse_args()
    return args


# Находим различия между линейными json
def find_diff(file1, file2):
    with open(file1) as f1, open(file2) as f2:
        templates_first = json.load(f1)
        templates_second = json.load(f2)
    res = []

    # Проходим по первому файлу и удаляем его ключи из второго
    for i in templates_first:
        if i in templates_second:
            if templates_first[i] == templates_second[i]:
                res.append(f'  {i}: {templates_first[i]}')
            else:
                res.append(f'- {i}: {templates_first[i]}')
                res.append(f'+ {i}: {templates_second[i]}')
            templates_second.pop(i)
        else:
            res.append(f'- {i}: {templates_first[i]}')

    # Проходим по второму файлу
    for i in templates_second:
        res.append(f'+ {i}: {templates_second[i]}')
    # Собираем вывод
    res.sort(key=lambda x: x.split()[0])
    res.sort(key=lambda x: x.split()[1] if '+ ' in x or '- ' in x else x.split()[0])
    res = '{\n  ' + '\n  '.join(res) + '\n}'
    res = res.replace('True', 'true').replace('False', 'false')
    return res
