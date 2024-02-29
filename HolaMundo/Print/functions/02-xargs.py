def addition(*numbers):
    result = 0
    for number in numbers:
        result += number
    print(result)


addition(2, 5, 3)
addition(2, 5, 10)
