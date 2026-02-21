# Ask user for birth year
birth_year = int(input("Enter your birth year: "))
# Ask user for current year
current_year = int(input("Enter current year: "))
# Calculate age
age = current_year - birth_year
# Calculate other values
months = age * 12
days = age * 365
hours = days * 24
minutes = hours * 60
years_to_100 = 100 - age
# Display results
print("\nYour Age Details:")
print("Current Age:", age, "years")
print("Age in Months:", months)
print("Age in Days (approx):", days)
print("Age in Hours:", hours)
print("Age in Minutes:", minutes)
print("Years until 100:", years_to_100)