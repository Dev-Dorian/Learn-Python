number = 1
while number < 100:
    print(number)
    number *= 2

command = ""

while command.lower() != "salir":
    command = input("$ ")
    print(command)

 # Loop Infinite

""" while True:
    command1 = input("$ ")
    print(command1)
    if command1.lower() == "salir":
        break
 """
