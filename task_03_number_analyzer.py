def is_prime(number):
    if number <= 1:
        return False
    i = 2
    while i * i <= number:
        if number % i == 0:
            return False
        i += 1
    return True

def get_divisors(number):
    number = abs(number)
    if number == 0:
        return []  # Every non-zero number divides 0; return empty for simplicity
    divisors = []
    i = 1
    while i <= number:
        if number % i == 0:
            divisors.append(i)
        i += 1
    return divisors

def sum_of_digits(number):
    number = abs(number)
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    return total

def reverse_number(number):
    sign = -1 if number < 0 else 1
    number = abs(number)
    reversed_num = 0
    while number > 0:
        reversed_num = reversed_num * 10 + number % 10
        number //= 10
    return sign * reversed_num

def analyze_number(number):
    print(f"\n--- Analysis of {number} ---")
    
    # Even or odd
    if number % 2 == 0:
        print("Even or Odd: Even")
    else:
        print("Even or Odd: Odd")
    
    # Prime (only positive numbers > 1 can be prime)
    if number > 1 and is_prime(number):
        print("Prime: Yes")
    else:
        print("Prime: No")
    
    # Sum of digits
    print(f"Sum of digits: {sum_of_digits(number)}")
    
    # Reversed
    print(f"Reversed: {reverse_number(number)}")
    
    # Divisors
    print(f"Divisors: {get_divisors(number)}")

# Handle user input
while True:
    try:
        num = int(input("Enter a number (or type 'q' to quit): "))
        analyze_number(num)
    except ValueError:
        choice = input("Invalid input. Type 'q' to quit or press Enter to try again: ")
        if choice.lower() == "q":
            break