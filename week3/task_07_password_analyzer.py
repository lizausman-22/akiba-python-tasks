def analyze_password(password, min_length=8):
    report = {
        "length_ok": len(password) >= min_length,
        "has_upper": any(c.isupper() for c in password),
        "has_lower": any(c.islower() for c in password),
        "has_digit": any(c.isdigit() for c in password),
        "has_special": any(c in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~" for c in password),
        "missing": []
    }

    if not report["length_ok"]:
        report["missing"].append(f"Minimum {min_length} characters")
    if not report["has_upper"]:
        report["missing"].append("Uppercase letter")
    if not report["has_lower"]:
        report["missing"].append("Lowercase letter")
    if not report["has_digit"]:
        report["missing"].append("Digit")
    if not report["has_special"]:
        report["missing"].append("Special character")

    report["is_strong"] = len(report["missing"]) == 0
    return report

# Test 5 fictional passwords
print("=== Testing 5 passwords ===")
tests = ["abc", "Password", "password123", "Pass123!", "SHORT1!"]

for pwd in tests:
    r = analyze_password(pwd)
    print(f"\nPassword: {pwd}")
    print("Strong:", r["is_strong"])
    if r["missing"]:
        print("Missing:", ", ".join(r["missing"]))
    else:
        print("All requirements passed")

# User input
print("\n=== Check your password ===")
password = input("Enter password: ")
min_len = int(input("Minimum length (default 8): ") or 8)

result = analyze_password(password, min_len)

print("\nResults:")
print("Length OK     :", result["length_ok"])
print("Has Uppercase :", result["has_upper"])
print("Has Lowercase :", result["has_lower"])
print("Has Digit     :", result["has_digit"])
print("Has Special   :", result["has_special"])
print("Strong        :", result["is_strong"])

if result["missing"]:
    print("Missing:", ", ".join(result["missing"]))
else:
    print("All requirements passed!")