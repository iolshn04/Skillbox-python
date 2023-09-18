def divider(number):
    for i in range(2, number + 1):
        if number % i == 0:
            break
    print('Наименьший делитель, отличный от единицы:', i)


number = int(input('Введите число: '))

divider(number)

# зачтено
