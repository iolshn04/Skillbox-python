import json

import requests

my_req = requests.get('https://swapi.dev/api/starships/10/')

data = json.loads(my_req.text)

pilot_list = []
for item in data['pilots']:
    req = requests.get(item)
    pilot = json.loads(req.text)
    pilot_dict = {}
    for key, val in pilot.items():
        if key == 'name' or key == 'height' or key == 'mass' or key == 'homeworld' or key == 'url':
            pilot_dict[key] = val
    pilot_list.append(pilot_dict)

new_data = {}
for key, val in data.items():
    if key == 'name' or key == 'max_atmosphering_speed' or key == 'starship_class':
        new_data[key] = val
new_data['pilots'] = pilot_list

with open('starship.json', 'w', encoding='utf-8') as file:
    json.dump(new_data, file, indent=4)

with open('starship.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
print(data)

# зачтено
