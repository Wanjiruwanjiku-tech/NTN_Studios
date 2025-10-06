# Project: BMI Calculator

try:
    print("Test your Body Mass Index(BMI) Today...\n")
    name = input("Enter your Name: ")
    print(f"\nHello {name.upper()}, Let's get started :\)")
    
    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (m): "))
    bmi = int(weight / (height ** 2))
    
    if bmi < 18.5:
        print(f"\n{name.upper()}, your bmi is {bmi}. This is considered Underweight.")
    elif bmi >= 18.5 and bmi <= 24.9:
        print(f"\n{name.upper()}, your bmi is {bmi}. This is considered Normal.")
    elif bmi >= 25.0 and bmi <= 29.9:
        print(f"\n{name.upper()}, your bmi is {bmi}. This is considered Overweight.")
    elif bmi >= 30:
        print(f"\n{name.upper()}, your bmi is {bmi}. This is considered Obese.")

except ValueError:
    print ("Invalid input. Try again and make sure to enter valid numbers")