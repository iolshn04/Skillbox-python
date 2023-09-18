def city_dict(country, city):
    for i_key in country.keys():
        if city in country[i_key]:
            return i_key
    return False


N = int(input('Количество стран: '))
country_dict = dict()
for i_list in range(1, N + 1):
    print(i_list, 'страна: ', end='')
    country_user = input()
    country_list = country_user.split()
    country_dict[country_list[0]] = country_list[1:]

first_city = input('Первый город: ')
key = city_dict(country_dict, first_city)
if key:
    print(f'Город {first_city} расположен в стране {key}')
else:
    print(f'По городу {first_city} данных нет.')

second_city = input('Второй город: ')
key = city_dict(country_dict, second_city)
if key:
    print(f'Город {second_city} расположен в стране {key}')
else:
    print(f'По городу {second_city} данных нет.')

third_city = input('Третий город: ')
key = city_dict(country_dict, third_city)
if key:
    print(f'Город {third_city} расположен в стране {key}')
else:
    print(f'По городу {third_city} данных нет.')

# зачтено
