# Simple Expense Tracker with Functions

expenses = []

def add_expense(description, category, amount):
    expenses.append({"description": description, "category": category, "amount": amount})
    print("Expense added!")


def total_expenses():
    total = 0
    for e in expenses:
        total = total + e["amount"]
    return total


def spending_by_category():
    categories = {}
    for e in expenses:
        cat = e["category"]
        if cat in categories:
            categories[cat] = categories[cat] + e["amount"]
        else:
            categories[cat] = e["amount"]
    return categories


def largest_expense():
    biggest = expenses[0]
    for e in expenses:
        if e["amount"] > biggest["amount"]:
            biggest = e
    return biggest


def expenses_above(threshold):
    result = []
    for e in expenses:
        if e["amount"] > threshold:
            result.append(e)
    return result


def spending_report():
    if len(expenses) == 0:
        print("No expenses yet.")
        return

    total = total_expenses()
    categories = spending_by_category()
    biggest = largest_expense()

    print("\n----- SPENDING REPORT -----")
    print("Total spent:", total)

    print("\nBy category:")
    highest_cat = ""
    highest_amount = 0
    for cat in categories:
        amount = categories[cat]
        percent = (amount / total) * 100
        print(cat, ":", amount, "(", round(percent, 1), "%)")
        if amount > highest_amount:
            highest_amount = amount
            highest_cat = cat

    print("\nHighest category:", highest_cat)
    print("Largest expense :", biggest["description"], "-", biggest["amount"])
    print("---------------------------")


# Main program
while True:
    print("\n1. Add expense")
    print("2. Show report")
    print("3. Show expenses above amount")
    print("4. Exit")
    choice = input("Choose: ")

    if choice == "1":
        desc = input("Description: ")
        cat = input("Category: ")
        amount = float(input("Amount: "))
        add_expense(desc, cat, amount)

    elif choice == "2":
        spending_report()

    elif choice == "3":
        limit = float(input("Show expenses above: "))
        found = expenses_above(limit)
        if len(found) == 0:
            print("None found.")
        else:
            for e in found:
                print(e["description"], "-", e["amount"])

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")