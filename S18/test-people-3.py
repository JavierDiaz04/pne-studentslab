import json

# Cargar archivo JSON
with open("people-3.json", "r") as file:
    data = json.load(file)

people = data["people"]

# Imprimir total de personas
print(f"Total people in the database: {len(people)}\n")

# Recorrer e imprimir datos
for person in people:
    print(f"Name: {person['name']}")
    print(f"Age: {person['age']}")

    phones = person["phone_numbers"]
    print(f"Phone numbers: {len(phones)}")

    for i, phone in enumerate(phones):
        print(f"  Phone {i}:")
        print(f"    Type: {phone['type']}")
        print(f"    Number: {phone['number']}")

    print()  # línea en blanco entre personas