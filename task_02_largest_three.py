# Get three numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Compare the numbers using conditions
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

# Handle equal cases
if num1 == num2 == num3:
    print("All three numbers are equal.")
elif (num1 == num2 == largest) or (num1 == num3 == largest) or (num2 == num3 == largest):
    print(f"The largest number is {largest} (two numbers are equal).")
else:
    print(f"The largest number is {largest}.")