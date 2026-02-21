# Ask user for number
num = int(input("Enter a number: "))
# Handle negative numbers
if num < 0:
    print("Factorial is not defined for negative numbers.")
# Handle 0
elif num == 0:
    print("0! = 1")
else:
    factorial = 1
    steps = ""
    # Calculate factorial using loop
    for i in range(num, 0, -1):
        factorial *= i
        steps += str(i)
        if i != 1:
            steps += " × "
    # Display result
    print(f"\n{num}! = {steps} = {factorial}")