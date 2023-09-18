import random

N = int(input('Количество чисел в списке: '))
num_list = [random.randint(0, 2) for _ in range(N)]
print('Список до сжатия:', num_list)
for i_list in num_list:
    if i_list == 0:
        num_list.remove(i_list)
        num_list.append(i_list)
for i_list in num_list:
    if i_list == 0:
        num_list.remove(i_list)

print('Список после сжатия:', num_list)

# зачтено
