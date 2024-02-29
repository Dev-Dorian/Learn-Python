greeting = 25


def greet():
    global greeting
    greeting = "Hello World"


def greetingLittlePig():
    greeting = 24
    print(greeting)


result1 = greeting + 3
print(result1)
greet()
result2 = greeting + 3
print(result2)
