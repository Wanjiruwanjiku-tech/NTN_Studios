
while True:
    try:
        name = input("What is your full name or type 'exit' to quit? ")
        if name.lower() == 'exit':
            print("Exiting...\n")
            break
        score_input = input("What is your score? ")
        if score_input.lower() == 'exit':
            print("Exiting...\n")
            break
        score = float(score_input)
        if score >= 90 and score <= 100:
            print(f"{name}, you got an A.\n")
        elif score >= 80 and score <= 89:
            print(f"{name}, you got a B.\n")
        elif score >= 70 and score <= 79:
            print(f"{name}, you got a C.\n")
        elif score >= 60 and score <= 69:
            print(f"{name}, you got a D.\n")
        elif score < 60:
            print(f"{name}, you got an F.\n")
        else:
            print("Your score should be between 0 - 100!\n")

    except ValueError:
        print(f"Use valid numbers.\n")