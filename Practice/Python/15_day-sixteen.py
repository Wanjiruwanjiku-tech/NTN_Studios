class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self): #Every instance needs a self
        print(f"Hello the car brand is: {self.brand} and the model is: {self.model}")

car1 = Car("Volvo", "2001")
car1.display_info()
print("-" * 40)

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return(f"{self.account_holder}: {self.balance}")
    
    def withdraw(self, amount):
        if self.balance < amount:
            return("Insufficient funds")
        else:
            self.balance -= amount
            return(f"{self.account_holder}: {self.balance}")

print("Natalie's Bank")
print("-" * 40)
account1 = BankAccount("Natalie", 6000)
print(f"\tDeposit\n{account1.deposit(5000)}")
print(f"\tWithdrawal\n{account1.withdraw(5000)}")
print("-" * 40)

account2 = BankAccount("Raphael", 1000)
print(f"\tDeposit\n{account2.deposit(5000)}")
print(f"\tWithdrawal\n{account2.withdraw(5000)}")

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def greeting(self):
        print(f"Hello {self.name}, welcome to the {self.grade} grade.")
    
    def student_list(self):
        student = []
        student.append(self.name)
        print(student)


while True:
    print("Welcome to the Salvatore's Boarding School")
    print("-" * 40)
    name = input("Enter your Name or 'exit' to quit: ")
    if name.lower() == 'exit':
        print("Exiting...")
        break

    grade = input("Enter your Grade or 'exit' to quit: ")
    if grade.lower() == 'exit':
        print("Exiting...")
        break

    student1 = Student(name, grade)
    student1.greeting()
    student1.student_list()
    print("-" * 40)
    print("\n")