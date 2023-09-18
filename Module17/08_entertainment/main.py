import random

N = int(input('Количество палок: '))
new_list = ['I'] * N
K = int(input('Количество бросков: '))
for i in range(K):
    Left_i = random.randint(1, N - 1)
    Right_i = random.randint(Left_i + 1, N)
    print(f'Бросок {i + 1}. Cбиты палки с номера {Left_i} \nпо номер {Right_i}')
    stick_list = [('.' if Left_i <= stick <= Right_i else 'I') for stick in range(1, 11)]
    new_list = [
        (stick_list[i_list] if new_list[i_list] != stick_list[i_list] and new_list[i_list] == 'I' else new_list[i_list])
        for i_list in range(N)]
print(''.join(new_list))

# зачтено
