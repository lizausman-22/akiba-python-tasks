class Dog:
    def make_sound(self):
        return "Woof!"

class Cat:
    def make_sound(self):
        return "Meow!"

class Cow:
    def make_sound(self):
        return "Moo!"

# Demonstrate polymorphism
animals = [Dog(), Cat(), Cow()]

for animal in animals:
    print(animal.make_sound())



from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

# Create objects and display areas
rect = Rectangle(5, 3)
circle = Circle(4)

print(f"Rectangle area: {rect.calculate_area()}")
print(f"Circle area: {circle.calculate_area():.2f}")