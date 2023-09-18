text = input('Введите строку: ')
count = 0
word = ''
word_start = text.find('h')
word_end = text.rfind('h')
for i_list in range(word_start + 1, word_end):
    word += text[i_list]
print('Развёрнутая последовательность между первым и последним h:', word[::-1])

# зачтено
