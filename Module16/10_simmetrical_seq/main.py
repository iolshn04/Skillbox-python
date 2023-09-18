def is_Palindrome(num):
    reverse_list = []
    for i_nums in range(len(num) - 1, -1, -1):
        reverse_list.append(num[i_nums])
    if reverse_list == num:
        return True
    else:
        return False


N = int(input('Кол-во чисел: '))
num_list = []
for _ in range(N):
    num = int(input('Число: '))
    num_list.append(num)
new_nums = []
answer = []

for i_nums in range(0, len(num_list)):
    for j_nums in range(i_nums, len(num_list)):
        new_nums.append(num_list[j_nums])
    if is_Palindrome(new_nums):
        for i_answer in range(0, i_nums):
            answer.append(num_list[i_answer])
        answer.reverse()
        break
    new_nums = []

print('Исходный список:', num_list)
print('Нужно приписать чисел:', len(answer))
print('Сами числа:', answer)

# зачтено
