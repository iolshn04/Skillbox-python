def summ_number(N):
    summ = 0
    if N > 0:
        while N != 0:
            count_number = N % 10
            summ += count_number
            N //= 10
        print('Сумма чисел', summ)
        return summ
    else:
        print('Введите положительное число: ')


def count(N):
    count_summ = 0
    while N != 0:
        count_number = N % 10
        count_summ += 1
        N //= 10
    print('Количество цифр в числе', count_summ)
    return count_summ


N = int(input('Введите число: '))

print('Разность суммы и количества цифр', summ_number(N) - count(N))

# зачтено
