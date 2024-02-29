# and, or, not

gas = False
turn_on = False
age = 18

if not gas and (turn_on or age > 17):
    print('You can move forward')

if not gas and turn_on and age > 19:
    print("You can move forward")
