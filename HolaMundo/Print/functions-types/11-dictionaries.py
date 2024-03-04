point = {"x": 25, "y": 50}
# print(point)
# print(point["x"])
# print(point["y"])

point["z"] = 45
# print(point)

# if "lala" in point:
#    print("encontre lala", point["lala"])

# print(point.get("x"))
# print(point.get("lala", 97))
del point["x"]
del (point["y"])

# print(point)
point["x"] = 25

for value in point:
    print(value, point[value])

for value in point.items():
    print(value)

for key, value in point.items():
    print(key, value)

users = [
    {"id": 1, "name": "Little Pig"},
    {"id": 2, "name": "Happy"},
    {"id": 3, "name": "Nicolas"},
    {"id": 4, "name": "Felipe"},
]

for user in users:
    print(user["name"])
