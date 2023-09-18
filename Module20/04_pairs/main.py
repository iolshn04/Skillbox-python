import random

number_list = [random.randint(1, 9) for i_num in range(10)]
new_number_list = list(zip(number_list[::2], number_list[1::2]))
print('Оригинальный список:', number_list)
print('Новый список:', new_number_list)

# 2 способ решения
# number_list = [random.randint(1,9) for i_num in range(10)]
# new_number_list = []
# i = 0
# for _ in range(5):
#     new_number_list.append(tuple(number_list[i:i+2]))
#     i +=2
#
# print('Оригинальный список:', number_list)
# print('Новый список:', new_number_list)

# зачтено
