# Count Words
def count_words(text):
    words = text.split()
    return len(words)
# Count Vowels
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count
# Count Consonants
def count_consonants(text):
    count = 0
    for char in text:
        if char.isalpha() and char.lower() not in "aeiou":
            count += 1
    return count
# Reverse Text
def reverse_text(text):
    return text[::-1]
# Check Palindrome
def is_palindrome(text):
    clean = text.lower().replace(" ", "")
    return clean == clean[::-1]
# Remove Vowels
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    result = ""
    for char in text:
        if char not in vowels:
            result += char
    return result
# Word Frequency
def word_frequency(text):
    words = text.lower().split()
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq
# Longest Word
def longest_word(text):
    words = text.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest
# Analyze Text
def analyze_text(text):
    print("\n=== TEXT ANALYSIS ===")
    print("Words:", count_words(text))
    print("Vowels:", count_vowels(text))
    print("Consonants:", count_consonants(text))
    print("Reversed:", reverse_text(text))
    print("Palindrome:", "Yes" if is_palindrome(text) else "No")
    print("Without vowels:", remove_vowels(text))
    lw = longest_word(text)
    print("Longest word:", lw, f"({len(lw)} letters)")
    freq = word_frequency(text)
    print("Word Frequency:", end=" ")
    for word, count in freq.items():
        print(f"{word}: {count}", end=", ")
    print()
text = input("Enter text: ")
analyze_text(text)