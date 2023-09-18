class squareNum:
    """ Класс для реализации итератора квадратов чисел"""
    def __init__(self, numbers):
        self.__number = numbers
        self.__counter = 0
    def __iter__(self):
        return self
    def __next__(self):
        self.__counter += 1
        if self.__counter <= self.__number:
            return self.__counter ** 2
        else:
            raise StopIteration

my_iter = squareNum(9)
for elem in my_iter:
    print(elem, end=' ')

print()

#Функция-генератор для квадратов чисел
def squarenum(num):
    cur_val = 1
    while cur_val <= num:
        yield cur_val ** 2
        cur_val += 1

sqr = squarenum(num=9)
for elem in sqr:
    print(elem, end=' ')

print()
#Генераторное выражение для квадратов чисел

square_gen = (num ** 2 for num in range(1, 10))
for i_num in square_gen:
    print(i_num, end=' ')