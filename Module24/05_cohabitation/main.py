import random


class Human:
    def __init__(self, name, satiety=50, food=50, money=0):
        self.name = name
        self.satiety = satiety
        self.food = food
        self.money = money

    def day(self, action):
        if self.satiety < 20 and self.food >= 10:
            self.satiety += 10
            self.food -= 10
            print('{} поел'.format(self.name))
        elif self.food and self.money > 10:
            self.food += 20
            self.money -= 10
            print('{} сходил в магазин'.format(self.name))
        elif action == 1:
            self.money += 50
            print('{} работает'.format(self.name))
        elif action == 2:
            self.satiety += 10
            self.food -= 10
            print('{} кушает'.format(self.name))
        else:
            self.satiety -= 10
            print('{} играет'.format(self.name))


class Result:
    def __init__(self, man_1, man_2):
        self.man_1 = man_1
        self.man_2 = man_2

    def death(self):
        if self.man_1.satiety == 0 or self.man_2.satiety == 0:
            return True, print('Один из людей умер')


human_1 = Human('Ваня')
human_2 = Human('Варя')

result = Result(human_1, human_2)
count_day = 0

while True:
    count_day += 1
    if count_day == 365:
        print('Эксперимент удался. Все живы')
        break
    elif result.death():
        break
    else:
        r = random.randint(1, 6)
        human_1.day(r)
        human_2.day(r)

print(count_day)

# зачтено
