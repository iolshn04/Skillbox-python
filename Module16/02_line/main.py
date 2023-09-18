first_class = list(range(160, 177, 2))
second_class = list(range(162, 181, 3))
first_class.extend(second_class)
index = 0
for i_list in range(len(first_class)):
    index += 1
    for number in range(index, len(first_class)):
        if first_class[i_list] > first_class[index]:
            min_num = first_class[i_list]
            first_class[i_list] = first_class[index]
            first_class[index] = min_num
print('Отсортированный список:', first_class)

# зачтено
