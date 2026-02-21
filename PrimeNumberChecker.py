# Part 1: Check Single Number
num = int(input("Enter a number: "))
if num <= 1:
    print(num, "is NOT a prime number")
elif num == 2:
    print("2 is a PRIME number")
else:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, "is a PRIME number")
    else:
        print(num, "is NOT a prime number")
# Part 2: Prime Numbers in Range
start = int(input("\nEnter start range: "))
end = int(input("Enter end range: "))
print("Prime numbers:\n", end=" ")
for n in range(start, end + 1):
    if n > 1:
        is_prime = True
        for i in range(2, n):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            print(n, end=" ") 