people = [
    {"name":"Rommer", "house": "house1"},
    {"name":"Cora", "house": "house2"},
    {"name":"Peter", "house": "house3"},
    {"name":"Abi", "house": "house4"},
    {"name":"John", "house": "house5"}
]

# def f(people):
#     return people["name"]    

# people.sort(key=f)

# Apply lambda for single line statement
people.sort(key=lambda person: person["name"])

print(people)