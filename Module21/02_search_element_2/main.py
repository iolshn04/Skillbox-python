site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def find_key(structure, my_key, depth=None):
    if depth is None or depth >= 1:
        if my_key in structure:
            return structure[my_key]
    else:
        return None
    for element in structure.values():
        if isinstance(element, dict) and depth != None:
            result = find_key(element, my_key, depth - 1)
            if result:
                break
        elif isinstance(element, dict):
            result = find_key(element, my_key)
            if result:
                break
    else:
        result = None
    return result


key = input('Введите искомый ключ: ')
answer = input('Хотите ввести максимальную глубину? Y/N: ').lower()
if answer == 'y':
    maximum_depth = int(input('Введите максимальную глубину: '))
    value_key = find_key(site, key, maximum_depth)
elif answer == 'n':
    value_key = find_key(site, key)
print(f'Значение ключа: {value_key}')

# зачтено
