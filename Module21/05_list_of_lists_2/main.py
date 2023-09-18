def flatten(new_list):
    result = []
    for i_elem in new_list:
        if isinstance(i_elem, int):
            result.append(i_elem)
        else:
            result.extend(flatten(i_elem))
    return result


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

print(flatten(nice_list))

# зачтено
