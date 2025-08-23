# 30-DAY CHALLENGE ON SOFTWARE ENGINEERING

- __Challenge Overview__
  1. Phase 1 (Days 1-10): _Core Foundations_
  2. Phase 2 (Days 11-20): _Backend, Frontend & System Thinking_
  3. Phase 3 (Days 21-30): _Building, Testing and Scaling Projects_

## Day 1: What is Software Engineering?

- __GOAL__:
  - Understand what software engineering is, what engineers do, and how software development differs from coding.

- Software engineering is the art and science of building, testing, maintaining, and scaling software systems. It is not just writing code, it's solving problems systematically, using tools, methods and teamwork.

- Imagine building a house, _coding_ is laying the bricks, _software engineering_ is designing the house, planning plumbing, electricity and thinking how many people are going to live there and for how long.

### Roles of a Software Engineer

1. Solve real-world problems using code
2. Design system architecture
3. Choose the right tools/languages
4. Write readable, maintainable code
5. Test and debug code
6. Collaborate in teams
7. Maintaining and improving systems over time.

#### 🧪 Quiz

- Definition: _Software Engineering is the art and science of building and maintaining software programs in a reliable way in order to solve real-world problems_

  - Problem: Long hospital wait times → Software: Appointment scheduling system with priority triage logic

  - Problem: Inadequate food Irrigation → Software: Watering system that detects dry soil and releases enough water for irrigation without wastage.

  - Problem: Fraud & corruption → Software: Fraud detection system that recognizes patterns and flags them.

  - Problem: Inadequate Ambulance Services → Software: Software that uses cameras to detect medical and trauma emergencies and triggers emergency medical services response

  - Problem: Unemployment → Software: A System that recognizes and spends time learning about a students patterns and provides a list of potential careers, tailored courses, and coaching

- What is the difference between coding and software engineering?
  - _Coding is the tool used to build software programs. Software engineering is how it is done, this includes designing, planning, and defining its purpose to solve real-world problems._

- Why is testing an essential part of software engineering?
  - _To ensure the program works as intended, to identify problems and make corrections or improvements_

- Name 3 responsibilities of a software engineer beyond coding.
  - _To maintain and improve systems over time_
  - _To solve real-world problems_
  - _To collaborate in teams_

  ## DAY 2: Programming Languages and Development

- __GOAL__:
- Understand the role of programming languages in software engineering, and how they are used to build software, as well as how to pick the right tools for the job

- A __programming language__ is a way to communicte with computers. Each programming language has its rules (_syntax_) and is good at certain things.

### Types of Programming Languages

|__Type__      |__Example__          |__Best For__                |
|--------------|---------------------|----------------------------|
|__High-level__| _Python, JavaScript_|Readable, begginner-friendly|
|__Low-level__ |_C, Assembly_        |Hardware-level control      |
|__Web__       |_HTML, CSS, JS_      |Websites                    |
|__Backend__   |_Java, Python, Go_   |Servers, APIs               |
|__Systems__   |_C, Rust_            |Operating systems           |
|__Data/AI__   | _Python, R_         |Machine Learning, Analysis  |

### Development Tools

1. __Text Editor/IDE__: VS Code, IntelliJ, PyCharm
2. __Version Control__: Git + GitHub (To save and track code)
3. __Terminal/Command Line__: Where the code and tools run
4. __Debugger__: Helps find and fix bugs in your code

- An IDE (_Integrated Development Environment_) is a software application that provides a complete environment suited for writing, testing and debugging code.

- Features of an IDE include:
  1. __Code Editor__: This is where you write your code examples include _VS Code, PyCharm, IntelliJ_.
  2. __Syntax Highlighting__: Colors Keywords, variables, functions for easy readability.
  3. __Code Completion__: The IDE suggests code snippets as you type.
  4. __Debugger__: Helps the developer find and fix errors
  5. __Intergrated Terminal__: Many come with a built in terminal
  6. __Project Management__: The IDE can handle multiple files and folders.
  7. __Plugins and Extensions__: This allow the developer to add extra features like Git Integration or Docker e.t.c
- When to use IDEs
  1. _When developing Applications, websites or APIs_
  2. _When you need debuging tools_
  3. _When managing large projects with multiple files_
  4. _When you want code suggestions and productivity boosts_

- The _Terminal_, Is a text-based interface where you type commands to interact with your computer or server.

- Features of a Terminal include:
  1. __File Navigation__: The terminal allows the developer to navigate files using commands like _cd, ls, dir_
  2. __Package Installation__: A developer installs packages and tools via the terminal using commands like _apt, npm, pip_
  3. __Run and Compile__: Developer can run and compile code they write on the terminal e.g _python app.py, gcc main.c_
  4. __System management__: Throught the terminal developers can manage systems and process files
  5. __Connect to remote serves__ using the _ssh_ command

- When to use the Terminal
  1. _Installing and updating software_
  2. _Running code quickly_
  3. _Managing servers or cloud environments_
  4. _Using Git for Version control_
  5. _When working in Linux environments_

## 📅 Day 3: How the Web Works (Client–Server Model)

- The goal is to _understand how information flows_ when you open a website or use an app.

- When you type _google.com_
  1. Client(your browser) asks for information like _"Hi, please give me Googles homepage."_
  2. Server(computer elsewhere) send a responsee like _"Here is the hompeage HTML, CSS, and JS(Codebase) files"_
  3. Client(your browser) takes the files and displays them.

### Key Concepts

1. __HTTP__ (_HyperText Transfer Protocol_): This is the language between servers and browsers

2. __Frontend__: What you see i.e the _User Interface(UI)_ like buttons, fonts, colors

3. __Backend__: What happens behind the scenes. This inclides _databases, servers, APIs_.

4. __Database__: Where data lives.