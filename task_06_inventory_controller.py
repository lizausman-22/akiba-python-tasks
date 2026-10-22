inventory = {}   # name: [price, stock]

while True:
    print("\n1. Add product")
    print("2. Search product")
    print("3. Update price")
    print("4. Increase stock")
    print("5. Sell product")
    print("6. Total value")
    print("7. Low stock report")
    print("8. Exit")

    choice = input("Choose (1-8): ")

    if choice == "1":
        name = input("Product name: ")
        if name == "" or name in inventory:
            print("Name empty or already exists")
        else:
            price = float(input("Price: "))
            stock = int(input("Stock: "))
            if price < 0 or stock < 0:
                print("Price and stock cannot be negative")
            else:
                inventory[name] = [price, stock]
                print("Product added")

    elif choice == "2":
        name = input("Product name: ")
        if name in inventory:
            print("Price:", inventory[name][0], "Stock:", inventory[name][1])
        else:
            print("Not found")

    elif choice == "3":
        name = input("Product name: ")
        if name not in inventory:
            print("Not found")
        else:
            new_price = float(input("New price: "))
            if new_price < 0:
                print("Price cannot be negative")
            else:
                inventory[name][0] = new_price
                print("Price updated")

    elif choice == "4":
        name = input("Product name: ")
        if name not in inventory:
            print("Not found")
        else:
            amount = int(input("Amount to add: "))
            if amount <= 0:
                print("Amount must be > 0")
            else:
                inventory[name][1] += amount
                print("Stock updated:", inventory[name][1])

    elif choice == "5":
        name = input("Product name: ")
        if name not in inventory:
            print("Not found")
        else:
            qty = int(input("Quantity to sell: "))
            if qty <= 0:
                print("Quantity must be > 0")
            elif qty > inventory[name][1]:
                print("Not enough stock")
            else:
                inventory[name][1] -= qty
                print("Sold. Remaining stock:", inventory[name][1])

    elif choice == "6":
        total = 0
        for name in inventory:
            total += inventory[name][0] * inventory[name][1]
        print("Total inventory value:", total)

    elif choice == "7":
        threshold = int(input("Low stock threshold (default 5): ") or 5)
        print("Low stock products:")
        found = False
        for name in inventory:
            if inventory[name][1] < threshold:
                print(name, "→", inventory[name][1], "units")
                found = True
        if not found:
            print("None")

    elif choice == "8":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")