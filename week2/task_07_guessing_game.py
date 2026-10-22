import random

secret = random.randint(1, 100)
attempts = 0

print("Guess the number between 1 and 100. You have 5 tries.")

while attempts < 5:
    guess = int(input("Your guess: "))
    attempts += 1

    if guess == secret:
        print(f"Congratulations! You guessed it in {attempts} attempts.")
        break
    elif guess < secret:
        print("Too low!")
    else:
        print("Too high!")
else:
    print(f"Game Over! The number was {secret}.")