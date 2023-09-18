def number_print(num):
    if num == 0:
        return 1
    number_print(num - 1)
    print(num)


number = int(input('Введите num: '))
number_print(number)

# зачтено
