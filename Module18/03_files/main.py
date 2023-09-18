file_name = input('Название файла: ')
name = file_name.split('.')
names = ''.join(name)
if not names.isalpha():
    print('Ошибка: название начинается на один из специальных символов.')
elif not (names.endswith('txt') or names.endswith('docx')):
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')
else:
    print('Файл назван верно.')

# зачтено
