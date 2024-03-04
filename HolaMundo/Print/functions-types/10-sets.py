# set means group
first = {1, 1, 2, 2, 3, 4, 6}
second = [3, 4, 5]
second = set(second)
# first.add(10)
# first.remove(1)

print(first | second)
print(first & second)
print(first - second)
print(first ^ second)

if 6 in second:
    print("Hello World")
