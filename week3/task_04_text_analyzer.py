text = input("Enter a paragraph: ").lower()

# Remove basic punctuation
for p in ".,!?;:'\"":
    text = text.replace(p, "")

words = text.split()

print("Words:", len(words))
print("Characters (no spaces):", len(text.replace(" ", "")))

vowels = 0
consonants = 0
for char in text:
    if char in "aeiou":
        vowels += 1
    elif char.isalpha():
        consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)

if words:
    longest = max(words, key=len)
    print("Longest word:", longest)

# Count word frequency
freq = {}
for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print("\nWord counts:")
for word in freq:
    print(word, ":", freq[word])

# Repeated words
print("\nRepeated words:")
for word in freq:
    if freq[word] > 1:
        print(word)

# Top 5 most frequent words
sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)
print("\nTop 5 most frequent words:")
for word, count in sorted_words[:5]:
    print(word, ":", count)