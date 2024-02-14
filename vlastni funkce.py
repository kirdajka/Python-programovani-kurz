def greet_user():
    print("Ahoj!")
greet_user()

def greet_user(name):
    print(f"Ahoj {name}!")


greet_user("Jirko")

def sum_two_numbers(a, b):
    return a + b
returned_value = sum_two_numbers(5, 3)
print(returned_value)



def convert_to_euro(crown):
    exchange_rate = 26
    return crown /exchange_rate
print(convert_to_euro(100))

def convert_to_euro(crown, exchange_rate):
    return crown * exchange_rate

def get_mark(points):
    if points <= 60:
        mark = 5
    elif points <= 70:
        mark = 4
    elif points <= 80:
        mark = 3
    elif points <= 90:
        mark = 2
    else:
        mark = 1
    return mark

points = int(input("Zadej počet bodů v testu: "))
mark = get_mark(points)
if mark == 5:
    points = int(input("Zadej počet bodů v opravném pokusu: "))
    mark = get_mark(points)
print(f"Výsledná známka je {mark}.")

def mult(a,b):
    return(a*b)
multiple_value = mult(5,3)
print(multiple_value)

def kilometry_na_mile(kilometry):
    return (kilometry*1.6)
print(kilometry_na_mile(100))

def mily_na_kilometry(mile):
    return (mile/1.6)
print(mily_na_kilometry(100))

def print_with_border(text, border_char='*'):
    # Délka textového řetězce plus mezery a dva znaky pro okraje
    line_length = len(text) + 4
    # Horní a dolní okraj
    border = border_char * line_length
    
    print(border)
    print(f"{border_char} {text} {border_char}")
    print(border)

# Základní použití
print_with_border("ahoj")
print_with_border("ahoj", "#")

def month_of_birth(birth_number):
    birth_number_str = str(birth_number)
    month = int(birth_number_str[2:4])
    if month > 50:
        month -= 50
    return month
print(month_of_birth(9207054439))  # Výstup: 7
print(month_of_birth(9555125899))  # Výstup: 5

def get_mark(points, bonus=0):
    if points + bonus <= 60:
        mark = 5
    elif points + bonus <= 70:
        mark = 4
    elif points + bonus <= 80:
        mark = 3
    elif points + bonus <= 90:
        mark = 2
    else:
        mark = 1
    return mark

points = int(input("Zadej počet bodů v testu: "))
bonus = int(input("Zadej počet bonusových bodů: "))
mark = get_mark(points, bonus)
if mark == 5:
    points = int(input("Zadej počet bodů v opravném pokusu: "))
    mark = get_mark(points, bonus)
print(f"Výsledná známka je {mark}.")

def sum_two_numbers(a, b):
    return a + b
value = sum_two_numbers(2, 3)
assert value == 4, "Sum of 2 a 3 should be 5"