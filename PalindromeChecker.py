# Takeing input from the users
text = input("Enter word/number: ")
# Convert to lowercase for checking
lower_text = text.lower()
# Reverse the text
reversed_text = lower_text[::-1]
print("\nOriginal:", text)
print("Reversed:", reversed_text)
# Check for palindrome
if lower_text == reversed_text:
    print("Result: PALINDROME ")
else:
    print("Result: NOT A PALINDROME ")