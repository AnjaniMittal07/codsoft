# Simple To-Do List in Python

def show_menu():
    print("\nTo-Do List Menu")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append({'task': task, 'completed': False})
    print(f"Task '{task}' added.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks):
            status = "Completed" if task['completed'] else "Pending"
            print(f"{i + 1}. {task['task']} - {status}")

def mark_task_completed(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter the task number to mark as completed: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks[task_num]['completed'] = True
        print(f"Task '{tasks[task_num]['task']}' marked as completed.")
    else:
        print("Invalid task number.")

def delete_task(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_num < len(tasks):
        removed_task = tasks.pop(task_num)
        print(f"Task '{removed_task['task']}' deleted.")
    else:
        print("Invalid task number.")

def main():
    tasks = []
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_completed(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()
