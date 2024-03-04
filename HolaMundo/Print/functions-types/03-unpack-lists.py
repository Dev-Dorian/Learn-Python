numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#
# first = numbers[0]
# second = numbers[1]
# third = numbers[2]

first, second, four, *others, penultimate, last = numbers
print(second, others, penultimate, last)
# print(second)
