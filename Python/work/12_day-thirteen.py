# Day Thirteen Functions

def check_age(age):
    if age >= 18:
        print('Access granted')
    else:
        print('Access denied')

# Call the function
while True:
    user_age = input("Enter your age or 'exit' to quit: " )
    if user_age.lower() == "exit":
        print("Exiting...")
        exit()
    try:
        age = int(user_age)
        check_age(age)
    except ValueError:
        print("Please enter a valid number or 'exit'.")