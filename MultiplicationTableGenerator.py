# Asking user for input
number = int(input("Enter number: "))
range_end = int(input("Enter range (end): "))
print("\nMultiplication Table of", number)
# Loop to generate table
for i in range(1, range_end + 1):
    print(number, "x", i, "=", number * i)