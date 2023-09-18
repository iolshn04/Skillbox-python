site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}


def change_values(struct, key, value):
    if key in struct:
        struct[key] = value
    else:
        for sub_struct in struct.values():
            if isinstance(sub_struct, dict):
                change_values(sub_struct, key, value)
    return struct


def display_site(struct, spaces=1):
    for key, value in struct.items():
        if isinstance(value, dict):
            print(print(' ' * spaces + '{', key), key)
            display_site(value, spaces + 3)
            print(' ' * spaces + '}')
        else:
            print("{}{} : {}".format(' ' * spaces, key, value))


def make_site(name):
    struct_site = site.copy()
    new_title = 'Куплю/продам {} недорого'.format(name)
    struct_site = change_values(struct_site, 'title', new_title)
    new_h2 = 'У нас самая низкая цена на {}'.format(name)
    struct_site = change_values(struct_site, 'h2', new_h2)

    return struct_site


sites = []
count_site = int(input('Сколько сайтов? '))

for _ in range(count_site):
    new_product = input('Введите название продукта для нового сайта: ')
    new_site = make_site(new_product)
    sites.append(new_site)
    for i_site in sites:
        display_site(i_site)

# зачтено
