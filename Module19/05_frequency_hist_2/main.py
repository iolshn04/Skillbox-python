def histogram(string):
    sym_dict = dict()
    for sym in string:
        if sym in sym_dict:
            sym_dict[sym] += 1
        else:
            sym_dict[sym] = 1

    return sym_dict


text = input('Введите текст: ').lower()

hist = histogram(text)

print('Оригинальный словарь частот:')
for i_sym in sorted(hist.keys()):
    print(i_sym, ':', hist[i_sym])

print('Инвертированный словарь частот:')
for i in range(min(hist.values()), max(hist.values()) + 1):
    new_list = []
    for i_sym in hist.keys():
        if i == hist[i_sym]:
            new_list.append(i_sym)
    print(f'{i} : {new_list}')

# зачтено
