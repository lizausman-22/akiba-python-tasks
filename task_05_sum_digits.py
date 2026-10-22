def sum_of_digits(n: int) -> int:
    """Return the sum of the digits of n using only arithmetic and a while loop."""
    if n < 0:
        n = -n                     # work with the absolute value

    total = 0
    while n > 0:
        total += n % 10            # extract the last digit
        n //= 10                   # remove the last digit
    return total


# Ask the user for a number
num = int(input("Enter a number: "))
print(f"Sum of digits of {num} is {sum_of_digits(num)}")