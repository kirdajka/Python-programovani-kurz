venecky = [1, 2, 4, 1, 6, 0, 1]
#chciupravit cislo na pozici 3
venecky[3]=2
#posledni tri cisla pomoci zaporneho indexu
print(venecky[-3:])
delka=len(venecky)
print(delka)
venecku_celkem = sum(venecky)
print(venecku_celkem)
nejmensi_prvek = min(venecky)
print(nejmensi_prvek)
print(max(venecky))
serazeny_zeznam = sorted(venecky)
print(serazeny_zeznam)
jmeno = "Denisa Kirdajova"
print(jmeno[2:5])
len(jmeno)
print(len(jmeno))
inzerat = "Na této pracovní pozici budete využívat Java a SQL"
if "Python" in inzerat:
    print("je to pro mne")
else:
    print("no") 
pohyby = [1200, -250, -800, 540, 721, -613, -222]
print(pohyby[2])
print(pohyby[2:])
print(len(pohyby))
print(max(pohyby))
print(min(pohyby))
print(sum(pohyby))
print(sum(pohyby)/len(pohyby))
s = [-2,3,7,6,5,19,5]
print(sum(s)/len(s))
print(max(pohyby)-min(pohyby))
print(max(s)-min(s))
inzerat = inzerat.upper()
print(inzerat)
inzerat = inzerat.upper()
print(inzerat)
jmeno = "   Denisa "
jmeno = jmeno.strip()
print(len(jmeno))
n = "po ut st čt pá"
jmena = ["Herec A", "Herečka A", "Herec B", "Herečka B"]
jmena_na_plakat = ", ".join(jmena)
print(jmena_na_plakat)
text = "Kurz vede lektor Marek"
text = text.replace("Marek","Pavel")
print(text)
jmeno="Denisa Kirdajova"
jmeno = jmeno.upper()
print(jmeno)
jmeno = jmeno.lower()
print(jmeno)
hodnoty = ['12', '1', '7', '-11']
f = hodnoty[2]
print(f)
s= int(f)+4
hodnoty[-2]= s
print(hodnoty)
import math
cislo = 2.47
zaokruhlene_cislo = math.ceil(cislo)
print(zaokruhlene_cislo)
hodnoty = '12.1 1.68 7.45 -11.51'
nove_hodnoty = hodnoty.split( )
print(nove_hodnoty)
f = nove_hodnoty[-1]
prepocteno = float(f) + 0.25
nove_hodnoty[-1] = str(prepocteno)
hodnoty = " ".join(nove_hodnoty)
print(hodnoty)
import statistics
votes = [
    "curling", 
    "vánoční svařák na trzích", 
    "vánoční svařák na trzích", 
    "curling", 
    "zážitková první pomoc",
    "curling", 
    "zážitková první pomoc",
    "curling",
    "zážitková první pomoc",  ]

print(statistics.mode(votes))
a = 3.45
lst = (1,2,3,4,5,6,7)
def middle_odd(lst):
    middle_index = len(lst) // 2  # Calculate the middle index
    return(lst[middle_index])  # Print the middle element
print (middle_odd(lst))
lst2 = (1,2,3,4,5,6)
def middle_even(lst2):
    middle_index = (len(lst2) // 2) -1  # Calculate the middle index
    return(lst2[middle_index])  # Print the middle element
print (middle_even(lst2))
venecky = [1, 2, 4, 1, 6, 0, 1]
print(venecky[10])

jen_cisla = "123"
cisla_a_pismena = "ABC123"

print(jen_cisla.isdecimal())









    










         
        

