# TASK 4 — Temperature Station

print("=== TEMPERATURE STATION ===")
print("Convert Celsius ↔ Fahrenheit\n")

# Ask the user for temperature in Celsius
celsius = float(input("Enter temperature in Celsius: "))

# Convert Celsius → Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Display both temperatures
print("\n========== RESULTS ==========")
print(f"Celsius    : {celsius}°C")
print(f"Fahrenheit : {fahrenheit}°F")
print("=============================")

# ========== BONUS ==========
print("\n---  Fahrenheit → Celsius ---")
fahrenheit_input = float(input("Enter temperature in Fahrenheit: "))

# Convert Fahrenheit → Celsius
celsius_from_f = (fahrenheit_input - 32) * 5/9

print(f"\nFahrenheit : {fahrenheit_input}°F")
print(f"Celsius    : {celsius_from_f}°C")