# Taking user Input

name = input("Enter your name: ")
age = int(input("Enter your age: "))
number = int(input("How many years to add to your age? "))
result = age + number

# Printing the result
print("\nThank you for playing my game!\n")
print("\tHello", name, "your current age is", age, "and after", number, "years you will be", result, "years old\n\t:)")

# How to concatenate input() with an integer
age = int(input("Enter your age: "))
print("Next year you will be " + str(age + 1))