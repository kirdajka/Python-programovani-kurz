import math 

class Locality:
    def __init__(self, name,coefficient):
        self.name = name
        self.coefficient = coefficient
    
    def __str__(self):
        return f"{self.name} (koeficient {self.coefficient})"

class Property:
    def __init__(self,locality,):
        self.locality = locality

class Estate(Property):
    def __init__(self, locality,estate_type,area):
        super().__init__(locality)
        self.estate_type = estate_type
        self.area = area
   
    def __str__(self):
        return f"{self.estate_type}, lokalita {self.locality} ({self.area} metrů čtverečních), daň {self.calculate_tax()} Kč"
    
    def calculate_tax(self):
        if self.estate_type == "land":
            coefficient = 0.85
        elif self.estate_type == "building site":
            coefficient = 9
        elif self.estate_type == "forrest":
            coefficient = 0.35
        else:
            print ("Invalid estate_type")
        tax = math.ceil (self.area * coefficient * self.locality.coefficient)
        return tax
  
class Residence(Property):
    def __init__(self, locality, area, commercial=False):
        super().__init__(locality)
        self.area = area
        self.commercial = commercial

    
    def calculate_tax(self):
        if self.commercial == False:
            tax = math.ceil (self.area * self.locality.coefficient)
        elif self.commercial == True:
            tax = tax*2
        return tax
    
    def __str__(self):
        return f"{self.commercial} nemovitost, lokalita {self.locality} ({self.area} metrů čtverečních), daň {self.calculate_tax()} Kč"

    





    