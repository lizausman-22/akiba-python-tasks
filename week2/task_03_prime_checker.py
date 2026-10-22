# Ask the user for a number
number = int(input("Enter a number: "))

# Handle special cases first
if number <= 1:
    print(f"{number} is not a prime number.")
else:
    is_prime = True

    # We only need to check divisors up to the square root of the number.
    # Reason: If a number n has a divisor larger than √n,
    # then it must also have a corresponding divisor smaller than √n.
    # So checking beyond √n is unnecessary and inefficient.
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break   # No need to continue once we find a divisor

    if is_prime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")