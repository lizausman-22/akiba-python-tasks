class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Product: {self.name} | Price: {self.price} birr | Quantity: {self.quantity}"

    def total_value(self):
        return self.price * self.quantity

product1 = Product("pen", 120, 15)
product2 = Product("pencil", 100, 10)
product3 = Product("paper", 45, 30)

print("\n=== Product Information System ===\n")

print(product1)
print(product2)
print(product3)

print("\n--- Total Values ---")
print(f"{product1.name} total value: {product1.total_value()} birr")
print(f"{product2.name} total value: {product2.total_value()} birr")
print(f"{product3.name} total value: {product3.total_value()} birr")

#The __str__() method defines how an object should be displayed as a readable string when you use print() on it.