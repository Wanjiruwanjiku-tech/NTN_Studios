# Working with strings

first_name = input("Enter your first Name: ")
second_name = input("Enter your second Name: ")
fun_fact = input("Tell us a Fun fact about yourself starting with 'I ...': ")
sentence = "HELLO MY NAME IS NATALIE AND I  am LEARNING HOW TO CODE IN PYTHON. IN THIS PROGRAM I AM LEARNING HOW TO WORK WITH STRINGS."
print("\n")
print(sentence.lower())
print("\n")
print(f"Hello, {first_name.upper()} {second_name.upper()}. A fun fact about you is {fun_fact.replace('I', 'You')}")