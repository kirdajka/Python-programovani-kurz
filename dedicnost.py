
class Package:
    def __init__(self, adress,weight,state):
        self.adress = adress
        self.weight = weight
        self.state = state

    def __str__(self):
        return f"Balik na {self.adress} ma hmotnost {self.weight} a je ve stavu {self.state}."

    def delivery_price(self):
        if self.weight < 35:
            return 129
        else:
           return 200

    

class ValuablePackage(Package):
    def __init__(self, adress,weight,state,value):
        super().__init__(adress,weight,state)
        self.value = value
    def __str__(self):
        return super().__str__() + f"Cena balika je {self.value} Czk."
    def delivery_price(self):
        price = super().delivery_price()
        return price * 1.05

package_1 = ValuablePackage("Grimmauldovo náměstí 11", 1.9, "nedoručen", 5500)
package_2 = Package("Godrikův důl 47", 1.9, "nedoručen")
package_3 = ValuablePackage("Vydrník svatého Drába 13", 1.9, "nedoručen", 5500)
package_list = [package_1, package_2, package_3]

total_value = 0

for package in package_list:
    if getattr(package, "state") == "nedoručen":
        total_value += getattr(package, "value",0)
    
        

print(total_value)



