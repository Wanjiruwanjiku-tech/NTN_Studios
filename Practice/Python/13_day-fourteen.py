def calculate_area(length, width):
    return length * width

# Call the Function
while True:
    print("Calculate the Area!")

    length = input("Insert the length or 'exit' to quit: ")
    if length.lower() == "exit":
        print("Exiting Program...")
        print("-" * 40)
        break

    width = input("Insert the width or 'exit' to quit: ")
    if width.lower() == "exit":
        print("Exiting Program...")
        print("-" * 40)
        break

    try:
        user_length = float(length)
        user_width = float(width)

        result = calculate_area(user_length, user_width)
        print(f"The result is {result}cm2")
        print("-" * 40)
    except Exception as e:
        print("Error Occured. Please enter valid numbers for length and width.")