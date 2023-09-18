def caesar_cipher(string, user_shift):
    char_list = [(alphabet[(alphabet.index(sym) + user_shift) % 33] if sym != ' ' else ' ') for sym in string]
    new_list = ''
    for i_list in char_list:
        new_list += i_list
    return new_list


alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
text = input('Введите сообщение: ')
shift = int(input('Введите сдвиг: '))

output = caesar_cipher(text, shift)

print('Зашифрованное сообщение:', output)

# зачтено
