class Parent:
    def __init__(self, name, age, children):
        self.name = name
        self.age = age
        self.children = []

    def print_info(self):
        print('Родитель:\n Имя: {}\n Возраст: {}'.format(
            self.name, self.age)
        )
        print(' Дети:', end=' ')
        for i_child in self.children:
            print(i_child.name, i_child.age, 'лет', end=' ')

    def is_calm(self, child):
        if child.calm_state == 1:
            print(f'Папа {self.name} спешит утешить {child.name}! ')
            child.calm_state = 0
        else:
            print(f'Папа {self.name} рад, что {child.name} спокоен! ')

    def is_feed(self, child):
        if child.hungry_state == 0:
            print(f'Папа {self.name} спешит накормить {child.name}! ')
            child.hungry_state = 1
        else:
            print(f'Папа {self.name} рад, что {child.name} сыт! ')


class Child:
    calm_states = {0: 'спокоен ', 1: 'плачет '}
    hungry_states = {0: 'голоден ', 1: 'сыт '}

    def __init__(self, child_name, child_age):
        self.name = child_name
        self.age = child_age
        self.calm_state = 0
        self.hungry_state = 0

    def __str__(self):
        return 'Ребенок:\n Имя: {}\n Возраст: {}\n Состояние спокойствия: {}\n Состояние голода: {}'.format(
            self.name, self.age, Child.calm_states[self.calm_state], Child.hungry_states[self.hungry_state],
        )


# parentName = input('Как зовут родителя? ')
# parentAge = int(input(f'Сколько {parentName} лет? '))
parent = Parent('Олег', 30, children=[])

# child_1Name = input('Как зовут ребенка? ')
# child_1Age = int(input(f'Сколько {child_1Name} лет? '))
# if parentAge - child_1Age < 16:
#     raise Exception('Это невозможно')
child_1 = Child('Ваня', 10)
parent.children.append(child_1)

# child_2Name = input('Как зовут ребенка? ')
# child_2Age = int(input(f'Сколько {child_2Name} лет? '))
# if parentAge - child_2Age < 16:
#     raise Exception('Это не может быть')
child_2 = Child('Варя', 12)
parent.children.append(child_2)

parent.print_info()
print('\n')
parent.is_feed(child_1)
print(child_1)

# зачтено
