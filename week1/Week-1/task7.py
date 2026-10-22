print("========================================")
print("            TRAVEL PLANNER")
print("========================================")

destination = input("Destination: ")
distance = float(input("Distance in kilometers: "))
speed = float(input("Average speed in km/h: "))

travel_time = distance / speed

hours = int(travel_time)
minutes = int((travel_time - hours) * 60)

print()
print(f"Destination: {destination}")
print(f"Distance: {distance:g} km")
print(f"Average Speed: {speed:g} km/h")
print()
print(f"Estimated Travel Time: {hours} hours and {minutes} minutes")

print("========================================")