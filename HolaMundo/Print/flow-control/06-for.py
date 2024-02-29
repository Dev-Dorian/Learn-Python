search = 2

for number in range(5):
    print(number)
    if number == search:
        print("Found ", search)
        break
    else:
        print("I did not find the number I was looking for")

for char in "Ultimate Python":
    print(char)
