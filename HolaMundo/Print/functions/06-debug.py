def large(text):
    result = 0
    for _ in text:
        result += 1
    return result


print("Little Pig")
l = large("Hello World")
print(l)
