N = int(input('Кол-во друзей: '))
K = int(input('Долговых расписок: '))
friends = []
for _ in range(N):
    friends.append(0)
for index in range(1, K + 1):
    print(index, '-я расписка')
    send = int(input('Кому: '))
    receive = int(input('От кого: '))
    money = int(input('Сколько: '))
    friends[send - 1] = friends[send - 1] - money
    friends[receive - 1] = friends[receive - 1] + money
print('Баланс друзей:')
for i in range(1, N + 1):
    print(i, ':', friends[i - 1])

# зачтено
