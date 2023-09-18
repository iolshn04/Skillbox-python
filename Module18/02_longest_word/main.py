string = input('Введите строку: ')

max = ''
string_list = string.split()
for i in string_list:
    if len(max) < len(i):
        max = i
print('Самое длинное слово:', max)
print('Длина этого слова:', len(max))

# зачтено
