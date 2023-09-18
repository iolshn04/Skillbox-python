skate_list = []
people_list = []
count_max = 0
skates_count = int(input('Кол-во коньков: '))
for i in range(1, skates_count + 1):
    print('Размер', i, '-й пары:', end=' ')
    size_skate = int(input())
    skate_list.append(size_skate)

people_count = int(input('Кол-во людей: '))
for i in range(1, people_count + 1):
    print('Размер ноги', i, '-го человека:', end=' ')
    size_people = int(input())
    people_list.append(size_people)

for i_list in people_list:
    for i_size in skate_list:
        if i_list >= i_size:
            count_max += 1
            people_list.remove(i_list)
            skate_list.remove(i_size)
print('Наибольшее кол-во людей, которые могут взять ролики:', count_max)

# зачтено
