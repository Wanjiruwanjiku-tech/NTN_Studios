# 30-DAY AI AGENTS MASTERY CHALLENGE.
-----------------------------------------------------

- A structured, practical and beginner to advanced roadmap to __master building AI agents__. Designed around free tools, daily micro-tasks, quick wins, and real-life use cases.

-------------------------------------------------------------------------------
## OVERVIEW: What to Learn.
- By the end of the challenge:

1. Understand AI agents and automation frame works like LangChain, AutoGen, CrewAI
2. Build your ouw custom AI agents using Python
3. Intergrate agents with tools
4. Create real-life projects
5. Gain enough expertise to teach others and freelance in the field.

---------------------------------------------------------------------------------------------------------

### Quick Links
| __Week One__              | __Week Two__                  | __Week Two__  | __Week Four__               | __Week Five__      |
|---------------------------|-------------------------------|---------------|-----------------------------|--------------------|
| [Day 1](#day-one )  | [Day 8](#day-eight )    | [Day 15](#day-fifteen )   | [Day 22](#day-twenty-two )  | [Day 29](#day-twenty-nine )|
| [Day 2](#day-two )  | [Day 9](#day-nine )     | [Day 16](#day-sixteen )   | [Day 23](#day-twenty-three )| [Go to Day 30](#day-thirty )|
| [Day 3](#day-three )| [Day 10](#day-ten )     | [Day 17](#day-seventeen ) | [Day 24](#day-twenty-four ) |
| [Day 4](#day-four ) | [Day 11](#day-eleven )  | [Day 18](#day-eighteen )  | [Day 25](#day-twenty-five ) |
| [Day 5](#day-five ) | [Day 12](#day-tweleve ) | [Day 19](#day-nineteen )  | [Day 26](#day-twenty-six )  |
| [Day 6](#day-six )  | [Day 13](#day-thirteen )| [Day 20](#day-twenty )    | [Day 27](#day-twenty-seven )|
| [Day 7](#day-seven )| [Day 14](#day-fourteen )| [Day 21](#day-twenty-one )| [Day 28](#day-twenty-eight )|


------------------------------------------------------------------------------------------
# DAY ONE
## What are AI agents, concept and real-world use
-------------------------------------------------------------------

- _AI agents_ are an autonomous AI entity that can __percieve__ its environment, make __decisions__ and __act__ toward achieving a goal.

    1. Percieves its environment for example through input, sensors, APIs or user prompts.
    2. Decides what to do using logic, rules or AI Models(a trained program that makes decisions)
    3. Acts to achieve specific goals like responding, generating text/code, retrieving info, taking action

    " _Think of it is as an AI entity that observes, thinks and acts towards a goal_"

- AI agents are different from chatbots because they're;

    1. __Goal Oriented__. Not just asking questions and getting answers.
    2. ___Autonomous__. Meaning they can take multiple steps without being told.


## Real-Life Examples of AI Agents

- __*Medical AI Agents*__ that diagnose diseases based on symptoms and Lab results.
- __*Research Agents*__ that summarize loads of datalike from 10 different websites about a topic and provide insights.
- __*Dev Agent*__ that writes code, debugs errors, explains functions
-----------------------------------------------------------------------------------------------------------------

# DAY TWO
## Types of AI Agents
--------------------------------------------------------------------------------------------------------------

- AI agent types are based on _how they behave and make decisions_.

### The four main types of AI agents.
1. __Reactive Agent.__
    - Acts based on current input and keeps no memory of state.
    - _**Example**_: _Obstacle-avoiding robot_

2. __Goal-Based.__
    - Chooses actions that help it reach a goal.
    -  _**Example**_: _Path planning delivery drone_

3. __Utility-Based.__
    - Picks an action that maximize value like comfort, speed, safety.
    -  _**Example**_: _Smart thermostat choosing mode_

4. __Learning Agent__
    - Learns from experience and improves decisions over time.
    -  _**Example**_: _AI that plays chess and improves_

        __"Sometimes agents combine these traits"__

### Mini Challenge
1. __Question__
- What type of agent would best suit your project to _"Summarize the Kenyan school curriculum and create dynamic, personalized learning content for students_

__Answer__: _The project would have traits of both __Utility-Based Agents__ because _it selects the most effective and simplified content for the learner_, and __Learning Agents__ because _it adapts to different learning styles and student feedback overtime_.

----------------------------------------------------------------------------------------------------
# DAY THREE
## Setup + Your First AI Agent
-----------------------------------------------------

- The goals for today include:
    1. Set up your Python environment for building AI Agents.
    2. Write your first simple agent in Python
    3. Understand how agents make decisions and interact

### Part 1: Setup instructions
- __Python 3.10+__ installed
- __VS Code__ installed with the python extension
- Install __openai__ and __langchain__
    - *pip install openai*
    - *pip install langchain*

- _Today we'll begin with a minimal agent that works with or without an_ __OpenAI API key__.

### Part 2: Your First AI Agent - Rule Based Decision Maker

- This agent acts based on simple input using decision rules. It is a simple __AI-like chatbot__ that responds to user input with __predefined replies__. It runs in the terminal and waits for the user to type something then it responds.

- The function takes __one parameter__ input_data that takes the users message.

- We then convert the input to lowercase so that comparisons are not __case-sensitive__.

- We then __define keywords__ with the responses we want to give.

- Then we create a simple __chat interface__.
    - Print a welcome message when the chatbot starts
    - Use an infinite loop so that the chatbot can keep running (__while *True*__ does the trick)
    - Prompt the user to type something (__user_input = *input("You: ")*__)
    - If the user exits, the loop breaks.

        if user_input.lower() == "exit":
            print("Exiting...")
            break

            __*#day3_agent.py*__
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


- ▶️ To run:
    - In terminal:
        - python day3_agent.py
    - Try:
        1. hello
        2. what’s the weather like
        3. bye
        4. anything random
        5. then exit to quit.
---------------------------------------------------------

# DAY FOUR
## Prompt Engineering for AI agents.
---------------------------------------------------------
1. __Part One:__ What is Prompt Engineering?
    - A __prompt__ is the instruction or input to give to an AI model like GPT, to get a specific type of output.
    - Insteadnof coding logic step-by-step like traditional programming, you __*use natural language as the "code"*__.
        - prompt = programming the mind of your AI agent

### Prompt Structure _(Most Common)
1. __Instruction__ - *What you want the AI to do*
2. __Context__ - *The background info, goals, roles, constraints*
3. __Input__ - *The question or user message*

### Examples
- Examples of Prompts
    1. __Basic Prompt__

        You are a helpful assistant. Answer concisely.
        User: What is the capital of Kenya?

    2. __Agent with Role + Task__

        You are a friendly Kenyan tour guide. Recommend 3 exciting places for a visitor to Nairobi on a budget. Include one food spot.

    3. __Logic Prompt (for reasoning)__

        You are a smart AI agent. Solve this step-by-step:
        If a car travels 60 km in 1.5 hours, what is the average speed?

2. __Part Two:__ Prompt Engineering Challenge
    - Imagine you are building an AI assistant for African sci-fi.
    
    - Create 2 prompts:
        1. A creative writing prompt that helps the AI generate story ideas about an African space explorer.
        2. A prompt that asks the AI to critique your story and give feedback on plot, characters, and style.
        