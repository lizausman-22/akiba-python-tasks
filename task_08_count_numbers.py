N = int(input("Enter a positive number: "))

even_count = 0
odd_count = 0
total_sum = 0

for i in range(1, N + 1):
    total_sum += i          # add every number to the sum

    if i % 2 == 0:
        even_count += 1     # even number
    else:
        odd_count += 1      # odd number

print(f"Even numbers: {even_count}")
print(f"Odd numbers: {odd_count}")
print(f"Sum of all numbers: {total_sum}")