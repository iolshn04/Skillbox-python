N = int(input('Введите количество пар слов: '))
words_list = []
flag = False
for i in range(N):
    print(i + 1, '-я пара: ', end='')
    words = input().lower()
    words_list.append(words.split(' — '))
    new_list = dict(words_list)

while True:
    word = input('Введите слово: ').lower()
    for i_key in new_list.keys():
        if i_key == word:
            print('Синоним:', new_list[i_key])
            flag = True
            break
        elif new_list[i_key] == word:
            print('Синоним:', i_key)
            flag = True
            break
    if flag:
        break
    else:
        print('Такого слова в словаре нет')

# зачтено
