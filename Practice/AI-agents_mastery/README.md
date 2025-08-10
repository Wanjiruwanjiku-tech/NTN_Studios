# 30-DAY AI AGENTS MASTERY CHALLENGE

- A structured, practical and beginner to advanced roadmap to __master building AI agents__. Designed around free tools, daily micro-tasks, quick wins, and real-life use cases.

## OVERVIEW: What to Learn

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
| [Day 3](#day-three )| [Day 10](#day-ten )     | [Day 17](#day-seventeen ) | [Day 24](#day-twenty-four ) | |
| [Day 4](#day-four ) | [Day 11](#day-eleven )  | [Day 18](#day-eighteen )  | [Day 25](#day-twenty-five ) | |
| [Day 5](#day-five ) | [Day 12](#day-twelve ) | [Day 19](#day-nineteen )  | [Day 26](#day-twenty-six )  | |
| [Day 6](#day-six )  | [Day 13](#day-thirteen )| [Day 20](#day-twenty )    | [Day 27](#day-twenty-seven )| |
| [Day 7](#day-seven )| [Day 14](#day-fourteen )| [Day 21](#day-twenty-one )| [Day 28](#day-twenty-eight )| |

## DAY ONE

### What are AI agents, concept and real-world use

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

## DAY TWO

### Types of AI Agents

- AI agent types are based on _how they behave and make decisions_.

### The four main types of AI agents

1. __Reactive Agent.__
    - Acts based on current input and keeps no memory of state.
    - _**Example**_: _Obstacle-avoiding robot_

2. __Goal-Based.__
    - Chooses actions that help it reach a goal.
    - _**Example**_: _Path planning delivery drone_

3. __Utility-Based.__
    - Picks an action that maximize value like comfort, speed, safety.
    - _**Example**_: _Smart thermostat choosing mode_

4. __Learning Agent__
    - Learns from experience and improves decisions over time.
    - __Example__: _AI that plays chess and improves_

        __"Sometimes agents combine these traits"__

### Mini Challenge

1. __Question__

- What type of agent would best suit your project to _"Summarize the Kenyan school curriculum and create dynamic, personalized learning content for students_

__Answer__: _The project would have traits of both __Utility-Based Agents__ because _it selects the most effective and simplified content for the learner_, and __Learning Agents__ because _it adapts to different learning styles and student feedback overtime_.

## DAY THREE

## Setup + Your First AI Agent

- The goals for today include:
    1. Set up your Python environment for building AI Agents.
    2. Write your first simple agent in Python
    3. Understand how agents make decisions and interact

### Part 1: Setup instructions

- __Python 3.10+__ installed
- __VS Code__ installed with the python extension
- Install __openai__ and __langchain__
  - _pip install openai_
  - _pip install langchain_

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

## DAY FOUR

## Prompt Engineering for AI agents

1. __Part One:__ What is Prompt Engineering?

    - A __prompt__ is the instruction or input to give to an AI model like GPT, to get a specific type of output.
    - Insteadnof coding logic step-by-step like traditional programming, you __*use natural language as the "code"*__.
        - prompt = programming the mind of your AI agent

### Prompt Structure _(Most Common)

1. __Instruction__ - _What you want the AI to do_
2. __Context__ - _The background info, goals, roles, constraints_
3. __Input__ - _The question or user message_

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

1. __Part Two:__ Prompt Engineering Challenge
    - Imagine you are building an AI assistant for African sci-fi.
    - Create 2 prompts:
        1. A creative writing prompt that helps the AI generate story ideas about an African space explorer.
        2. A prompt that asks the AI to critique your story and give feedback on plot, characters, and style.
        - __Example:__
            1. "You are a creative writing assistant. Generate 3 unique story ideas about an African space explorer who discovers a new planet."
            2. "You are a literary critic. Read my story about an African space explorer and provide detailed feedback on plot, characters, and style."

## DAY FIVE

### Your first AI-Powered Agent using free tools

- We will use __mock responses__ to simulate GPT-style output locally while preserving the core logic of a real AI agent.

- This will help you build reusable agent structures that you can plug into OpenAI or other AI models later.

#### What is Context in AI Agents?

- __Context__ is the background information or knowledge that an AI agent uses to understand and respond to user input effectively.

- This helps the agent to respond appropriately based on what has already been said or done.

- Context can include:
    1. Previous user messages
    2. Agent's own responses
    3. Any relevant data or facts

- In __GPT-style models__, context = the prompt + the conversation history + the task instructions.
  - It is __stateless__, meaning, unless you include past info again in the input it forgets it.
  - In agents, context is often manually passed or stored in variables, memory or databases etc.

#### What is Memory in AI Agents?

- __Memory__ is the ability of an AI agent to remember past interactions, decisions, and data over time.

- It is the __persistent state__ that the agent can recall across interactions. There are two main types:
  1. __Short-term memory__ - stores recent interactions, like the last few messages. It lives during the session. Example: _Remembering your name in a session_.
  2. __Long-term memory__ - stores important information across sessions, like user preferences or past decisions. The information is stored permanently and can be retrieved later. Example: _Remembering your favorite color across multiple chats_.

- In real agents, memory is often stored in:
  - __Variables__ - for short-term, local memory
  - __Databases of Files__ - for long-term memory
  - __Vector stores__ - for semantic recall (e.g., storing embeddings)

#### Mocking GPT-Style Responses

- Since GPT models are expensive or unavailable offline, developers often _mock_ the responses to simulate how an agent would behave. This is done using functions that imitate how GPT would behave.

- Mocking means you simulate a response like

    def mock_gpt_response(prompt):
        if "hello" in prompt.lower():
            return "Hi there! I'm your AI agent. How can I help?"
        elif "weather" in prompt.lower():
            return "Sorry, I can't check the weather yet, but I can pretend it's sunny! ☀️"
        elif "bye" in prompt.lower():
            return "Goodbye! Hope to chat again soon."
        else:
            return "Hmm... I didn't understand that. Try asking something else."

- This allows you to test the agent's logic without needing an actual AI model.

#### How Context and Memory work in a Mock Agent

- Let's say you are _building an agent that simulates GPT and remembers the user's favorite color_.
  1. Remember what you tell it(Memory).
  2. Respond appropriately based on what it knows(Context).

## DAY SIX

## DAY SEVEN

## DAY EIGHT

## DAY NINE

## DAY TEN

## DAY ELEVEN

## DAY TWELVE

## DAY THIRTEEN

## DAY FOURTEEN

## DAY FIFTEEN

## DAY SIXTEEN

## DAY SEVENTEEN

## DAY EIGHTEEN

## DAY NINETEEN

## DAY TWENTY

## DAY TWENTY ONE

## DAY TWENTY TWO

## DAY TWENTY THREE

## DAY TWENTY FOUR

## DAY TWENTY FIVE

## DAY TWENTY SIX

## DAY TWENTY SEVEN

## DAY TWENTY EIGHT

## DAY TWENTY NINE

## DAY THIRTY
