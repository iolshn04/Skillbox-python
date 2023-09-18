import random


class Warrior:
    def __init__(self, name, health):
        self.name = name
        self.health = health


warrior_1 = Warrior('Воин_1', 100)
warrior_2 = Warrior('Воин_2', 100)

while True:
    number = random.randint(1, 2)
    if number == 1:
        warrior_2.health -= 20
        print('{} атаковал {}, здоровья осталось: {}'.format(
            warrior_1.name, warrior_2.name, warrior_2.health)
        )
    else:
        warrior_1.health -= 20
        print('{} атаковал {}, здоровья осталось: {}'.format(
            warrior_2.name, warrior_1.name, warrior_1.health)
        )
    if warrior_1.health == 0:
        print('Победил {}'.format(warrior_2.name))
        break
    elif warrior_2.health == 0:
        print('Победил {}'.format(warrior_1.name))
        break

# зачтено
