list1 = [1, 2, 3, 4]
print(list1)
print(*list1)

list2 = [5, 6]

combined = ["Hello", *list1, "mundo", *list2, "little pig"]
print(combined)

point1 = {"x": 19}
point2 = {"y": 15}

newPoint = {**point1, "lala": "hello world", **point2, "z": "world"}
print(newPoint)
