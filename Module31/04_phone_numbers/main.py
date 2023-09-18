import re


def check_phone_numbers(phone_numbers):
    pattern = r'^[89]\d{9}$'

    for num, val in phone_numbers.items():
        if re.match(pattern, val):
            print('{}: всё в порядке'.format(num))
        else:
            print('{}: не подходит'.format(num))


phone_list = {'первый номер': '9999999999', 'второй номер': '999999-999', 'третий номер': '99999x9999'}

check_phone_numbers(phone_list)

# зачтено
