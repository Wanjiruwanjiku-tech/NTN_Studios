# Simple to-do list App - console version

tasks = [] # Empty list to store tasks

def show_menu():
    print("\n--- To-Do List App ---")
    print("1. View tasks")
    print("2. Add a tasks")
    print("3. Remove a tasks")
    print("4. Exit")

def view_tasks():
    if len(tasks) == 0:
        print("No tasks yet!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter your new task: ")
    tasks.append(task)
    print(f"Task '{task}' added.")

def remove_task():
    view_tasks()
    try:
        task_num = int(input("Enter the task number to remove: "))
        removed = tasks.pop(task_num - 1)
        print(f"Task '{removed}' removed.")

    except (ValueError, IndexError):
        print("Invalid task number.")

while True:
    try:
        show_menu()
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-4")
    except ValueError:
        print("Invalid choice. Please use 1-4")