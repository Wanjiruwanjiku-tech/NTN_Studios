import random

secret_number = random.randint(1, 20)

print("* Welcome to the Number Guessing Game! *")
print("I'm thinking of a number between 1 and 20...")

while True:
    guess = input("Take a guess or 'exit' to quit: ")
    if guess.lower() == "exit":
        print("Exiting game ...")
        break
    
    user_guess = int(guess)

    if user_guess == secret_number:
        print("* Correct! You guessed the number! *")
        break
    elif user_guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
print("-" * 40)
