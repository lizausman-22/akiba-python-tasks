def calculate_subtotal(items):
    subtotal = 0
    for item in items:
        if item["price"] < 0 or item["quantity"] < 0:
            raise ValueError("Price and quantity cannot be negative")
        subtotal += item["price"] * item["quantity"]
    return subtotal

def calculate_discount(subtotal):
    if subtotal < 1000:
        return 0
    elif subtotal < 3000:
        return subtotal * 0.05
    else:
        return subtotal * 0.10

def calculate_tax(amount, tax_rate):
    if tax_rate < 0 or tax_rate > 100:
        raise ValueError("Invalid tax rate")
    return amount * tax_rate / 100

def generate_receipt(items, tax_rate):
    subtotal = calculate_subtotal(items)
    discount = calculate_discount(subtotal)
    tax = calculate_tax(subtotal - discount, tax_rate)
    final = subtotal - discount + tax

    print("\n--- RECEIPT ---")
    for item in items:
        print(f"{item['name']}: {item['quantity']} x {item['price']} = {item['price'] * item['quantity']}")
    print(f"Subtotal: {subtotal:.2f}")
    print(f"Discount: {discount:.2f}")
    print(f"Tax: {tax:.2f}")
    print(f"Final: {final:.2f}")

items = []
print("Enter products (type 'done' to finish)")
while True:
    name = input("Name: ")
    if name.lower() == "done":
        break
    price = float(input("Price: "))
    quantity = float(input("Quantity: "))
    items.append({"name": name, "price": price, "quantity": quantity})

tax_rate = float(input("Tax rate (%): "))
generate_receipt(items, tax_rate)