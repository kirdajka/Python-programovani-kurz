recept = {
    'nazev': 'Batáty se šalvějí a pancettou',
    'narocnost': 'stredni',
    'doba': 30,
    'ingredience': [
        ['batát', '1', '15 kč'],
        ['olivový olej', '2 lžíce', '2 kč'],
        ['pancetta', '4-6 plátků', '21 kč'],
        ['přepuštěné máslo', '2 lžíce', '5 kč'],
        ['mletý černý pepř', '1/2 lžičky', '0.5 kč'],
        ['sůl', '1/2 lžičky', '0.1 kč'],
        ['muškátový oříšek', 'špetka', '1 kč'],
        ['česnek', '2 stroužky', '1 kč'],
        ['šalvějové lístky', '20-25', '12 kč']
    ]
}
celkem = 0
for ingredience in recept["ingredience"]:
    cena_text = ingredience [2] 
    cena = float(cena_text.split(' ')[0])
    celkem += cena
print (f" recept stoji celkem {celkem} Kc")

purchase_list = [
    {"Jméno": "Petr", "Položka": "Prací prášek", "Částka": 399},
    {"Jméno": "Ondra", "Položka": "Savo", "Částka": 80},
    {"Jméno": "Petr", "Položka": "Toaletní papír", "Částka": 65},
    {"Jméno": "Libor", "Položka": "Pivo", "Částka": 124},
    {"Jméno": "Petr", "Položka": "Pytel na odpadky", "Částka": 75},
    {"Jméno": "Míša", "Položka": "Utěrky na nádobí", "Částka": 130},
    {"Jméno": "Ondra", "Položka": "Toaletní papír", "Částka": 120},
    {"Jméno": "Míša", "Položka": "Pečící papír", "Částka": 30},
    {"Jméno": "Zuzka", "Položka": "Savo", "Částka": 80},
    {"Jméno": "Pavla", "Položka": "Máslo", "Částka": 50},
    {"Jméno": "Ondra", "Položka": "Káva", "Částka": 300}
]

sum_per_person = {}
for item in purchase_list:
    person = item["Jméno"]
    value = item["Částka"]
    if person in sum_per_person:
        sum_per_person[person] += value
    else:
        sum_per_person[person] = value

total_value = 0
for person, value in sum_per_person.items():
    total_value += value
    print(f"{person} utratil(a) za společné nákupy {value} Kč.")
import statistics
sum_per_person = {}

for polozka in purchase_list:
    person = polozka["Jméno"]
    value = polozka["Částka"]
    sum_per_person[person] = sum_per_person.get(person, 0) + value
average_value = statistics.mean(sum_per_person.values())

for person, value in sum_per_person.items():

    diff = round(value - average_value)

    if diff > 0:
        print(f'{person} dostane {diff}')
    elif diff < 0:
        print(f'{person} zaplati {abs(diff)}')
    else:
        print(f'{person} je na nule')