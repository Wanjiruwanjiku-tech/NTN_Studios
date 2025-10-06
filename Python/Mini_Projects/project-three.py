# Mini Project 3: Word Analyzer (Analyze a user's favorite word)
# Requirements
# 1. Ask for a word
# 2. print =>
#       - Its length
#       - The word in uppercase
#       - The first and last letters
#       - Whether it contains the letter "e"

try:
    print("Word Analyzer")
    word = str(input("Enter your favorite word: "))
    word_length = len(word)
    word_uppercase = word.upper()
    first_letter = word[0]
    last_letter = word[-1]
    
    print(f"Breakdown:")
    print(f"\tLength: {word_length} letters")
    print(f"\tUppercase: {word_uppercase}")
    print(f"\t First Letter: {first_letter}")
    print(f"\t Last Letter: {last_letter}")

    letter = "e"
    if letter in word:
        print(f"Letter {letter} is found in the word '{word.capitalize()}'\n")
    else:
        print(f"Letter {letter} is not found in the word '{word.capitalize()}'\n")

except ValueError:
    print("Invalid Input, Use letters")