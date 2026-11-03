class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)          # initialize parent attributes
        self.department = department

    def display_info(self):                     # method overriding
        super().display_info()                  # optionally reuse parent behavior
        print(f"Department: {self.department}")
        print("Role: Manager")


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)          # initialize parent attributes
        self.programming_language = programming_language

    def display_info(self):                     # method overriding
        super().display_info()                  # optionally reuse parent behavior
        print(f"Programming Language: {self.programming_language}")
        print("Role: Developer")


# Create objects
emp = Employee("liza", 50000)
mgr = Manager("mastewal", 80000, "Sales")
dev = Developer("dawit", 70000, "Python")

# Call display_info() for each
print("=== Employee ===")
emp.display_info()

print("\n=== Manager ===")
mgr.display_info()

print("\n=== Developer ===")
dev.display_info()

#Inheritance is an OOP mechanism that allows a new class (child/subclass) to acquire the attributes and methods of an existing class (parent/superclass).
#Parent class (base/superclass): The class that is inherited from. It defines common attributes and behavior.
#Child class (derived/subclass): The class that inherits from the parent. It can add new attributes/methods or override existing ones, while still having access to everything defined in the parent (unless restricted).
#Method overriding occurs when a child class defines a method with the same name and signature as a method in its parent class.
#super() returns a temporary object of the parent class, allowing the child class to call the parent’s methods (most commonly __init__ or other overridden methods).
#Single inheritance: A class inherits from only one parent class
#Multiple inheritance: A class inherits from two or more parent classes at the same time