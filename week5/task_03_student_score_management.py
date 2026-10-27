class Student:

    school_name = "Akiba Academy"

    def __init__(self, name, score, department):
        
        self.name = name
        self.score = score
        self.department = department

    def display(self):
        print(f"School: {Student.school_name}")
        print(f"Name: {self.name}")
        print(f"Score: {self.score}")
        print(f"Department: {self.department}")


student1 = Student("Amina Hassan", 85, "Computer Science")
student2 = Student("Brian Otieno", 72, "Business")
student3 = Student("Fatuma Ali", 91, "Engineering")

print("\n=== Student Score Management ===\n")

print("Student 1:")
student1.display()


print("\nStudent 2:")
student2.display()

print("\nStudent 3:")
student3.display()

print("\nUpdating score of Student 2 (Brian Otieno)...")
student2.score = 88

print("\nUpdated Student 2:")
student2.display()



print("\n=== Verifying Independent Scores ===")
print(f"{student1.name}'s score: {student1.score}")
print(f"{student2.name}'s score: {student2.score}")
print(f"{student3.name}'s score: {student3.score}")
