first_file = open('text.txt', 'r')


def histogram(string_1):
    special_sym = ".,:;!_*-+()/#%& "
    sym_dict = dict()
    for sym in string_1:
        if sym in sym_dict and sym not in special_sym:
            sym_dict[sym] += 1
        elif sym not in sym_dict and sym not in special_sym:
            sym_dict[sym] = 1
    return sym_dict


for i_elem in first_file:
    string = list(i_elem.lower())

hist = histogram(string)
summ = sum(hist.values())
sorted_list = sorted(hist.values(), reverse=True)
sorted_dict = {}
for i_elem in sorted_list:
    for j_elem in sorted(hist):
        if i_elem == hist[j_elem]:
            sorted_dict[j_elem] = i_elem

for i_elem in sorted_dict:
    print(i_elem, ':', round(hist[i_elem] / summ, 3))
first_file.close()

# зачтено
