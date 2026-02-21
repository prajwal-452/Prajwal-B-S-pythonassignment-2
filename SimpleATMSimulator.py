balance = 10000   # Initial balance

while True:
    print("\n=== ATM SIMULATOR ===")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = int(input("Enter choice: "))
    #Check Balance
    if choice == 1:
        print("Current Balance: Rs", balance)
    #Deposit Money
    elif choice == 2:
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            balance += amount
            print("Deposit successful!")
            print("New balance: Rs", balance)
        else:
            print("Invalid deposit amount!")
    #Withdraw Money
    elif choice == 3:
        amount = float(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Insufficient balance!")
        elif balance - amount < 500:
            print("Minimum balance of Rs500 must remain!")
        elif amount <= 0:
            print("Invalid withdrawal amount!")
        else:
            balance -= amount
            print("Withdrawal successful!")
            print("New balance: Rs", balance)
    # Exit
    elif choice == 4:
        print("Thank you for using ATM ")
        break
    else:
        print("Invalid choice! Please select 1-4.")