import random
best_score = None  # To track minimum attempts
while True:
    number = random.randint(1, 100)
    attempts = 7
    used_attempts = 0
    guessed = False
    print("\nNUMBER GUESSING GAME")
    print("I have selected a number between 1 and 100.")
    print("You have 7 attempts!")
    while attempts > 0:
        guess = int(input("\nEnter your guess: "))
        used_attempts += 1
        attempts -= 1
        if guess == number:
            print("Congratulations! You guessed it correctly!")
            print("Attempts used:", used_attempts)
            guessed = True
            # Update best score
            if best_score is None or used_attempts < best_score:
                best_score = used_attempts
                print(" New Best Score:", best_score)
            break
        elif guess > number:
            print("Too high!")
        else:
            print("Too low!")
        # Close hint (within 5)
        if abs(guess - number) <= 5 and guess != number:
            print(" Very close!")
        print("Attempts remaining:", attempts)
    if not guessed:
        print("\nYou failed! The correct number was:", number)
    # Play again option
    again = input("\nDo you want to play again? (yes/no): ").lower()
    if again != "yes":
        print("Thanks for playing!")
        break