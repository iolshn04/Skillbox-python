def reverse_file(file):
    reverse = ''
    reverse_list = []
    for i_file in file:
        reverse_list.append(i_file.split())
    reverse_list.reverse()
    for i_file in reverse_list:
        reverse = ' '.join(i_file)
        print(reverse)
    return reverse


file_name = open('zen.txt', 'r')

reverse_file(file_name)

# зачтено
