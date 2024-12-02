#To do List appp version 1- the boring version.  Look at version 2 for a more interesting version with better practices.
# Data structure to store tasks
tasks = []

#Menu Display

def display_menu():
    print('*'*30)
    print("To Do List App")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task As Complete")
    print("4. Delete Task")
    print("5. Exit")
    print('*'*30)

#Function to add Task
def add_task():
    title = input("Enter Task Title: ").strip()
    if title:
        tasks.append({"title": title, "done": False})
        print("Task Added")
    else:
        print("Title cannot be empty")

#Function to view tasks
def view_tasks():
    print("Tasks")
    print("-"*30)
    for i, task in enumerate(tasks):
        title = task["title"]
        status = "Done" if task["done"] else "Not Done"
        print(f"{i+1}. {title} - {status}")
    print("-"*30)

    if not tasks:
        print("No tasks. Add a task")

#Function to mark task as complete

def mark_task_as_complete():
    view_tasks()
    if tasks:
        try:
            task_number = int(input("Enter task number: "))
            if 1 <= task_number <= len(tasks):
                task = tasks[task_number-1]
                task["done"] = True
                print("Task marked as complete")
            else:
                print("Invalid task number")
        except ValueError: 
            print("Please enter a valid task number")

#Function to delete task
def delete_task():
    view_tasks()
    if tasks:
        try:
            task_number = int(input("Enter task number: "))
            if 1 <= task_number <= len(tasks):
                tasks.pop(task_number-1)
                print("Task deleted")
            else:
                print("Invalid task number")
        except ValueError: 
            print("Please enter a valid task number")

#Main Program
def main():
    while True:
        display_menu()
        try:
            choice = input("Enter choice: ")
            if choice == '1':
                add_task()
            elif choice == '2':
                view_tasks()
            elif choice == '3':
                mark_task_as_complete()
            elif choice == '4':
                delete_task()
            elif choice == '5':
                print("\n--Good bye--\n")
                break
            else:
                print("Invalid choice. Please try again")
        
        except Exception as e:
            print("An error occurred: ", e)
       
if __name__ == "__main__":
    main()

