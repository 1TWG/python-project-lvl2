import copy


# Удаление и добавления элемента в файл
def remove_add_val(d1, i, d_diff, action):
    if type(d1[i]) is dict:
        d_diff[action + i] = make_diff_dict(d1[i], d1[i])
    else:
        d_diff[action + i] = d1[i]


def diff_value(d1, d2, i, d_diff):
    if type(d1[i]) is dict and type(d2[i]) is dict:
        d_diff['  ' + i] = make_diff_dict(d1[i], d2[i])
    elif type(d1[i]) is dict and type(d2[i]) is not dict:
        d_diff['- ' + i] = make_diff_dict(d1[i], d1[i])
        d_diff['+ ' + i] = d2[i]
    elif type(d1[i]) is not dict and type(d2[i]) is dict:
        d_diff['- ' + i] = d1[i]
        d_diff['+ ' + i] = make_diff_dict(d2[i], d2[i])
    else:
        if d1[i] == d2[i]:
            d_diff['  ' + i] = d1[i]
        else:
            d_diff['- ' + i] = d1[i]
            d_diff['+ ' + i] = d2[i]


# Создание diff словаря
def make_diff_dict(d1, d2):
    d_diff = {}
    dict_keys = sorted(list(set(list(d1.keys()) + list(d2.keys()))))
    for i in dict_keys:
        in_first = i in d1
        in_second = i in d2
        if in_first and in_second:
            diff_value(d1, d2, i, d_diff)
        if in_first and not in_second:
            remove_add_val(d1, i, d_diff, '- ')
        if not in_first and in_second:
            remove_add_val(d2, i, d_diff, '+ ')
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
