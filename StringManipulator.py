# Asking user for a sentence
sentence = input("Enter a sentence: ")
# Original sentence
print("\nOriginal sentence:",sentence)
#Total characters (with spaces)
print("\nTotal characters (with spaces):",len(sentence))
#Total characters (without spaces)
print("\nTotal characters (without spaces):",len(sentence.replace(" ", "")))
#Total words
words = sentence.split()
print("\nTotal words:",len(words))
#UPPERCASE
print("\nUPPERCASE:",sentence.upper())
#lowercase
print("\nlowercase:",sentence.lower())
#Title Case
print("\nTitle Case:",sentence.title())
#First word
print("\nFirst word:")
if len(words) > 0:
    print(words[0])
else:
    print("No words found")
#Last word
print("\nLast word:")
if len(words) > 0:
    print(words[-1])
else:
    print("No words found")
#Reversed sentence
print("\nReversed sentence:",sentence[::-1])