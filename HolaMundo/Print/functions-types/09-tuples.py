numbers = (1, 2, 3) + (4, 5, 6)
print(numbers)

point = tuple([1, 2])
print(point)

lessNumbers = numbers[:2]
print(lessNumbers)

first, second, *others = numbers
print(first, second, others)

for n in numbers:
    print(n)

# the tuples cannot be modified, only a new list created and we modify the list
listNumbers = list(numbers)
listNumbers[0] = "Happy Little Pig"
print(listNumbers)
