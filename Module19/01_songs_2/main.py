violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}
sound = 0
numbers = int(input('Сколько песен выбрать? '))
for i_dict in range(1, numbers + 1):
    print(f'Название {i_dict} песни:', end=' ')
    names = input('')
    sound += float(violator_songs[names])
print('Общее время звучания песен: ', round(sound, 2), 'минуты')

# зачтено
