first_string = input('Первая строка: ')
second_string = input('Вторая строка: ')
max = len(first_string) - 1
flag = True
for i_list in range(1, len(first_string) - 1):
    third_list = second_string[i_list:]
    if first_string.startswith(third_list) and i_list != max:
        print('Первая строка получается из второй со сдвигом', i_list)
        flag = False
        break
if flag:
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')

# зачтено
