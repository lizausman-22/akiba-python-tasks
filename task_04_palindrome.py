# Get a word from the user
word = input("Enter a word: ")

# Convert to lowercase so the check ignores uppercase/lowercase differences
cleaned_word = word.lower()

# Check if the word is the same forwards and backwards
if cleaned_word == cleaned_word[::-1]:
    print(f'"{word}" is a palindrome.')
else:
    print(f'"{word}" is not a palindrome.')