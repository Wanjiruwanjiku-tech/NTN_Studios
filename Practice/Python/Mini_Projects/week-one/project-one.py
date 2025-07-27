# Mini Project 1: Age in days calculator
# Requirements
# 1. Ask the user for their name and age in years
# 2. Calculate how many days they have been alive i.e age * 365
# 3. Print the result using an f string
try:
    print("Welcome, Get to know your age in days\n")
    name = input("Enter your name: ")
    age = int(input(f"Hello {name}, Enter your age in years: "))

    result = age * 365
    print (f"\n{name.upper()}, your age in is {result} days")

except ValueError:
    print(f"Invalid input {name}, ensure to use valid numbers.")