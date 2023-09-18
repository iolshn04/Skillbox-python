ip_adress = input('Введите IP: ')
ip_list = ip_adress.split('.')
flag = False
if len(ip_list) == 4:
    for i_list in ip_list:
        if not i_list.isdigit():
            print(i_list, '- это не целое число')
            flag = False
            break
        else:
            if int(i_list) < 0:
                print(i_list, 'меньше 0')
                flag = False
                break
            elif int(i_list) > 255:
                print(i_list, 'превышает 255')
                flag = False
                break
            else:
                flag = True

else:
    print('Адрес — это четыре числа, разделённые точками.')
if flag:
    print('IP-адрес корректен.')

# зачтено
