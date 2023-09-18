def tpl_sort(tpl):
    for element in tpl:
        if not isinstance(element, int):
            return tpl
    return tuple(sorted(tpl))

# tup_list = (6, 3, -1, 8, 4, 10, -5)
# print(tpl_sort(tup_list))

# зачтено
