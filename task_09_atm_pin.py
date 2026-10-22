pin = "1234"
attempts = 0

while attempts < 3:
    user_pin = input("Enter PIN: ")
    attempts += 1

    if user_pin == pin:
        print("Access granted!")
        break
    else:
        print("Incorrect PIN.")
        print(f"Attempts remaining: {3 - attempts}")
else:
    print("Card blocked.")