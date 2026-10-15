'''
Haydn Moyer
People
'''



person1 = {
    "first_name": "Roquan",
    "last_name": "Downep Jr",
    "age": 58,
    "city": "New York City"
}

person2 = {
    "first_name": "Mike",
    "last_name": "Evans",
    "age": 98,
    "city": "Boston, Massachusetts"
}

person3 = {
    "first_name": "Mark",
    "last_name": "Rualo",
    "age": 36,
    "city": "Keosha, Wisconsin"
}

people = [person1, person2, person3]

for person in people:
    print("\nPerson:")
    print(f"First name: {person['first_name']}")
    print(f"Last name: {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}")