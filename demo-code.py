import json

TASKS_FILE = "tasks.json"

def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(description):
    if not description.strip():
        print("Task description cannot be empty!")
        return
    tasks = load_tasks()
    tasks.append({"description": description, "completed": False})
    save_tasks(tasks)
    print("Task added successfully!")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, start=1):
            status = "✔" if task["completed"] else "✘"
            print(f"{i}. {task['description']} [{status}]")

def complete_task(index):
    tasks = load_tasks()
    if not tasks:
        print("No tasks available to complete.")
        return
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        save_tasks(tasks)
        print("Task marked as completed!")
    else:
        print("Invalid task number.")

def delete_task(index):
    tasks = load_tasks()
    if not tasks:
        print("No tasks available to delete.")
        return
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)
        print("Task deleted successfully!")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        if choice == "1":
            desc = input("Enter task description: ")
            add_task(desc)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            try:
                index = int(input("Enter task number to mark as complete: ")) - 1
                complete_task(index)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "4":
            try:
                index = int(input("Enter task number to delete: ")) - 1
                delete_task(index)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "5":
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
