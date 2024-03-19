from datetime import datetime
zacatek_lekce = "13. 3. 2024 18:00"
# Doplň kód do uvozovek
zacatek_lekce = datetime.strptime(zacatek_lekce, "%d. %m. %Y %H:%M")
print(zacatek_lekce)


def time_to_christmas():
    return datetime(2024, 12, 24, 18, 0) - datetime.now()
print(time_to_christmas)

for _ in range(9):
    print("I love Python")