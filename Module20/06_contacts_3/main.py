def surname(telephone_dict):
    user_search = input('Введите фамилию для поиска: ')
    user_search = user_search.title()
    for i_user in telephone_dict:
        if user_search in i_user:
            print(i_user[0], i_user[1], telephone_dict[i_user])


def telephone(telephone_dict):
    key = input('Введите имя и фамилию нового контакта (через пробел): ')
    value = int(input('Введите номер телефона: '))
    key = tuple(key.split())
    if key in telephone_dict:
        print('Такой человек уже есть в контактах.')
    else:
        telephone_dict[key] = value
    return telephone_dict


number_dict = {}
while True:
    print('Введите номер действия:')
    command = int(input('1. Добавить контакт \n2. Найти человека \n'))
    if command == 1:
        telephone(number_dict)
        print('Текущий словарь контактов:', number_dict)
    else:
        surname(number_dict)

# зачтено
