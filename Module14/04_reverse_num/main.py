def numberback(N):
    firstnumber = int(N)
    summ = ''
    differance = int((N - firstnumber) * 100)
    while firstnumber != 0:
        first = str(firstnumber % 10)
        summ += first
        firstnumber //= 10
    summ += '.'

    while differance != 0:
        second = str(differance % 10)
        summ += second
        differance //= 10
    number = float(summ)
    return number


first_number = float(input('Введите первое число: '))
second_number = float(input('Введите второе число: '))

print('Первое число наоборот:', numberback(first_number))
print('Второе число наоборот:', numberback(second_number))
print('Сумма:', numberback(first_number) + numberback(second_number))

# зачтено
