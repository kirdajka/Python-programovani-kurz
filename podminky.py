number_of_tickets = int(input("Kolik si přejete lístků? "))
price_per_ticket = 190
total_price = number_of_tickets * price_per_ticket
if total_price >= 500:
    discount = 0.1
    total_price = total_price * (1 - discount)
    print(f"Získáváte slevu {discount * 100} %")

print(f"Celková cena nákupu je {int(total_price)} Kč.")

number_of_tickets = int(input("Kolik si přejete lístků? "))
price_per_ticket = 190
total_price = number_of_tickets * price_per_ticket
if total_price >= 500:
    discount = 0.1
    total_price = total_price * (1 - discount)
    print(f"Získáváte slevu {discount * 100}.")
else:
    to_discount = total_price - 500
    print(f"Nakupjte ještě za {to_discount} Kč a získáte slevu 10 %!")

print(f"Celková cena nákupu je {total_price} Kč.")

number_of_tickets = int(input("Kolik si přejete lístků? "))
price_per_ticket = 190
total_price = number_of_tickets * price_per_ticket
if total_price >= 1500:
    discount = 0.2
    total_price = total_price * (1 - discount)
    print(f"Získáváte slevu {discount * 100}.")
elif total_price >= 500:
    discount = 0.1
    total_price = total_price * (1 - discount)
    print(f"Získáváte slevu {discount * 100}.")
else:
    to_discount = total_price - 500
    print(f"Nakupjte ještě za {to_discount} Kč a získáte slevu 10 %!")

print(f"Celková cena nákupu je {total_price} Kč.")

age = int(input("Jaký je Váš věk? "))
if age >= 13:
    number_of_tickets = int(input("Kolik si přejete lístků? "))
    price_per_ticket = 190
    total_price = number_of_tickets * price_per_ticket
    if total_price >= 1500:
        discount = 0.2
        total_price = total_price * (1 - discount)
        print(f"Získáváte slevu {discount * 100}.")
    elif total_price >= 500:
        discount = 0.1
        total_price = total_price * (1 - discount)
        print(f"Získáváte slevu {discount * 100}.")
    else:
        to_discount = total_price - 500
        print(f"Nakupjte ještě za {to_discount} Kč a získáte slevu 10 %!")

    print(f"Celková cena nákupu je {total_price} Kč.")