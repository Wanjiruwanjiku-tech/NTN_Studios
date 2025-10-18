def chat_interface(user_input):

    animals = [
        "Cat",
        "Lion",
        "Elephant",
        "Rhino",
        "Dog"
    ]

    animals.append(user_input)

    print(f"\nHere is a list of Animals in the zoo: {animals}")

# User Interface
while True:
    print("Welcome to the Zoo!")
    new_animal = input("Add a new animal Here or 'exit' to quit: ")
    if new_animal.lower() == "exit":
        print("Exiting...")
        print("=" * 40)
        print("\n")
        break
    zoo_animals = chat_interface(new_animal)