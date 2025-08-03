# Mini Project six: Basic Chatbot that performs Mathematical calculations
# Requrements.
# 1. Prompts user to enter their name.
# 2. Prompts user to enter the type of calculation to perform
# 3. Promts the user to enter two numbers to work with
# 4. Prints the result.

def math_chatbot(num1, num2, operation):

    try:
        num1 = float(num1)
        num2 = float(num2)

        if operation == "+":
            return (num1 + num2)
        elif  operation == "-":
            return num1 - num2
        elif  operation == "/":
            return num1 / num2
        elif  operation == "//":
            return num1 // num2
        elif  operation == "*" :
            return num1 * num2
        elif  operation == "%":
            return num1 % num2
        elif  operation == "**":
            return num1 ** num2
        else:
            return "⚠️  Invalid operation."

    except TypeError:
        print("⚠️  Error! Enter a valid Number.")
    except ValueError:
        return "⚠️  Please enter valid numbers."
    except ZeroDivisionError:
        return "⚠️  Cannot divide by zero."
    
# The Interface
if __name__ == "__main__":
    print("🤖: Welcome to the Mathematical Chatbot")
    name = input("🤖: What is your Name?\n")
    name = name.strip().capitalize()
    print(f"🤖: Hello {name}! I can perform the following operations:")
    print("""
        ➕  Addition (+)
        ➖  Subtraction (-)
        ✖️  Multiplication (*)
        ➗  Division (/)
        🔢  Floor Division (//)
        🧮  Modulus (%)
        🔺  Power (**)
    """)
    
    while True:
        print("\nType 'exit' anytime to leave.")

        number1 = input(f"🤖: {name}, enter the first number: ")
        if number1.lower() == "exit":
            break

        number2 = input(f"🤖: {name}, enter the second number: ")
        if number2.lower() == "exit":
            break

        operation = input(f"🤖: {name}, enter the operation (+, -, *, /, //, %, **): ")
        if operation.lower() == "exit":
            break
       
        response = math_chatbot(number1, number2, operation)
        print(f"🤖:{response}")
    print(f"\n🤖: Goodbye, {name}! Thanks for using the chatbot. 👋")