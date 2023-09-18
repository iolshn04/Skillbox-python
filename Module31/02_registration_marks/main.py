import re


def find_car_numbers(text):
    car_numbers = re.findall(r'[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}', text)
    return car_numbers


def find_taxi_numbers(text):
    taxi_numbers = re.findall(r'[АВЕКМНОРСТУХ]{2}\d{3}\d{2,3}', text)
    return taxi_numbers


input_text = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'

car_numbers = find_car_numbers(input_text)
taxi_numbers = find_taxi_numbers(input_text)

print('Список номеров частных автомобилей:', car_numbers)
print('Список номеров такси:', taxi_numbers)

# зачтено
