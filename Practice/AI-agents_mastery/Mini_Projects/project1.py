# Mini Project 1: Simple  Chatbot
# Contains predefined responses

def agent_one(input_data, name):
    # convert the input to lowercase.
    input_data = input_data.lower()
    name = name.capitalize()
    # Predefined responses
    if "hello" in input_data:
        return (f"Hi {name}, my name is Nat and I'm your AI agent. How can I help?")
    elif "quote" in input_data:
        return (f"{name} your quote is 'Mercy happens when God\'s Love crashes into our shame, when we recognize that in our worst moments, He looked at us, loved us and gave us his life so we could live'")
    elif "weather" in input_data:
        return (f"Sorry {name}, I can't check the weather yet, but I can pretend it's sunny! ☀️")
    elif "bye" in input_data:
        return (f"Goodbye {name}, see you soon")
    else:
        return "I don't understand your question"

# QUESTIONS
# 1.Hello how are you?
# 2. Can you give me a quote?
# 3. What's the weather like?
# 4. bye!

# Simple interface
if __name__ == "__main__":
    print("🤖 AI Agent: Ready to chat!")
    name = input("Enter your name: ").strip().lower()
    print (f"🤖 Agent: Hello {name}, Let's get started!")
    # Infinite loop to keep the program open
    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Exiting agent. Bye!")
            break
        # Call the agent function with user input
        response = agent_one(user_input, name)
        print(f"🤖 Agent: {response}")