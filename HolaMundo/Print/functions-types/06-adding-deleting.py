pets = [
    "Wolfgang",
    "Pelusa",
    "Pulga",
    "Max",
    "Pulga",
    "Little pig happy"
]
pets.insert(1, "Himalaya")
pets.append("Little pig sad")
print(pets)

pets.remove("Himalaya")
pets.pop(1)
del pets[0]
# pets.clear()
print(pets)
