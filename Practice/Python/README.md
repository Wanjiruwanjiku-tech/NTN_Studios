# 30-DAY _PYTHON_ MASTERY CHALLENGE: Beginner to Advanced
----------------------------------------------------------------

## Breakdown

1. __Week One(Days 1-7)__ - *Syntax, Variables, input/outout.*
2. __Week Two(Days 8-14)__ - *Control flow, conditions and loops.*
3. __Week Three(Days 15-21)__ - *Lists, tuples, dictionaries, sets.*
4. __Week Four(Days 22-28)__ - *Functions, file Handling and intermediate Python.*
5. __Week Five(Days 29-30)__ - *Advanced concepts.*

---------------------------------------------------------------------------------------

### Quick Links

[Go to Day 1](#day-one )
[Go to Day 2](#day-two )
[Go to Day 3](#day-three )
[Go to Day 4](#day-four )
[Go to Day 5](#day-five )
[Go to Day 6](#day-six )
[Go to Day 7](#day-seven )
[Go to Day 8](#day-eight )
[Go to Day 9](#day-nine )
[Go to Day 10](#day-ten )
[Go to Day 11](#day-eleven )
[Go to Day 12](#day-tweleve )
[Go to Day 13](#day-thirteen )
[Go to Day 14](#day-fourteen )
[Go to Day 15](#day-fifteen )
[Go to Day 16](#day-sixteen )
[Go to Day 17](#day-seventeen )
[Go to Day 18](#day-eighteen )
[Go to Day 19](#day-nineteen )
[Go to Day 20](#day-twenty )
[Go to Day 21](#day-twenty-one )
[Go to Day 22](#day-twenty-two )
[Go to Day 23](#day-twenty-three )
[Go to Day 24](#day-twenty-four )
[Go to Day 25](#day-twenty-five )
[Go to Day 26](#day-twenty-six )
[Go to Day 27](#day-twenty-seven )
[Go to Day 28](#day-twenty-eight )
[Go to Day 29](#day-twenty-nine )
[Go to Day 30](#day-thirty )

------------------------------------------------------------------------------------------
# DAY ONE
## Hello Python
--------------------------------------------------------------------------------
- __Goal__: Run your first Python program.

    #Python program
    print("Hello Natalie"")

- Print() is a built-in function that outputs to the console.
- The text inside the quote is a string
- The __#__ is used for comments

------------------------------------------------------------------------------------------

# DAY TWO
## Variables and Data Types.
-----------------------------------------------------
- __Goal__: Understand how to store values in variables and use basic data types

    name = "Natalie"
    age = 27
    height = 1.65

1. __name__ is a string created using double or single quotes.
2. __age__ is an integer
3. __height__ is a float (decimal)

### Data types

- Python automatically assigns data types when you assign values

|__Type__  | __Example__| __Use case__          |
|----------|------------|-----------------------|
|_str_     | "hello"    | Names, messages, text |
|_int_     | 42         | Whole numbers         |
|_float_   | 3.14       | Decimals              |
|_bool_    | True/False | Logic deecisions      |

-------------------------------------------------------------------------------------------

# DAY THREE
## Taking user input
-----------------------------------------------------------------------------------------------
- __Goal__: Learn how to get data from a user, use it in a program and convert it into the right type

### Key concepts

1. __input()__ function
- This function *pauses the program and waits for th user to provide input*

    name = input("What is Your Name? ")
    print("hello,", name)

2. __All input values are strings__
- Even when the user types a number, Python reads it as a string. To fix this you must convert the user's input into appropriate data type in order to use their input in your program, if not converted errors will arise.

    age = int(input("Enter your age, "))
    __*int()* converts the users input into a whole number/ the appropriate data type that can be used in the program__


