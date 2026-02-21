# Ask how many numbers
count = int(input("How many numbers? "))
total = 0
# Take first number to initialize max and min
num = float(input("Enter number 1: "))
total += num
maximum = num
minimum = num
# Loop for remaining numbers
for i in range(2, count + 1):
    num = float(input(f"Enter number {i}: "))
    total += num
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num
# Calculate average
average = total / count
# Display results
print("\nResults:")
print("Sum:", total)
print("Average:", average)
print("Maximum:", maximum)
print("Minimum:", minimum)