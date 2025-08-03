# Mini Project 5: Username Generator
# Goal: Generate a username using personal info.
# Requirements:
# 1. Ask for first name, last name and favorite number.
# 2. Generate a username

first_name = input("Enter your First Name: ")
last_name = input("Enter your Last Name: ")
favorite_number = input("Enter your Favorite Number: ")

first = first_name.lower()
last = last_name.lower()

username = first[:3] + favorite_number + "_" + last[-3:].capitalize()
# Take the first 3 letters of first name, add favorite number, and last 3 letters of last name capitalized

print(f"Your generated username is: {username}\n")
print("Username Breakdown:")
print(f"\tFirst Name: {first_name}")
print(f"\tLast Name: {last_name}")
print(f"\tFavorite Number: {favorite_number}")
print(f"\tGenerated Username: {username}\n")
print("Thank you for using the Username Generator!")