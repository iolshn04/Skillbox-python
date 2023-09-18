def is_prime(n):
    prime = True
    i = 2

    while i < n:
        if n % i == 0:
            prime = False
            break
        i += 1

    if prime:
        return prime


def crypto(another_list):
    result_list = []
    for i_index, i_value in enumerate(another_list):
        if is_prime(i_index) and i_index != 0 and i_index != 1:
            result_list.append(i_value)
    return result_list


print(crypto(list(range(11))))

# зачтено
