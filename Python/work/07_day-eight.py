# TASK
# Create a program that:
# 1. Asks the user to enter a number
# 2. Prints whether the number is positive, Negative, or zero
# 3. Prints whether the number is even or odd
try:
    number = float(input("Enter a single number: "))

    if number >= 9:
        print("Select a Lesser Number")
    elif number == 0:
        print(f"{number}, is Zero")
    elif number < 0:
        print(f"{number}, is a Negative")
    elif number > 0:
        print(f"{number}, is a Positive")
    
    result = number % 2
    if result == 0:
        print("The Number is Even")
    else:
        print("The Number is Odd")
except ValueError:
    print("Error! Use a valid Number")