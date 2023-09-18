import random


class Buddhist:
    def __init__(self, karma=0):
        self.__karma = karma

    def get_karma(self):
        return self.__karma

    def set_karma(self, enlightenment):
        self.__karma += enlightenment


def one_day(count):
    if random.randint(1, 10) == 1:
        with open('karma.log', 'a', encoding='utf-8') as karma_log:
            misdemeanor = random.choice(
                ['KillError', 'DrunkError', 'CarCrashError', 'GluttonyError', 'DepressionError'])
            karma_log.write('День {}: проступок - {}\n'.format(count, misdemeanor))
            Flag = False
            return Flag
    else:
        return random.randint(1, 7)


Flag = False
buddhist = Buddhist()
day = 0

while buddhist.get_karma() < 500:
    day += 1
    if Flag:
        pass
    else:
        buddhist.set_karma(one_day(day))
print('Просветление достигнуто')

# зачтено
