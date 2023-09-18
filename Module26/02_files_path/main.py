import os


def gen_files_path(directory="/Users/"):
    file_paths = []
    target_directory = input('Введите каталог, который нужно найти: ')

    for adress, dirs, files in os.walk(directory):
        if target_directory in dirs:
            target_path = os.path.join(adress, target_directory)
            for dirpath, dirnames, filenames in os.walk(target_path):
                for filename in filenames:
                    file_paths.append(os.path.join(dirpath, filename))

    return file_paths

files = gen_files_path()
for file_path in files:
    print(file_path)