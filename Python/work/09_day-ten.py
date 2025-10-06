# Online Library Access
try:
    while True:
        user_age = input("Enter your age or 'exit' to quit: ")
        if user_age.lower() == "exit":
            print("Exiting...\n")
            break
        age = int(user_age)
        if age >= 18:

            member = input("Are you a Member?(yes/no) or 'exit' to quit: ")
            if member.lower() == "exit":
                print("Exiting...\n")
                break

            if member.lower() == 'yes':
                print("Welcome to the Library. Full access is granted")
            elif member.lower() == 'no':
                print("Please register for full access.")

                while True:
                    guidlines = input("\nNeed help or guidance? 'yes/no' or 'exit' to quit: ")
                    if guidlines.lower() == "exit":
                        print("Redirecting...\n")
                        break

                    if guidlines.lower() == 'yes':
                        print("""Guidelines
                        
                        1. Visit ntnstudios.com
                        2. Click register
                        3. Fill in the required details
                        """
                        )
                    elif guidlines.lower() == 'no':
                        print("Thank you for visiting.")
                    else:
                        print("Use the stated answers 'yes/no'")

            else:
                print("Kindly Confirm Your Membership")
            
        else:
            print("Access denied. Parental consent required.")
            
except ValueError:
    print("Error! Use Valid Numbers")