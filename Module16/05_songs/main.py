violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]
N = int(input('Сколько песен выбрать: '))
summ = 0

for i in range(1, N + 1):
    print('Название', i, '-й песни:', end=' ')
    name_song = input()
    for i_list in violator_songs:
        if name_song == i_list[0]:
            summ += i_list[1]
print('Общее время звучания песен:', round(summ, 2), 'минуты')

# зачтено
