class Student:
    def __init__(self, name, student_id, department):
        self.name = name
        self.student_id = student_id
        self.department = department

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"Department: {self.department}")

    def introduce(self):
        print(f"Hello! My name is {self.name}. I am a student in the {self.department} department with ID {self.student_id}.")

student1 = Student("liza usman", "1234", "software engineering")
student2 = Student("mastewal getu", "5678", "computer science")
student3 = Student("dawit abebe", "8901", "electrical engineering")

print("Student Information:")
student1.display_info()
student2.display_info()
student3.display_info()

print("\nStudent Introductions")
student1.introduce()
student2.introduce()
student3.introduce()