# -*- coding:utf-8 -*-


import json
import copy


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
    res_string = res_string.replace('True', 'true')\
        .replace('None', 'null')\
        .replace('False', 'false')
    return res_string


# Чтение файлов
def generate_diff(file1, file2):
    with open(file1) as f1, open(file2) as f2:
        templates_first = json.load(f1)
        templates_second = json.load(f2)
    dict_res = make_diff_dict(templates_first, templates_second)

    # dict_res = json.dumps(dict_res, indent=4)
    dict_res = stringify(dict_res, ' ', 2)
    return dict_res
