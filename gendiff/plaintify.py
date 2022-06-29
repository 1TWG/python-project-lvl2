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
    values = []
    for j in (d1, d2):
        if type(j[i]) is dict:
            values.append('[complex value]')
        elif type(j[i]) is str:
            values.append(f"'{j[i]}'")
        else:
            values.append(j[i])

    return f"Property '{way + i}' was updated. " \
           f"From {values[0]} to {values[1]}\n"


def plantify_for_one(i, d1, d2, way):
    is_in_first = i in d1 and i not in d2
    is_in_second = i not in d1 and i in d2
    if is_in_first:
        return f"Property '{way + i}' was removed\n"
    elif is_in_second:
        return add_value(d2, i, way)
    else:
        return ''


# Рендеринг итоговой строки в текстовом представлении
def plaintify(d1, d2, way='', count=0):
    res_st = ''
    dict_keys = sorted(list(set(list(d1.keys()) + list(d2.keys()))))
    for i in dict_keys:
        if i in d1 and i in d2:
            is_both_dict = type(d1[i]) is dict and type(d2[i]) is dict
            is_one_dict = d1[i] != d2[i] and (type(d1[i]) is not dict
                                              or type(d2[i]) is not dict)
            if is_both_dict:
                way += str(i) + '.'
                res_st += plaintify(d1[i], d2[i], way, count)
                way_t = way.split('.')[:-2]
                way = '.'.join(way_t) + '.'
            if is_one_dict:
                res_st += change_value(d1, d2, i, way)
        res_st += plantify_for_one(i, d1, d2, way)
        if i in cl_way:
            way = ''
    res_st = res_st.replace("'False'", 'false') \
        .replace("True", 'true') \
        .replace("None", 'null') \
        .replace("'[", '[') \
        .replace("]'", ']')

    return res_st
