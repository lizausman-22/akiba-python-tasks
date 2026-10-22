print("================================")
print("          BMI REPORT")
print("================================")

name = input("Name: ")
weight = float(input("Weight in kilograms: "))
height = float(input("Height in meters: "))

bmi = weight / (height * height)

print()
print(f"Name: {name}")
print(f"Weight: {weight:g} kg")
print(f"Height: {height:.2f} m")
print()
print(f"BMI: {bmi:.2f}")

print("================================")