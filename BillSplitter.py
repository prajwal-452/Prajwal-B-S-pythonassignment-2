# Taking inputs
bill = float(input("Enter total bill: "))
people = int(input("Number of people: "))
tax_percent = float(input("Tax percentage: "))
tip_percent = float(input("Tip percentage: "))
# Calculations
tax_amount = bill * tax_percent / 100
after_tax = bill + tax_amount
tip_amount = after_tax * tip_percent / 100
total_bill = after_tax + tip_amount
per_person = total_bill / people
# Display output
print("\n=== BILL BREAKDOWN ===")
print("Subtotal:     Rs{:.2f}".format(bill))
print("Tax ({}%):    Rs{:.2f}".format(tax_percent, tax_amount))
print("After tax:    Rs{:.2f}".format(after_tax))
print("Tip ({}%):    Rs{:.2f}".format(tip_percent, tip_amount))
print("Total:        Rs{:.2f}".format(total_bill))
print("Per person:   Rs{:.2f}".format(per_person))