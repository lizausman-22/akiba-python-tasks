print("==============================")
print("      CURRENCY EXCHANGE")
print("==============================")

exchange_rate = float(input("Exchange Rate (1 USD = ? ETB): "))
usd_amount = float(input("USD Amount: "))

etb_amount = usd_amount * exchange_rate

print()
print(f"Exchange Rate: 1 USD = {exchange_rate:g} ETB")
print()
print(f"ETB Amount: {etb_amount:,.0f} ETB")

print("==============================")