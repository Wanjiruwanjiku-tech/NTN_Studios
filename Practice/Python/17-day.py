# Number guessing game
import random

def show_welcome():
    print("\n--- Guess the Number! ---")

def choose_difficulty():
   
    print("1. Easy (1 -10)")
    print("2. Medium (10 - 50)")
    print("3. Hard (50-100)")
    print("4. Exit")
    

def easy_level():
    print("\n--- Easy Level ---")
    while True:    # replay loop
        answer = random.randint(1, 10)

        while True:    # guessing loop
            try:
                user_guess = int(input("Enter guess (1-10): "))
                if user_guess == answer:
                    print("\n---Congratulations you win! ---")
                    break
                elif user_guess < answer:
                    print("Too Low, try again!")
                elif user_guess > answer:
                    print("Too High, try again!")
            except ValueError:
                print("Invalid choice. Use valid numbers.")
        # ask for replay
        if not replay_game():
            break   # exit easy level, back to menu

def medium_level():
    print("\n--- Medium Level ---")
    while True:
        answer = random.randint(10, 50)
        
        while True:    
            try:    
                user_guess = int(input("Enter guess (10-50): "))
                if user_guess == answer:
                    print("\n---Congratulations you win! ---")
                    break
                elif user_guess < answer:
                    print("Too Low, try again!")
                elif user_guess > answer:
                    print("Too High, try again!")
            except ValueError:
                print("Invalid choice. Use valid numbers.")
         
        if not replay_game():
            break

def hard_level():
    print("\n--- Hard Level ---")
    while True:
        answer = random.randint(50, 100)

        while True:
            try:
                user_guess = int(input("Enter guess (50-100): "))
                if user_guess == answer:
                    print("\n---Congratulations you win! ---")
                    break
                elif user_guess < answer:
                    print("Too Low, try again!")
                elif user_guess > answer:
                    print("Too High, try again!")
            except ValueError:
                print("Invalid choice. Use valid numbers.")
        if not replay_game():
            break

def replay_game():
    replay = input("Do you want to play again at the same difficulty? (y/n): ")

    while True:
        if replay.lower() == "y":
            return True    # play again
        elif replay.lower() == 'n':
            return False   # back to menu
        else:
            print("Invalid choice, use 'y/n'")
            continue

while True:
    show_welcome()
    choose_difficulty()

    choice = input("Choose difficulty level (1-3): ")

    if choice == "1":
        easy_level()
    elif choice == "2":
        medium_level()
    elif choice == "3":
        hard_level()
    elif choice == "4":
        print("--- Goodbye ---")
        break
    else:
        print("Invalid choice. Please select 1-4")

