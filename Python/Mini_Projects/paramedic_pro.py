def check_age(age):
    if age >= 20:
        return("✅ Access granted")
    else:
        return("❌ Access denied")

def simple_calculator(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a / b
    elif operator == "//":
        return a // b
    elif operator == "**":
        return a ** b
    elif operator == "%":
        return a % b
    else:
        return("Error! Use Valid operator")

def area_calculator(length, width):
    return length * width


# Call the function
try:

    while True:
        print("=" * 40)
        print("🚑 Welcome to Paramedic Prep-Pro Utility app.")
        print("=" * 40)
        print("1. Login Check")
        print("2. Simple Calculator")
        print("3. Area Calculator")
        print("4. Exit")
        choice = input("Choose an option (1-4)")
        # Choice 1
        if choice == "1":
            print("🚑 Login Check.")
            user_age = input("Enter your age or 'exit' to quit: ")
            age = int(user_age)
            print(check_age(age))
        elif choice == "2":
            print("🚑 Prep-pro Simple Calculator")
            operation = input("Enter operation (+, -, *, /, //, **, %): ")
            number_one = float(input("Enter the first number: "))
            number_two = float(input("Enter the second number: "))
            result = simple_calculator(number_one, number_two, operation)
            print(f"The result of {number_one} {operation} {number_two} is {result}")

        elif choice == "3":
            print("🚑 Area Calculator")
            user_length = float(input("Insert the Length: "))
            user_width = float(input("Insert the Width: "))
            print(f"The result is {area_calculator(user_length, user_width)} cm2")

        elif choice == "4":
            print("👋 Exiting Program... Goodbye!")
            break

        else:
            print("⚠️ Invalid choice, please try again.")
except Exception as e:
    print(f"⚠️ Error: {e}.")