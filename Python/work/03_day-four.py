# Basic Math operations

addition = "+"
subtraction = "-"
multiplication = "*"
division = "/"
exponentiation = "**"
modulus = "%"
floor_division = "//"

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
operation = input(f"Choose an operation {addition}, {subtraction}, {multiplication}, {division}, {exponentiation}, {modulus}, {floor_division}: ")

if operation == addition:
    result = number1 + number2
elif operation == subtraction:
    result = number1 - number2
elif operation == multiplication:
    result = number1 * number2
elif operation == division:
    result = number1 / number2
elif operation == exponentiation:
    result = number1 ** number2
elif operation == modulus:
    result = number1 % number2
elif operation == floor_division:
    result = number1 // number2

print(f"The result of {number1} {operation} {number2} is: {result}")