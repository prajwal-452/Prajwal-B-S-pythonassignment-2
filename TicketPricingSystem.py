# Taking inputs
age = int(input("Enter age: "))
day = input("Enter day of the week: ").strip().lower()
tickets = int(input("Enter number of tickets: "))
# Age-based pricing
if age < 3:
    base_price = 0
    category = "Free"
elif 3 <= age <= 12:
    base_price = 150
    category = "Child"
elif 13 <= age <= 59:
    base_price = 300
    category = "Adult"
else:
    base_price = 200
    category = "Senior"
# Calculate total base amount
total_base = base_price * tickets
# Day-based discount
if day in ["friday", "saturday", "sunday"]:
    discount = total_base * 0.20
else:
    discount = 0
# Final amount
final_amount = total_base - discount
# Display result
print("\n   MOVIE TICKET BILL   ")
print("Category:", category)
print("Base price per ticket: Rs", base_price)
print("Total base amount: Rs", total_base)
print("Discount: Rs", discount)
print("Final amount to pay: Rs", final_amount)