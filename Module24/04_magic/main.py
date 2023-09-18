class Water:
    def __str__(self):
        return 'Вода'

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Vapor()
        elif isinstance(other, Earth):
            return Dirt()
        else:
            return None


class Air:
    def __str__(self):
        return 'Воздух'

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()
        else:
            return None


class Fire:
    def __str__(self):
        return 'Огонь'

    def __add__(self, other):
        if isinstance(other, Earth):
            return Lava()
        elif isinstance(other, Water):
            return Vapor()
        elif isinstance(other, Air):
            return Lightning()
        else:
            return None


class Earth:
    def __str__(self):
        return 'Земля'

    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Air):
            return Dust
        elif isinstance(other, Fire):
            return Lava
        else:
            return None


class Storm:
    def __str__(self):
        return 'Шторм'


class Vapor:
    def __str__(self):
        return 'Пар'


class Dirt:
    def __str__(self):
        return 'Грязь'


class Dust:

    def __str__(self):
        return 'Пыль'


class Lightning:

    def __str__(self):
        return 'Молния'


class Lava:

    def __str__(self):
        return 'Лава'


water = Water()
air = Air()
earth = Earth()
fire = Fire()
print('{} + {} = {}'.format(water, air, air + water))
print('{} + {} = {}'.format(water, fire, fire + water))
print('{} + {} = {}'.format(water, earth, earth + water))
print('{} + {} = {}'.format(air, fire, air + fire))
print('{} + {} = {}'.format(air, earth, air + earth))
print('{} + {} = {}'.format(fire, earth, fire + earth))

# зачтено
