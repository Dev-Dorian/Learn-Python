def get_product(**data):
    print(data)
    print(data["id"], data["name"])


get_product(id="23", name="iPhone", desc="This is a iphone")
