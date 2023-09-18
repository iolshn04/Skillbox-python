class Property:
    TAX_COEFF = 0

    def __init__(self, worth):
        self.worth = worth

    def tax(self):
        return self.worth * Property.TAX_COEFF


class Appartment(Property):
    TAX_COEFF = 1 / 1000
    NAME = "Квартира"

    def __init__(self, worth):
        super().__init__(worth)

    def tax(self):
        return Appartment.TAX_COEFF * self.worth


class Car(Property):
    TAX_COEFF = 1 / 200
    NAME = "Машина"

    def __init__(self, worth):
        super().__init__(worth)

    def tax(self):
        return Car.TAX_COEFF * self.worth


class CountryHouse(Property):
    TAX_COEFF = 1 / 500
    NAME = "Загородный дом"

    def __init__(self, worth):
        super().__init__(worth)

    def tax(self):
        return Car.TAX_COEFF * self.worth


def main():
    owner_name = input('Введите ваше имя: ')
    owner_cash = float(input(f'{owner_name}, введите доступные средства: '))

    total_tax = 0
    for PropertyClass in [Appartment, Car, CountryHouse]:
        answer = int(input(f'Есть ли у вас {PropertyClass.NAME} (0 - нет, 1 - есть): '))
        if not answer:
            continue

        worth = float(input(f'Введите стоимость {PropertyClass.NAME}: '))
        owner_property = PropertyClass(worth)

        total_tax += owner_property.tax()

    print(f'Общая сумма налога к уплате - {total_tax}')
    if total_tax > owner_cash:
        print('К сожалению, у вас не хватает денег для уплаты всех налогов')
        print(f'Недостающая сумма {total_tax - owner_cash}')
    else:
        print(f'После уплаты налогов у вас останется {owner_cash - total_tax}')


main()
