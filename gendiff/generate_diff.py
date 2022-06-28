# -*- coding:utf-8 -*-


import json
from gendiff.plaintify import plaintify, make_cl_way
from gendiff.stringify import make_diff_dict, stringify


# Чтение файлов
def generate_diff(file1, file2, format=None):
    with open(file1) as f1, open(file2) as f2:
        templates_first = json.load(f1)
        templates_second = json.load(f2)
    if not format:
        dict_res = make_diff_dict(templates_first, templates_second)
        res = stringify(dict_res, ' ', 2)
    elif format == 'plain':
        make_cl_way(templates_first, templates_second)
        res = plaintify(templates_first, templates_second)[:-1]
    elif format == 'json':
        dict_res = make_diff_dict(templates_first, templates_second)
        res = json.dumps(dict_res, indent=4)

    return res
