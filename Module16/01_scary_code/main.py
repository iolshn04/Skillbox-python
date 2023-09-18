a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]
t = 0

a.extend(b)
for i in range(len(a)):
    if a[i] == 5:
        t += 1
for i in a:
    if i == 5:
        a.remove(i)
print('Кол-во цифр 5 при первом объединении:', t)

a.extend(c)
for i in range(len(a)):
    d = a.count(3)
print('Кол-во цифр 3 при втором объединении:', d)
print('Итоговый список:', a)

# зачтено
