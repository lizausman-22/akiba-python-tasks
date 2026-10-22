balance = float(input("Enter opening balance: "))
transactions = []
total_deposited = 0
total_withdrawn = 0
daily_limit = 1000
daily_withdrawn = 0

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Show Summary")
    print("5. Exit")

    choice = input("Choose (1-5): ")

    if choice == "1":
        amount = float(input("Amount to deposit: "))
        if amount <= 0:
            print("Amount must be greater than 0")
        else:
            balance += amount
            total_deposited += amount
            transactions.append({"type": "deposit", "amount": amount, "balance_after": balance})
            print("Deposited. New balance:", balance)

    elif choice == "2":
        amount = float(input("Amount to withdraw: "))
        if amount <= 0:
            print("Amount must be greater than 0")
        elif amount > balance:
            print("Not enough balance")
        elif daily_withdrawn + amount > daily_limit:
            print("Daily limit exceeded. Remaining:", daily_limit - daily_withdrawn)
        else:
            balance -= amount
            total_withdrawn += amount
            daily_withdrawn += amount
            transactions.append({"type": "withdraw", "amount": amount, "balance_after": balance})
            print("Withdrawn. New balance:", balance)

    elif choice == "3":
        print("Current balance:", balance)

    elif choice == "4":
        print("\n--- Summary ---")
        print("Total deposited :", total_deposited)
        print("Total withdrawn :", total_withdrawn)
        print("Final balance   :", balance)
        print("Transactions:")
        for t in transactions:
            print(t)

    elif choice == "5":
        print("Final balance:", balance)
        print("Goodbye!")
        break

    else:
        print("Invalid choice")