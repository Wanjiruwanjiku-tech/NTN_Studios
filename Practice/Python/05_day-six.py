# Handling errors and type conversion

# Error Handling
try:
    # Type conversion
    number = int(input("Enter the number to double: "))
    result = number * 2

    print(f"The double of {number} is {result}")
except ValueError:
    print("Invalid input. Please enter a number.")