def read_file(file_name):
    line_count = 0
    sym_sum = 0
    try:
        # Мы можем объявить несколько контекстных менеджеров за раз
        # Обязательно всегда явно указывай кодировку utf8!
        with open(file_name, 'r', encoding="utf8") as file, open('errors.log', 'w', encoding="utf8") as file_error:
            for i_line in file:
                line_count += 1
                # Метод .strip() убирает все пробельные символы у строки.
                # Затем нам лишь надо взять длину у этой "очищенной" строки
                # Это лучше, лаконичнее и читабельнее чем то что было до этого)
                length = len(i_line.strip())
                if length < 3:
                    # Сздаем строку с сообщением об ошибке
                    error_message = 'Ошибка: менее трёх символов в строке {}'.format(line_count)
                    # Выводим её в консоль
                    print(error_message)
                    # А также пишем в файл
                    file_error.write(error_message)

                sym_sum += length
    except:
        print('Что-то пошло не так')

    return sym_sum


result = read_file(file_name='people.txt')
# Печатаем итог
print(f"Общее количество символов: ", result)
