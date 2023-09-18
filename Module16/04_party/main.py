def delete_guest(name, guest):
    for i_list in guest:
        if i_list == name:
            return True
    return False


guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
count = 5

print('Сейчас на вечеринке', count, 'человек', guests)
text = input('Гость пришел или ушёл? ')

while text != 'Пора спать':
    name_guest = input('Имя гостя: ')
    if text == 'пришёл':
        if count < 6:
            guests.append(name_guest)
            count += 1
            print('Привет', name_guest, '!')
        else:
            print('Прости,', name_guest, ', но мест нет.')
    if text == 'ушёл':
        if delete_guest(name_guest, guests):
            guests.remove(name_guest)
            count -= 1
            print('Пока,', name_guest, '!')
        else:
            print('Такого гостя нет на вечеринке')
    print('Сейчас на вечеринке', count, 'человек', guests)
    text = input('Гость пришёл или ушёл? ')
print('Вечеринка закончилась, все легли спать.')

# зачтено
