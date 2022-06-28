import copy


# Создание diff словаря
def make_diff_dict(d1, d2):
    d_diff = {}
    dict_keys = sorted(list(set(list(d1.keys()) + list(d2.keys()))))
    for i in dict_keys:
        if i in d1 and i in d2:
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
            if len(str(temp_dict_s[i])) > 0:
                res_string += str(replace * spacecount) + str(i) \
                              + ': ' + str(temp_dict_s[i]) + '\n'
            else:
                res_string += str(replace * spacecount) + str(i) \
                              + ': ' + '\n'
    res_string += '}'
    res_string = res_string.replace('True', 'true') \
        .replace('None', 'null') \
        .replace('False', 'false')
    return res_string
