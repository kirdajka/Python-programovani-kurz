class Package:
    def __init__(self, adress,weight,state):
        self.adress = adress
        self.weight = weight
        self.state = state
    def __str__(self):
        return self.adress

    def get_info(self):
        return f"Balik na {self.adress} ma hmotnost {self.weight} a je ve stavu {self.state}."
    
package_1 = Package ("Kremlikova 1",34.5,"nedorucen")
package_2 = Package ("predvoje",56.4,"dorucen")

print (package_1.get_info())

def delivery_price(self):
    if self.weight < 35:
        print(129)
    else:
        print(200)


def deliver(self):
    if self.state == "dorucen":
        return "Balík již byl doručen"
    elif self.state == "nedorucen":
        self.state = "dorucen"
        return "doruceni ulozeno"

print(deliver(package_1))

class Task:
    def __init__(self, description, assigned_to):
        self.description = description
        self.completed = False
        self.assigned_to = assigned_to

email_task = Task("Napsat e-mail zákazníkovi, že program je hotový.", "Jirka")

email_task.completed = True
print(email_task.completed)


class Task:
    def __init__(self, description,):
        self.description = description
        self.completed = False
        
# Potřebujeme, aby tento řádek nekončil chybou
task_1 = Task("Napsat e-mail zákazníkovi, že program je hotový.",) 
# Tento řádek ale musí pořád fungovat
task_2 = Task("Opravit chybu ve formuláři pro zadání adresy.", "Jirka")


