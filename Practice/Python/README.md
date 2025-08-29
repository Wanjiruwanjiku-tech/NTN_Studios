# 30-DAY _PYTHON_ MASTERY CHALLENGE: Beginner to Advanced

## Breakdown

1. __Week One(Days 1-7)__ - _Syntax, Variables, input/outout._
2. __Week Two(Days 8-14)__ - _Control flow, conditions and loops._
3. __Week Three(Days 15-21)__ - _Lists, tuples, dictionaries, sets._
4. __Week Four(Days 22-28)__ - _Functions, file Handling and intermediate Python._
5. __Week Five(Days 29-30)__ - _Advanced concepts._

---------------------------------------------------------------------------------------

### Quick Links

| __Week One__              | __Week Two__                  | __Week Two__                    |
|---------------------------|-------------------------------|---------------------------------|
| [Go to Day 1](#day-one)  | [Go to Day 8](#day-eight)    | [Go to Day 15](#day-fifteen)   |
| [Go to Day 2](#day-two)  | [Go to Day 9](#day-nine)     | [Go to Day 16](#day-sixteen)   |
| [Go to Day 3](#day-three)| [Go to Day 10](#day-ten)     | [Go to Day 17](#day-seventeen) |
| [Go to Day 4](#day-four) | [Go to Day 11](#day-eleven)  | [Go to Day 18](#day-eighteen)  |
| [Go to Day 5](#day-five) | [Go to Day 12](#day-twelve)  | [Go to Day 19](#day-nineteen)  |
| [Go to Day 6](#day-six)  | [Go to Day 13](#day-thirteen)| [Go to Day 20](#day-twenty)    |
| [Go to Day 7](#day-seven)| [Go to Day 14](#day-fourteen)| [Go to Day 21](#day-twenty-one)|

| __Week Four__                     | __Week Five__                    |
|-----------------------------------|----------------------------------|
| [Go to Day 22](#day-twenty-two)  | [Go to Day 29](#day-twenty-nine)  |
| [Go to Day 23](#day-twenty-three)| [Go to Day 30](#day-thirty)       |
| [Go to Day 24](#day-twenty-four) |                                   |
| [Go to Day 25](#day-twenty-five) |                                   |
| [Go to Day 26](#day-twenty-six)  |                                   |
| [Go to Day 27](#day-twenty-seven)|                                   |
| [Go to Day 28](#day-twenty-eight)|                                   |

## DAY ONE

### Hello Python

- __Goal__: Run your first Python program.

    #Python program
    print("Hello Natalie"")

- Print() is a built-in function that outputs to the console.
- The text inside the quote is a string
- The __#__ is used for comments

## DAY TWO

### Variables and Data Types

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

## DAY THREE

### Taking user input

- __Goal__: Learn how to get data from a user, use it in a program and convert it into the right type

### User Input Concepts

1. __input()__ function

- This function _pauses the program and waits for th user to provide input_

    name = input("What is Your Name? ")
    print("hello,", name)

1. __All input values are strings__

- Even when the user types a number, Python reads it as a string. To fix this you must convert the user's input into appropriate data type in order to use their input in your program, if not converted errors will arise.

        age = int(input("Enter your age, "))

- __*int()* converts the users input into a whole number/ the appropriate data type that can be used in the program__

## DAY FOUR

### Basic Math and Arithmetic Operators

- Our goal is to _perform math operations in python and build a simple calculator_.

#### Key concepts: Arithmetic Operators

#### Arithmetic Operators

|__Operator__ | __Description__   |__Example__ |__Result__|
|-------------|-----------------  |------------|----------|
|_+_          | Addition          | 3 + 2      | 5        |
|_-_          | Subtraction       | 3 - 2      | 1        |
|_*_          | Multiplication    | 3 * 2      | 6        |
|_/_          | Division          | 9 / 2      | 4.5      |
|_//_         | Floor division    | 9 // 2     | 4        |
|_%_          | Modulus(remainder)| 9 % 2      | 1        |
|_**_         | Exponentiation    | 2 ** 3     | 8        |

## DAY FIVE

### Working with strings

- The goal is to _understand how to manipulate and format strings using python's built in methods_.

#### Key string concepts

1. Common string methods
    text = "Natalie"
    - __text.strip()__ - removes whitespace
    - __text.lower()__ - turn all text to lowercase
    - __text.upper()__ - turns all text to uppercase
    - __text.replace("Natalie", "Python pro")__ - replaces selected words with the specified word
    - __text.split(",")__ - splits words, and returns a list

2. Concatenation (__Joining strings together__)
    name = "Natalie"
    greeting = "Hello, " + name + "!"

3. Formatted strings (__f-strings__)
    age =27
    print(f"I am {age} years old)

## _DAY SIX_

### Type Conversion and Error Handling

- The goal is to _Learn how to convert between data types and handle errors gracefully so your program doesn't crash_.

### Key Concepts

1. __Type conversion__

    | __Function__   | __Converts to...__ | __Example__         | __Code__                      |
    |----------------|--------------------|---------------------|-------------------------------|
    | _int()_        | _Integer_          | int("4") => 4       | age = int("28")               |
    | _str()_        | _String_           | str(4) => "4"       | print(str(age) + "years old") |
    | _float()_      | _Float_            | int("4.12") => 4.12 | height = float("1.65")        |

2. __Hanling Errors__
    - Done using _try/except_ block. Used to prevent code crashes when the user enters the wrong input.

        try:
            age = int(input("Enter your age: "))
            print(f"Next year you will be {age + 1}")
        except ValueError:
            print("Please Enter a valid Number!")

    - This is called __Exception Handling__

### Task

1. Write a program that:
    1. Asks the user for a number
    2. Tries to convert it into an integer
    3. If it works, prints the number doubled
    4. If not, prints _"Invalid input. Please enter a number"_

    - __Answer File__ : __05_day-six.py__
    - Open terminal and run __python 05_day-six.py__ to test.

## _DAY SEVEN_

### _Mini Project + Quiz_

- The goal is to _apply everything from __Days 1-6__ into a mini real-life app and test your knowledge_.

### Project: _BMI Calculator_

- Build a program that:
    1. Asks your name.
    2. Asks for your weight (kg)
    3. Asks for your weight (m)
    4. Calculates and displays your BMI
        - BMI = weight / (height ** 2)
    5. Classifies it
        - BMI < 18.5 => Underweight
        - 18.5-24.9 => Normal
        - 25-29.0 => overweight
        - 30+ => obese

- __Answer File:__ __06_day-seven.py__.
- run __python 06_day-seven.py__ to test.

#### Week One Done

## DAY EIGHT

### Making Decisions with _if, elif_ and _else_

- The goal is to learnhor to let your program __make decisions__.

### Decision Making Concepts

1. __if__ Statement

        age = 18
        if age >= 18:
            print("You are an adult.")

2. __else__ Statement

        if age >= 18:
            print("You are an adult.")
        else:
            print("You are a child.")

3. __elif__ Statement

        if age >= 18:
            print("You are an adult.")
        elif age >= 15
            print("You are a minor")
        else:
            print("You are a child.")

### Relational Operators

| __Symbol__| __Meaning__     | __Example *(x = 5)*__|
|-----------|-----------------|----------------------|
| _==_      | Equal to        | __x == 5__           |
| _!=_      | Not equal to    | __x != 3__           |
| _>_       | Greater than    | __x > 4__            |
| _<_       | Less than       | __x < 6__            |
| _>=_      | Greater or equal| __x >= 5__           |
| _<=_      | Less or equal   | __x <= 5__           |

## DAY NINE

### Comparison and Logical Operators

- The __goal__ is to master multiple conditions using logical operators

#### Logical Operators

|__Operator__|__Description__                       |__Example__      |__Result__       |
|------------|--------------------------------------|-----------------|-----------------|
|_and_       |True if both conditions are true      |x > 3 and x < 10 |true             |
|_or_        |True if at least one condition is true|x > 3 or x < 10  |if either is true|
|_not_       |Reverses the Result                   |not(x > 5)       |true if x <= 5   |

        age = 20
        has_id = True
        if age >= 18 and has_id:
            print("You can enter.")
        else:
            print("Access denied.")

## DAY TEN

### Nesting and Multiple Conditions

- The goal is to __Learn nested conditionals snd how to combine multiple checks__ for more complex decision making.

1. Nested if statements

- You can place an if statement inside another if statement to create more complex conditions.

        age = 20
        has_id = True
        if age >= 18:
            if has_id:
                print("You can enter.")
            else:
                print("You need an ID.")
        else:
            print("You are too young.")

## DAY ELEVEN

### Logical Operators Deep Dive (and, or, not)

- The Goal is to _learn how to combine multiple conditions more effectively_.
  - _and_ => both conditions must be True
  - _or_ => at least one must be True
  - _not_ => reverses the condition

## DAY TWELVE

### Loops (for and while)

- __For loops__ _repeat for each item in a collection_

  fruits = ["apple", "banana", "cherry"]
  forr fruit in fruits:
    print(f"I like{fruit})
- It loops through each element in a list, string or other iterable
- _fruit_ is a loop variable that changes each iteration

- __While loops__ _Repeat while a condition is true_

  count = 1
  while count <= 5:
    print(f"count is {count}")
    count += 1
- This runs until the condition becomes false. _Forgetting to update the variable can cause an infinite loop_.

#### Loop control statements

1. __break__ Exits the loop immeaditaly
2. __continue__ Skip the rest of the current iteration and move to the next one
3. __pass__ Do nothing (placeholder)

  for num in range(1, 6):
    if num == 3:
        continue  # Skip printing 3
    print(num)

## DAY THIRTEEN

### Functions in Python

- Functions help the developer to
  1. _Organize_ code into reusable pieces
  2. _Avoid Repetition_ by writing logic once and calling it multiple times
  3. _Make your code cleaner_ and easier to debug

- __Basic Function__
  
  def greet():
    print("Hello, welcome to Python!")

1. __def__: This is the keyword to define a function
2. __greet__: This is the function name
3. __()__: The parenthesis can hold additional inputs or parameters.
4. __:__: Tells python that a block is starting
5. __Indentation__: This is the code inside the function

- _To call the function_: __greet()__

- __Functions with Parameters(inputs)__

  def greet_user(name):
    print(f"Hello {name}, welcome to Python!")

- _To call the function_: greet_user("Natalie")

- __NB__: _break_ is only valid inside a loop. To fix this, use _exit()_ or _sys.exit()_ to terminate the program when the user types "exit":

## DAY FOURTEEN

### Functions with Parameters and Return Values

- In many cases, _functions return values_ instead of printing them. This makes them more reusable.

  def square(number):
    return number * number

result = square(5)
print("The square is:", result)

- 🔎 What’s happening here
  1. square(5) runs the function.
  2. Instead of printing inside, it returns the result.
  3. We store it in result and print later.

## DAY FIFTEEN

### Data Structures: Lists

- Lists are like containers that hold multiple items in one variable. Lists are __Ordered__ meaning each item has its own position, Lists are __Mutable__ meaning you can change the contents inside and Lists can __hold different data types__.

  fruits = ["apple", "banana", "cherry", ]
  print(fruits[0])  #This prints "apple"
  print(fruits[2])  #This prints "cherry"
  print(fruits[1])  #This prints "banana"
  print(fruits[-1])  #This prints "cherry"

- Each item's position is called an __index__. Positive inddexing starts from _[0]_ while negaative indexing starts from _[-1]_.
- Common methods include:
  1. __list.append(x)__: Add an item to the end of the list. Similar to _a[len(a):] = [x]_
  2. __list.extend(iterable)__: Extend the list by appending all the items from the iterable.
  3.__list.insert(index, x)__: Insert an item at a given position/index. The first argument is the index of the element before which to insert.
  4. __list.remove(x)__: Remove the first item whose value is equal to x, it raises a value error if no such item is found.
  5. __list.pop([index])__: Removes the item at the given position and return it. If no index is specified, _list.pop()_, removes the last item on the list.
  6. __list.clear()__: Removes all items on the list similar to _del a[:]_.

#### Using lists as a Stack

- The list methods make it easy to use a list as a stack, where _the last element added is the first element retrieved_ (Last-in, first-out). To add an item to the top use __list.append(x)__ an to retrieve an item from the top of the stack use __list.pop()__

#### Using Lists as queues

- It is also possible to use a list as a queue. where _the frist element added is the first element retrieved_ (first-in, first-out). However, lists are not as efficient for this purpose because doing inserts and pops from the begininng of a list is slow, since all other elements have to be shifted one by one. To implement a queue, use _collections.deque_
  - _from collections import deque_
  - _queue = deque(["Eric", "Martin", "James",])_
  - _queue.append("Terry") #Terry arrives_
  - _queue.append("Graham") #Graham arrives_
  - _queue.popleft() # Eric the first to arrive now leaves_
  - _queue.popleft() # Martin the second to arrive now leaves_

#### List Comprehensions

- List comprehensions provide a concise way to create lists. A short and elegant way.
- Instead of writing loops line by line, you can generate lists in one line

- structure:
  - [expression for item in iterable if condition]

  1. __expression__: _What to do with each item e.g square it, double it, convert it._
  2. __item__: _Each item in the iterable(like a loop variable)._
  3. __iterable__: _Something you loop over (list, tuple, string e.t.c)_
  4. __If condition(_optional_)__: _Filter items based on a rule._

- A common application for list comprehensions is to make a new list where each element is a result of some operation applied to each item of another sequence/iterable. OR create a subsequence of those elements that satisfy a certain condition

    numbers = [1, 2, 3, 4, 5]
    squares = [number**2 for number in numbers]
    print(squares) # [1, 4, 9, 16, 25]

    numbers = [1, 2, 3, 4, 5, 6]
    evens = [n for n in numbers if n % 2 == 0]
    print(evens) # [2, 4, 6]

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
