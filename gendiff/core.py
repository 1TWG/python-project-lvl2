# -*- coding:utf-8 -*-


import json
import copy

cl_way = []


def make_cl_way(d1, d2):
    global cl_way
    cl_way = sorted(list(set(list(d1.keys()) + list(d2.keys()))))


def plaintify(d1, d2, way='', count=0):
    res_st = ''
    dict_keys = sorted(list(set(list(d1.keys()) + list(d2.keys()))))
    for i in dict_keys:
        if i in d1 and i not in d2:
            res_st += f"Property '{way + i}' was removed\n"
        elif i in d1 and i in d2 \
                and type(d1[i]) is dict \
                and type(d2[i]) is dict:
            way += str(i) + '.'
            res_st += plaintify(d1[i], d2[i], way, count)
            way_t = way.split('.')[:-2]
            way = '.'.join(way_t) + '.'

        elif i not in d1 and i in d2:
            if type(d2[i]) is dict:
                val = '[complex value]'
            else:
                val = d2[i]
            res_st += f"Property '{way + i}' was added with value: '{val}'\n"
        elif i in d1 and i in d2 \
                and d1[i] != d2[i] \
                and (type(d1[i]) is not dict or type(d2[i]) is not dict):
            if type(d1[i]) is dict:
                val1 = '[complex value]'
            else:
                val1 = d1[i]
            if type(d2[i]) is dict:
                val2 = '[complex value]'
            else:
                val2 = d2[i]
            res_st += f"Property '{way + i}' was updated. " \
                      f"From '{str(val1)}' to '{val2}'\n"
        if i in cl_way:
            way = ''
    res_st = res_st.replace("'False'", 'false') \
        .replace("'True'", 'true') \
        .replace("'None'", 'null') \
        .replace("'[", '[') \
        .replace("]'", ']')

    return res_st


# Создание diff словаря
def make_diff_dict(d1, d2):
    d_diff = {}
    dict_keys = sorted(list(set(list(d1.keys()) + list(d2.keys()))))
    for i in dict_keys:
        if i in d1 and i in d2:
            if type(d1[i]) is dict and type(d2[i]) is dict:
                d_diff['  ' + i] = make_diff_dict(d1[i], d2[i])
            elif type(d1[i]) is dict and type(d2[i]) is str:
                d_diff['- ' + i] = make_diff_dict(d1[i], d1[i])
                d_diff['+ ' + i] = d2[i]
            else:
                if d1[i] == d2[i]:
                    d_diff['  ' + i] = d1[i]
                else:
                    d_diff['- ' + i] = d1[i]
                    d_diff['+ ' + i] = d2[i]
        if i in d1 and i not in d2:
            if type(d1[i]) is dict:
                d_diff['- ' + i] = make_diff_dict(d1[i], d1[i])
            else:
                d_diff['- ' + i] = d1[i]

        if i not in d1 and i in d2:
            if type(d2[i]) is dict:
                d_diff['+ ' + i] = make_diff_dict(d2[i], d2[i])
            else:
                d_diff['+ ' + i] = d2[i]
    return d_diff


# Рендеринг итоговой строки
def stringify(d, replace, spacecount):
    temp_dict_s = copy.deepcopy(d)
    res_string = '{\n'
    for i in temp_dict_s:
        if type(temp_dict_s[i]) is dict:

            res_string += str(replace * spacecount) \
                          + str(i) + ': ' \
                          + stringify(temp_dict_s[i],
                                      replace, spacecount + 4)[0:-1] \
                          + str(replace * spacecount) + '  }\n'
        else:
            res_string += str(replace * spacecount) + str(i) \
                          + ': ' + str(temp_dict_s[i]) + '\n'
    res_string += '}'
    res_string = res_string.replace('True', 'true') \
        .replace('None', 'null') \
        .replace('False', 'false')
    return res_string


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

    return res
