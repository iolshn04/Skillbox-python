shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

summ = 0
detail = input('Название детали: ')
count_details = int(input('Кол-во деталей: '))
for i_list in shop:
    if i_list[0] == detail:
        summ += i_list[1]
        count_details -= 1
        if count_details == 0:
            break
print('Общая стоимость деталей:', summ)
