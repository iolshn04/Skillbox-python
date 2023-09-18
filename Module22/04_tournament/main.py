# first_file = open('first_tour.txt', 'w')
# num_list = []
k = input('Число баллов для второго тура: ')
# first_file.write(k + '\n')
# while True:
#     participants_list = input('Введите участника: ').split()
#     if participants_list[0] == 'end':
#         break
#     else:
#         num_list.append(participants_list)
# for i_elem in num_list:
#     participants = ' '.join(i_elem)
#     first_file.write(participants + '\n')
# first_file.close()

first_file = open('first_tour.txt', 'r')
count = 0
count_1 = 0
num_list_2 = []

for i_elem in first_file:

    if int(i_elem[-3:]) > int(k):
        count += 1
        num_list_2.append(i_elem)
second_file = open('second_tour.txt', 'w')
second_file.write(str(count) + '\n')

for i_elem in num_list_2[::-1]:
    members = i_elem.split()
    count_1 += 1
    second_file.write(str(count_1) + ') ' + members[1][0] + '. ' + members[0] + ' ' + members[2] + '\n')
second_file.close()

second_file = open('second_tour.txt', 'r', encoding='utf-8')
for i_elem in second_file:
    print(i_elem, end='')

# зачтено
