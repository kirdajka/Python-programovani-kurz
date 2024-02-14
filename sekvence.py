flight_number = input("Zadejte číslo letu: ")
prefix = flight_number[0] + flight_number[1]
if prefix == "BA":
    company = "British Airways"
elif prefix == "LH":
    company = "Lufthansa"
else:
    company = "Neznámá společnost"
print(f"Letíte se společností {company}")

guest_list = ["Jirka", "Klára", "Natálie"]
new_guest = input("Zadej jméno dalšího hosta: ")
guest_list.append(new_guest)
print(guest_list)

incoming_person = input("Zadej jméno příchozího hosta: ")
if incoming_person in guest_list:
    print("Buď vítán(a)!")
else:
    print("Bohužel nejsi na seznamu.")

school_marks = [
    ["Jiří", 1, 4, 3, 2],
    ["Natálie", 2, 3, 4, 3],
    ["Tereza", 1, 1, 2, 1],
]

print(f"První student(ka) v seznamu je {school_marks[0][0]}.")
print(f"Její/jeho poslední známka je {school_marks[0][-1]}.")
