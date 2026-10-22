# Exam Result Report
# Collects student info and scores, calculates average, and displays a result..

# Ask for student information
name = input("Enter student name: ")
python_score = float(input("Enter Python score: "))
english_score = float(input("Enter English score: "))
math_score = float(input("Enter Mathematics score: "))

# Calculate the average
average = (python_score + english_score + math_score) / 3

# Display the result report
print("========================================")
print("          STUDENT RESULT")
print("========================================")
print()
print(f"Student: {name}")
print()
print(f"Python:       {python_score}")
print(f"English:      {english_score}")
print(f"Mathematics:  {math_score}")
print("----------------------------------------")
print(f"Average:      {average}")
print("========================================")