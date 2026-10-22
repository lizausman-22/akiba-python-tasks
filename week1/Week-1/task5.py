print("========================================")
print("                RECEIPT")
print("========================================")

customer_name = input("Customer name: ")
product_name = input("Product name: ")
price = float(input("Price: "))
quantity = int(input("Quantity: "))

total = price * quantity

print()
print(f"Customer: {customer_name}")
print()
print("Product        Price       Qty")
print("----------------------------------------")
print(f"{product_name:<15} {price:>7.0f} ETB    {quantity}")
print()
print(f"Total:         {total:,.0f} ETB")
print()
print("Thank you for shopping!")
print("========================================")