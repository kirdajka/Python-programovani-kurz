class Employee:
    def __init__(self, name, position, holiday_entitlement):
        self.name = name
        self.position = position
        self.holiday_entitlement = holiday_entitlement
    def take_holiday(self, days):
        if self.holiday_entitlement >= days:
            self.holiday_entitlement -= days
            return f"Užij si to."
        else:
            return f"Bohužel už máš nárok jen na {self.holiday_entitlement} dní."
class Manager(Employee):
    def __init__(self, name, position, holiday_entitlement, subordinates, car):
        super().__init__(name, position, holiday_entitlement)
        self.subordinates = subordinates
        self.car = car

class Salesman(Employee):
    def __init__(self, name, position, holiday_entitlement, car):
        # Volám metodu __init__() mateřské třídy
        super().__init__(name, position)
        self.car = car

marian = Manager("Marian Přísný", "vedoucí konstrukčního oddělení", 25, 5, "Škoda Octavia 1.5 TSI")

if isinstance(marian, Manager):
    print("Objekt pochází ze třídy Manager (nebo jejích potomků).")
else:
    print("Objekt nepochází ze třídy Manager (nebo jejích potomků).")


marian = Manager("Marian Přísný", "vedoucí konstrukčního oddělení", 25, 5, "Škoda Octavia 1.5 TSI")
marketa = Manager("Markéta Polková", "teamleader", 25, 12, "Škoda Octavia RS")
frantisek = Employee("František Novák", "konstruktér", 25)
employee_list = [marian, marketa, frantisek]

expected_people = 0

for item in employee_list:
    if isinstance(item, Manager):
        # Připravíme si pozvánku
        print(f"Pozvánka pro {item.name} na školení leadershipu.")
        # Započítáme si jednoho člověka navíc
        expected_people = expected_people + 1

print(f"Čekáme {expected_people} osob.")





class Item:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def get_info(self):
        return f"{self.title} stojí {self.price} Kč."

    def get_time_to_read(self):
        pass

# Navic pages atribut
class Book(Item):
    def __init__(self, title, price, pages):
        super().__init__(title, price)
        self.pages = pages

    def get_info(self):
        return f"Kniha {self.title} má {self.pages} stran a stojí {self.price} Kč."

    def get_time_to_read(self, minutes=4):
        return self.pages * minutes / 60

# navic duration_in_hours a narrator
class AudioBook(Item):
    def __init__(self, title, price, duration_in_hours, narrator):
        super().__init__(title, price)
        self.duration_in_hours = duration_in_hours
        self.narrator = narrator

    def get_info(self):
        # Jen ukazka jak se treba popasovat s vypisem
        return super().get_info().replace('Kniha', 'Audiokniha')

    def get_time_to_read(self):
        return self.duration_in_hours

audiokniha = AudioBook('Problém tří těles', 299, 14.4, 'Zbyšek Horák')
kniha = Book('Kadet Hornblower', 242, 399)
total_time = kniha.get_time_to_read() + audiokniha.get_time_to_read()
# print(f'Budes potrebovat {total_time} h')

favourite_narrator = "Zbyšek Horák"
item_1 = AudioBook("Problém tří těles", 299, 14.4, "Zbyšek Horák")
item_2 = Book("Kadet Hornblower", 399, 242)
item_3 = AudioBook("Odysseus", 389, 13.7, "Lukáš Hlavica")

all_items = [item_1, item_2, item_3]

for item in all_items:
    if getattr(item, "narrator",0) == favourite_narrator:
        print (getattr(item, "title"))

 