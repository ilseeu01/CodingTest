class Product:
    def __init__(self, name="codetree", code=50):
        self.name = name
        self.code = code

product = [Product() for _ in range(2)]
name, code = input().split()
code = int(code)
product[1].name = name
product[1].code = code

product1 = product[0]
product2 = product[1]
print(f"product {product1.code} is {product1.name}")
print(f"product {product2.code} is {product2.name}")