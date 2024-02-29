n1 = input("Enter First Number ")
n2 = input("Enter Second Number ")

n1 = int(n1)
n2 = int(n2)

addition = n1 + n2
subtraction = n1 - n2
multiplication = n1 * n2
division = n1 / n2

message = f"""For the numbers {n1} and {n2},
the result of the addition is {addition},
the result of the subtraction is {subtraction},
the result of the multiplication is {multiplication},
the result of the division is {division}.
"""
print(message)
