matrix = [[0, 1], [2, 3]]
print(matrix)
print("length: ", len(matrix))

numbers = list(range(20)) # List function also creates lists
print(f"\nnumbers") # Does not include 20, prints 0-19
print("length: ", len(numbers))

zeros = [0] * 100
print(f'\n{zeros}') # Prints 100 zeros
print("length: ", len(zeros))

chars = list('Hello World')
print(f"\n{chars}") # Each character becomes an item in a list
print("length: ", len(chars)) # Print the length of chars

# Accessing Items
print("\nAccessing Items in a list")
name = list("Natalie")
print(name)
print(name[0]) # First
print(name[-1]) # last
print(name[4])

name2 = list("Martin")
print(name2)
name2[0] = "A"
print(f"Replace first letter with 'A'{name2}")
print(f"Sliced: {name2[2:4]}")