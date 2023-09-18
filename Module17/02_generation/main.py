N = int(input('Введите длину списка: '))
new_list = [(1 if i_list % 2 == 0 else i_list % 5) for i_list in range(N)]
print(new_list)

# зачтено
