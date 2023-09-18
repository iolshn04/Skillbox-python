sms = input('Сообщение: ')
first_list = sms.split()
sms_list = []

for i_list in first_list:
    if i_list.isalpha():
        sms_list.append(i_list[::-1])
    else:
        end = i_list[len(i_list) - 1]
        new_list = list(i_list)
        word = end
        for i in new_list:
            if i == end:
                break
            else:
                word += i
        sms_list.append(word[::-1])

print('Новое сообщение:', ' '.join(sms_list))

# зачтено
