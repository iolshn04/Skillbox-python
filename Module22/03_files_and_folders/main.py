import os


def search_file(cur_path, summ_list=[0, 0, 0]):
    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        if os.path.isdir(path):
            search_file(path)
            summ_list[1] += 1
        elif os.path.isfile(path):
            size = os.stat(path).st_size
            summ_list[0] += size
            summ_list[2] += 1
    return summ_list


path_abs = os.path.abspath(os.path.join('..', '..', 'Module14'))

result_file = search_file(path_abs)
print(path_abs)
print('Размер каталога (в Кб):', result_file[0] / 1024)
print('Количество подкаталогов:', result_file[1])
print('Количество файлов:', result_file[2])

# зачтено
