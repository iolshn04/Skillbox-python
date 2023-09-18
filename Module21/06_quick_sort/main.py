def sort_list(new_list):
    if len(new_list) <= 1:
        return new_list
    more_list = []
    less_list = []
    equal_list = []
    for i_elem in new_list:
        if new_list[-1] == i_elem:
            equal_list.append(i_elem)
        elif i_elem > new_list[-1]:
            more_list.append(i_elem)
        else:
            less_list.append(i_elem)

    return sort_list(less_list) + equal_list + sort_list(more_list)


old_list = [5, 8, 9, 4, 2, 9, 1, 8]

print(sort_list(old_list))

# зачтено
