nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

outputt = [x for each_list_2 in nice_list for each_list in each_list_2 for x in each_list]
print(outputt)

# зачтено
