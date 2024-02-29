def hello(name, lastname="Cook"):
    print("Hello World!")
    print(f"Welcome {name} {lastname}")


hello("Dorian", "Hidalgo")
hello("Michael")

hello(lastname="Park", name="Caroline")
