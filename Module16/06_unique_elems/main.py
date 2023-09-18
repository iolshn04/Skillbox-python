first_list = []
second_list = []
for i in range(1, 4):
    print('Введите', i, '-е число для первого списка:', end=' ')
    num = int(input())
    first_list.append(num)
for i in range(1, 8):
    print('Введите', i, '-е число для второго списка:', end=' ')
    num = int(input())
    second_list.append(num)

print('Первый список', first_list)
print('Второй список', second_list)

first_list.extend(second_list)
for i in first_list:
    for j in range(1, first_list.count(i)):
        first_list.remove(i)
print(first_list)

# зачтено
