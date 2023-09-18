text = input('Введите текст: ')
count = 0
count_list = []
for i in range(len(text)):
    if text[i] in 'ауоыиэяюёе':
        count += 1
        count_list.append(text[i])
print('Список гласных букв:', count_list)
print('Длина списка', count)

# зачтено
