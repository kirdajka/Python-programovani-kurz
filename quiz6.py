class Employee:
    def __init__(self, name, position, holiday_entitlement):
        self.name = name
        self.position = position
        self.holiday_entitlement = holiday_entitlement

class Salesman(Employee):
    def __init__(self, name, position, holiday_entitlement, car):
        super().__init__(name, position, holiday_entitlement)
        self.car = car
frantisek = Employee("František Novák", "konstruktér", 25)
jakub = Salesman("Jakub Nový", "business development manager", 25, "Škoda Octavia")

print(isinstance(jakub, Employee))
print(isinstance(frantisek, Salesman))