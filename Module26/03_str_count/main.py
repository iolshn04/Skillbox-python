import os


def count_lines_in_files(directory):
    files = [f for f in os.listdir(directory) if f.endswith('.py')]

    for file in files:
        file_path = os.path.join(directory, file)
        count = 0

        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

            for line in lines:
                line = line.strip()
                if not line:
                    continue
                if line.startswith('#'):
                    continue
                count += 1
        yield count

path_abs = os.path.abspath(os.path.join('..', '..', 'Module14/01_os_info'))
print(path_abs)
directory = path_abs
lines_counts = count_lines_in_files(directory)

for count in lines_counts:
    print(count)
