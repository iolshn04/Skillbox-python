array_1 = [1, 5, 10, 20, 40, 80, 100]

array_2 = [6, 7, 20, 80, 100]

array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

array_fir = set(array_1)
array_tw = set(array_2)
array_th = set(array_3)
print(array_fir, array_tw, array_th)
print('Решение со множествами: ')
print('Первая задача:', array_fir & array_tw & array_th)
print('Вторая задача:', array_fir - (array_th | array_tw))
print()

print('Решение без множеств:')
array_4 = []
for i_dict in array_1:
    if i_dict in array_2 and i_dict not in array_4 and i_dict in array_3:
        array_4.append(i_dict)
print('Первая задача:', array_4)

array_3.extend(array_2)
array_4 = []
for i_dict in array_1:
    if i_dict not in array_3:
        array_4.append(i_dict)
print('Вторая задача:', array_4)

# зачтено
