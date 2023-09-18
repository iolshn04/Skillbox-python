import random

first_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
second_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
third_team = [(first_team[i_list] if first_team[i_list] > second_team[i_list] else second_team[i_list])
              for i_list in range(20)]
print('Первая команда:', first_team)
print('Вторая команда:', second_team)
print('Победители тура:', third_team)

# зачтено
