
# class employee

class Employee:
    def __init__(self, name , position, holiday_entitlement):
        self.name = name
        self.position = position
        self.holiday_entitlement = holiday_entitlement

    def __str__(self):
        return f"Zaměstnanec {self.name} pracuje na pozici {self.position}."

    def get_info(self):
        return f"Zamestnanec {self.name} pracuje jako {self.position}."
    
    def take_holiday(self, days):
        if self.holiday_entitlement >= days:
            self.holiday_entitlement -= days
            return f"Užij si to."
        else:
            return f"Bohužel už máš nárok jen na {self.holiday_entitlement} dní."

employee_1 = Employee("Frantisek","konstrukter",25)
employee_2 = Employee("klara","konstrikter",23)
print(employee_2.get_info())
print(employee_1)


class Package:
    def __init__(self, adress,weight,state):
        self.adress = adress
        self.weight = weight
        self.state = state

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

delivery_price(package_1)

class Book:
    def __init__(self,title, pages,price,sold,costs):
        self.title = title
        self.pages = pages
        self.price = price
        self.sold = sold
        self.costs = costs

    
    def get_info(self):
        return f"Kniha s nazvom {self.title} ma {self.pages} stran a jej cena je {self.price}."
    
    def profit(self):
        self.sold * (self.price - self.costs)
    
    def rating(self):
        profit = self.profit()
        if profit < 50000:
            return "propadak"
        elif profit > 500000:
            return "uspech"
        else:
            return "prumer"


book_1 = Book ("kto chyta v zite",400,555,45,345)
book_2 = Book ("1984",423,467,34,56)

print (book_1.get_info())

print(book_1.profit())
print(book_1.rating())




    