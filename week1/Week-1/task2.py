# TASK 2 — Student ID Card

student_name = input("Enter your name: ")
student_id = input("Enter your student ID: ")
department = input("Enter your department: ")
year = int(input("Enter your year: "))
university = input("Enter your university: ")
phone = input("Enter your phone number: ")

print("\n+--------------------------------+")
print("|       AKIBA STUDENT CARD      |")
print("+--------------------------------+")
print(f"| Name: {student_name:<25}|")
print(f"| ID: {student_id:<27}|")
print(f"| Department: {department:<18}|")
print(f"| Year: {year:<25}|")
print(f"| University: {university:<18}|")
print(f"| Phone: {phone:<23}|")
print("+--------------------------------+")
