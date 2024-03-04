users = [
    ["Little pig", 4],
    ["Max", 1],
    ["Pulga", 5]
]

# users = []
# for user in users:
#   users.append(user[0])
# print(users)
# users = [user[0] for user in users]

# filter
users = [user for user in users if user[1] > 2]  # list comprehension
users3 = list(filter(lambda user: user[1] > 2, users))  # using filter
print(users)
print(users3)

users1 = list(map(lambda user: user[0], users))  # using map
users2 = [user[0] for user in users if user[1] > 2]  # list comprehension

print(users1)
print(users2)
