N = int(input('Кол-во человек: '))
people_list = list(range(1, N + 1))
start = 0
K = int(input('Какое число в считалке? '))
print('Значит, выбывает каждый', K, '-й человек')
while len(people_list) > 1:
    print('Текущий круг людей:', people_list)
    print('Начало счета с номера', people_list[start])
    start = (start + K - 1) % len(people_list)
    print('Выбывает человек под номером', people_list[start])
    people_list.remove(people_list[start])
    if start > 1:
        start = 0
print('Остался человек под номер', people_list[0])

# зачтено
