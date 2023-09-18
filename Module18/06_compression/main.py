new_string = input('Введите строку: ')
new_string += ' '
string_list = list(new_string)
code_string = []
count_sym = 1
i_sym = string_list[0]

for i in range(1, len(string_list)):
    if string_list[i] == string_list[i - 1]:
        count_sym += 1
    else:
        code_string.append(string_list[i - 1])
        code_string.append(str(count_sym))
        count_sym = 1
print(''.join(code_string))

# зачтено
