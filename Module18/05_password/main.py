def upper_word(password_user):
    for i_num in password_user:
        if i_num.isupper():
            return True
            break
    return False


def number_word(password_number):
    numbers = '1,2,3,4,5,6,7,8,9'
    count = 0
    for i_list in password_number:
        if i_list in numbers:
            count += 1
    if count >= 3:
        return True
    else:
        return False


password = input('Придумайте пароль: ')
while True:
    if len(password) >= 8 and number_word(password) and upper_word(password):
        print('Это надежный пароль!')
        break
    else:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
        password = input('Придумайте пароль: ')

# зачтено
