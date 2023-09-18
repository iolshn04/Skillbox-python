def my_sum(*args):
    total_sum = 0
    for i_elem in args:
        if isinstance(i_elem, int):
            total_sum += i_elem
        elif isinstance(i_elem, (list, tuple)):
            total_sum += my_sum(*i_elem)
    return total_sum


print(my_sum([[1, 2, [3]], [1], 3]))

# зачтено
