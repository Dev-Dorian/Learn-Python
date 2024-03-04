numbers = [2, 4, 1, 45, 75, 22]

numbers.sort()
print(numbers)

# numbers.reverse()
numbers.sort(reverse=True)
print(numbers)

numbers2 = sorted(numbers)
print(numbers2)

numbers2 = sorted(numbers, reverse=True)
print(numbers2)

users = [
    ["Little pig", 4],
    ["Max", 8],
    ["Pulga", 2]
]


def sort(element):
    return element[1]


users.sort(key=sort)
print(users)

users.sort(key=sort, reverse=True)
print(users)

users.sort(key=lambda el: el[1])  # sorting with lambda expressions
print(users)
