# -*- coding:utf-8 -*-


import json
import os.path as path
import yaml
from gendiff.plaintify import plaintify, make_cl_way
from gendiff.stringify import make_diff_dict, stringify


# Чтение файлов
def generate_diff(file1, file2, format=None):
    with open(path.abspath(file1)) as f1, open(path.abspath(file2)) as f2:
        ext1, ext2 = path.splitext(file1)[1], path.splitext(file2)[1]
        if ext1 == '.json' and ext2 == '.json':
            templates_first = json.load(f1)
            templates_second = json.load(f2)
        elif ext1 in ('.yml', '.yaml') and ext2 in ('.yml', '.yaml'):
            templates_first = yaml.full_load(f1)
            templates_second = yaml.full_load(f2)
        else:
            return 'File extension is not supported'
    res = ''
    if not format:
        dict_res = make_diff_dict(templates_first, templates_second)
        res = stringify(dict_res, ' ', 2)
    elif format == 'plain':
        make_cl_way(templates_first, templates_second)
        res = plaintify(templates_first, templates_second)[:-1]
    elif format == 'json':
        dict_res = make_diff_dict(templates_first, templates_second)
        res = json.dumps(dict_res, indent=4)

    print(res)
    #return res
