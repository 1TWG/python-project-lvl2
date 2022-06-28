# -*- coding:utf-8 -*-


cl_way = []


def make_cl_way(d1, d2):
    global cl_way
    cl_way = sorted(list(set(list(d1.keys()) + list(d2.keys()))))


# Рендеринг итоговой строки в текстовом представлении
def plaintify(d1, d2, way='', count=0):
    res_st = ''
    dict_keys = sorted(list(set(list(d1.keys()) + list(d2.keys()))))
    for i in dict_keys:
        if i in d1 and i not in d2:
            res_st += f"Property '{way + i}' was removed\n"
        if i in d1 and i in d2 \
                and type(d1[i]) is dict \
                and type(d2[i]) is dict:
            way += str(i) + '.'
            res_st += plaintify(d1[i], d2[i], way, count)
            way_t = way.split('.')[:-2]
            way = '.'.join(way_t) + '.'

        if i not in d1 and i in d2:
            if type(d2[i]) is dict:
                val = '[complex value]'
            else:
                val = d2[i]
            if str(val).isdigit():
                res_st += f"Property '{way + i}' was added with value: {val}\n"
            else:
                res_st += f"Property '{way + i}' was added with value: '{val}'\n"
        if i in d1 and i in d2 \
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
            if str(val2).isdigit():
                res_st += f"Property '{way + i}' was updated. " \
                          f"From '{str(val1)}' to {val2}\n"
            else:
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
