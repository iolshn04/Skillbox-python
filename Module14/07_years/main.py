def years(start, end):
    for i in range(start, end + 1):
        first = i // 1000
        second = i // 100 % 10
        third = i % 100 // 10
        four = i % 10
        if first == second and first == third or first == second and first == four or first == third and first == four or second == third and second == four:
            print(i)


start = int(input('Введите первый год: '))
end = int(input('Введите второй год: '))
print('Годы от', start, 'до', end, 'с тремя одинаковыми цифрами:')
years(start, end)

# зачтено
