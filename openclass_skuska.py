users = [
    {'id': 1, 'name': 'Alice', 'age': 30, 'city': 'New York'},
    {'id': 2, 'name': 'Bob', 'age': 25, 'city': 'Los Angeles'},
    {'id': 3, 'name': 'Charlie', 'age': 35, 'city': 'New York'},
    {'id': 4, 'name': 'Diana', 'age': 28, 'city': 'Miami'}
]

def count_people_from_city(data, city):
	count = 0
	for data in users:
		if data["city"] == city:
			count += 1
	return count



users = [
    {'id': 1, 'name': 'Alice', 'age': 30, 'city': 'New York'},
    {'id': 2, 'name': 'Bob', 'age': 25, 'city': 'Los Angeles'},
    {'id': 3, 'name': 'Charlie', 'age': 35, 'city': 'New York'},
    {'id': 4, 'name': 'Diana', 'age': 28, 'city': 'Miami'}
]

new_york = count_people_from_city(users, "New York")
assert new_york == 2, "Z New Yorku jsou dva lidé"
miami = count_people_from_city(users, "Miami")
assert miami == 1, "Z Miami je jeden člověk"
denver = count_people_from_city(users, "Denver")
assert denver == 0, "Z Denveru není nikdo"