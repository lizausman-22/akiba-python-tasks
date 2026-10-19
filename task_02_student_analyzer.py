def validate_score(score):
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100")
    return score

def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def calculate_average(students):
    total = 0
    count = 0
    for s in students:
        total += s["score"]
        count += 1
    return total / count if count > 0 else 0

def find_highest(students):
    highest = students[0]
    for s in students:
        if s["score"] > highest["score"]:
            highest = s
    return highest

def find_lowest(students):
    lowest = students[0]
    for s in students:
        if s["score"] < lowest["score"]:
            lowest = s
    return lowest

def count_pass_fail(students):
    passed = 0
    failed = 0
    for s in students:
        if s["score"] >= 50:
            passed += 1
        else:
            failed += 1
    return passed, failed

def above_average(students):
    avg = calculate_average(students)
    result = []
    for s in students:
        if s["score"] > avg:
            result.append(s)
    return result

def generate_report(students):
    avg = calculate_average(students)
    highest = find_highest(students)
    lowest = find_lowest(students)
    passed, failed = count_pass_fail(students)
    top = above_average(students)

    print("\n--- CLASS REPORT ---")
    for s in students:
        print(f"{s['name']}: {s['score']} ({calculate_grade(s['score'])})")
    print(f"Average: {avg:.2f}")
    print(f"Highest: {highest['name']} ({highest['score']})")
    print(f"Lowest: {lowest['name']} ({lowest['score']})")
    print(f"Passed: {passed} | Failed: {failed}")
    print("Above average:")
    for s in top:
        print(f"  {s['name']} ({s['score']})")

students = []
print("Enter students (type 'done' to finish)")
while True:
    name = input("Name: ")
    if name.lower() == "done":
        break
    score = float(input("Score: "))
    validate_score(score)
    students.append({"name": name, "score": score})

if students:
    generate_report(students)
else:
    print("No students entered.")