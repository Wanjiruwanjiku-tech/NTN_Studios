# day3_agent.py

def ai_agent(input_data):
    # Simple reactive agent logic
    input_data = input_data.lower()
    if "hello" in input_data:
        return "Hi there! I'm your AI agent. How can I help?"
    elif "weather" in input_data:
        return "Sorry, I can't check the weather yet, but I can pretend it's sunny! ☀️"
    elif "bye" in input_data:
        return "Goodbye! Hope to chat again soon."
    else:
        return "Hmm... I didn't understand that. Try asking something else."

# Simple interface
if __name__ == "__main__":
    print("🤖 AI Agent: Ready to chat!")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Exiting agent. Bye!")
            break
        response = ai_agent(user_input)
        print("Agent:", response)
