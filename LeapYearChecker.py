# Ask user for year
year = int(input("Enter a year: "))
# Check leap year condition
if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
    print("\nYear:", year)
    print("Leap Year ")
    print("Reason: Divisible by 4 and (not divisible by 100 OR divisible by 400).")
else:
    print("\nYear:", year)
    print("NOT a Leap Year ")
    if year % 4 != 0:
        print("Reason: Not divisible by 4.")
    elif year % 100 == 0 and year % 400 != 0:
        print("Reason: Divisible by 100 but NOT divisible by 400.")