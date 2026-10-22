print("========================================")
print("            EMPLOYEE PAYSLIP")
print("========================================")

employee_name = input("Employee name: ")
basic_salary = float(input("Basic salary: "))
transport_allowance = float(input("Transport allowance: "))
food_allowance = float(input("Food allowance: "))

gross_salary = basic_salary + transport_allowance + food_allowance

print()
print(f"Employee: {employee_name}")
print()
print(f"Basic Salary:          {basic_salary:,.0f} ETB")
print(f"Transport Allowance:   {transport_allowance:,.0f} ETB")
print(f"Food Allowance:        {food_allowance:,.0f} ETB")
print("----------------------------------------")
print(f"Gross Salary:          {gross_salary:,.0f} ETB")
print("========================================")