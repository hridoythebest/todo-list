# Simple To-Do List

tasks = []  # Initialize an empty list to store tasks

def add_task(task):
    tasks.append(task)
    print("Task added successfully.")

def complete_task(task):
    if task in tasks:
        tasks.remove(task)
        print("Task marked as complete.")
    else:
        print("Task not found.")

def view_tasks():
    if tasks:
        print("Current tasks:")
        for task in tasks:
            print(" -", task)
    else:
        print("No tasks found.")

def main():
    print("Welcome to Simple To-Do List!")
    while True:
        print("\nOptions:")
        print("1. Add task")
        print("2. Mark task as complete")
        print("3. View tasks")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            task = input("Enter the task: ")
            add_task(task)
        elif choice == "2":
            task = input("Enter the task to mark as complete: ")
            complete_task(task)
        elif choice == "3":
            view_tasks()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
