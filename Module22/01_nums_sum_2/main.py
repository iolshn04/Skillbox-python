file_num = open('numbers.txt', 'r')
summ = 0
for i_num in file_num:
    count_sum = i_num.split()
    if count_sum:
        summ += int(count_sum[0])
print(summ)

# зачтено
