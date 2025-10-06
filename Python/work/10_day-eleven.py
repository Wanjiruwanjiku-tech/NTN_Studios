# Mini Task: Build a Voter Eligibility checker
try:
    # Coutry
    voting_age = {
            "kenya": 18,
            "japan": 20,
            "mexico": 19,
            "brazil": 16,
            "india": 18
        }

    while True:
        print("Check your Eligibility to Vote!")
        # Check for country
        country = input("Enter your country or 'exit' to quit: ")
        if country.lower() == 'exit':
            print("Exiting Program...")
            break
        if country.lower() not in voting_age:
            print("Sorry I don't have voting age info for that country.")
            continue
        required_age = voting_age[country]
        # Check Age
        age = input("Enter your Age or 'exit' to quit: ")
        if age.lower() == 'exit':
            print("Exiting Program...")
            break
        if not age.isdigit():
            print("Use Numbers to enter your age!")
            continue

        user_age = int(age)

        # Ask for id
        has_id = input("Do you have an ID 'yes/no' or 'exit' to quit: ")
        if has_id.lower() == "exit":
            print("Exiting program...")
            break
        if has_id not in ["yes", "no"]:
            print("Please answer 'yes' or 'no'!")
            continue

        # Check eligilility
        if user_age >= required_age and has_id.lower() == "yes":
            print(f"You are eligible to vote in {country.title()}.")
        else:
            print(f"You are not eligible to vote in {country.title()}.")
        print("-" * 40)

except Exception as e:
    print(f"An error occurred: {e}")