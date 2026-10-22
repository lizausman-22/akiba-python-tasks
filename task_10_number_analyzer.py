largest = None
smallest = None
total = 0
even = 0
odd = 0

print("Enter 10 numbers:")

for i in range(10):
    num = float(input(f"Number {i+1}: "))

    # Track largest and smallest
    if largest is None or num > largest:
        largest = num
    if smallest is None or num < smallest:
        smallest = num

    # Add to total
    total += num

    # Count even / odd
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

average = total / 10

print("\nResults:")
print("Largest:", largest)
print("Smallest:", smallest)
print("Sum:", total)
print("Average:", average)
print("Even numbers:", even)
print("Odd numbers:", odd)