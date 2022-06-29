cl_way = []


def make_cl_way(d1, d2):
    global cl_way
    cl_way = sorted(list(set(list(d1.keys()) + list(d2.keys()))))


def add_value(d2, i, way):
    if type(d2[i]) is dict:
        val = '[complex value]'
    else:
        val = d2[i]
    if str(val).isdigit():
        return f"Property '{way + i}' was added with value: {val}\n"
    else:
        return f"Property '{way + i}' " \
               f"was added with value: '{val}'\n"


def change_value(d1, d2, i, way):
    if type(d1[i]) is dict:
        val1 = '[complex value]'
    else:
        val1 = d1[i]
        if type(val1) is str:
            val1 = f"'{val1}'"
    if type(d2[i]) is dict:
        val2 = '[complex value]'
    else:
        val2 = d2[i]
        if type(val2) is str:
            val2 = f"'{val2}'"
    return f"Property '{way + i}' was updated. " \
           f"From {val1} to {val2}\n"


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
            res_st += add_value(d2, i, way)
        if i in d1 and i in d2 \
                and d1[i] != d2[i] \
                and (type(d1[i]) is not dict or type(d2[i]) is not dict):
            res_st += change_value(d1, d2, i, way)
        if i in cl_way:
            way = ''
    res_st = res_st.replace("'False'", 'false') \
        .replace("True", 'true') \
        .replace("None", 'null') \
        .replace("'[", '[') \
        .replace("]'", ']')

    return res_st
