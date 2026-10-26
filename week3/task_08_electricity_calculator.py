def validate_units(units):
    if units< 0:
        return False
    return True
def calculate_tier_charge(units):
    if units <= 50:
        t1 = units*0.5
        t2 = 0
        t3 = 0
    elif units <= 150:
        t1 = 50*0.5
        t2 = (units-50)*0.75
        t3 = 0
    else:
        t1=50*0.5
        t2=100*0.75
        t3=(units-150)*1.2
    return t1, t2, t3
def calculate_total_bill(units, service_fee=0.0):
    if not validate_units(units):
        return 0
    t1, t2, t3=calculate_tier_charge(units)
    total = t1+t2+t3+service_fee
    return total
def generate_bill_summary(units, service_fee=0.0):
    if not validate_units(units):
        return
    t1, t2, t3=calculate_tier_charge(units)
    total = calculate_total_bill(units, service_fee)
    print("\n-----Electricity Bill------")
    print("Units used: ", units)
    print("First 50 units: ", t1, "Birr")
    print("next 100 units: ", t2, "Birr")
    print("above 150 units: ", t3, "Birr")
    if service_fee >0:
        print("Service fee: ", service_fee, "Birr")
    print("Total Bill = ", total, "Birr" )
    print("-------------------------------")
units=float(input("Enter the amount of units used: "))
fee=float(input("Enter service fee(or 0): "))
generate_bill_summary(units,fee)