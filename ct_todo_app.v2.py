# This is version two of the to do app.  It is more interesting and has better practices.
# This includes:
# Timestamps for tasks
# Better error checking on empty task lists
# Function to sort tasks by status or creation time
# Data persistence by saving tasks to a file
# Task Priority and Due Date
# Color-coded status display
# UX/UI improvements- including using Unicode symbols for status display to make it more visually appealing.
# A hidden joke.

import json
from datetime import datetime

# Data structure to store tasks
tasks = []

# File to save tasks
TASKS_FILE = "tasks.json"

# Load tasks from file
def load_tasks():
    """Load tasks from the tasks file."""
    global tasks
    try:
        with open(TASKS_FILE, "r") as file:
            tasks = json.load(file)
        print("Tasks loaded successfully.")
    except FileNotFoundError:
        print("No saved tasks found. Starting fresh.")
    except json.JSONDecodeError:
        print("Error reading tasks file. Starting fresh.")

# Save tasks to file
def save_tasks():
    """Save tasks to the tasks file."""
    try:
        with open(TASKS_FILE, "w") as file:
            json.dump(tasks, file)
        print("Tasks saved successfully.")
    except Exception as e:
        print(f"Error saving tasks: {e}")

# Display menu
def display_menu():
    """Display the main menu."""
    print("\n" + "*" * 30)
    print(f"{'To-Do List App':^30}")
    print("*" * 30)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task As Complete")
    print("4. Delete Task")
    print("5. Sort Tasks")
    print("6. Exit")
    print("*" * 30)

# Function to add a task
def add_task():
    """Add a task to the to-do list."""
    title = input("Enter Task Title: ").strip()
    if not title:
        print("Task title cannot be empty.")
        return

    if any(task['title'] == title for task in tasks):
        print("This task already exists.")
        return

    priority = input("Enter Task Priority (Low/Medium/High): ").strip().capitalize()
    if priority not in {"Low", "Medium", "High"}:
        priority = "Medium"  # Default priority

    due_date = input("Enter Due Date (YYYY-MM-DD, optional): ").strip()
    if due_date:
        try:
            datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Skipping due date.")
            due_date = ""

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    tasks.append({"title": title, "done": False, "priority": priority, "due_date": due_date, "timestamp": timestamp})
    print("Task added.")

# Function to view tasks
def view_tasks():
    """Display all tasks."""
    if not tasks:
        print("No tasks to display. Add a task first.")
        return

    print("\nTasks")
    print("-" * 50)
    for i, task in enumerate(tasks, start=1):
        title = task["title"]
        status = "✔️ Done" if task["done"] else "❌ Not Done"
        priority = task["priority"]
        due_date = task.get("due_date", "No Due Date")
        timestamp = task["timestamp"]

        # Color-code status
        status_color = "\033[92m" if task["done"] else "\033[91m"  # Green for done, red for not done
        reset_color = "\033[0m"

        print(f"{i}. {title} - {status_color}{status}{reset_color} - Priority: {priority} - Due: {due_date} (Added: {timestamp})")
    print("-" * 50)

# Function to mark a task as complete
def mark_task_as_complete():
    """Mark a task as complete."""
    view_tasks()
    if not tasks:
        return

    task_number = get_task_number()
    if task_number is not None:
        tasks[task_number - 1]["done"] = True
        print("Task marked as complete.")

# Function to delete a task
def delete_task():
    """Delete a task from the to-do list."""
    view_tasks()
    if not tasks:
        return

    task_number = get_task_number()
    if task_number is not None:
        confirm = input(f"Are you sure you want to delete task '{tasks[task_number - 1]['title']}'? (y/n): ").lower()
        if confirm == 'y':
            tasks.pop(task_number - 1)
            print("Task deleted.")
        else:
            print("Task not deleted.")

# Helper function to get a valid task number
def get_task_number():
    """Prompt the user for a valid task number."""
    try:
        task_number = int(input("Enter task number: "))
        if 1 <= task_number <= len(tasks):
            return task_number
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
    return None

# Function to sort tasks
def sort_tasks():
    """Sort tasks by title, priority, or due date."""
    print("\nSort Options:")
    print("1. By Title")
    print("2. By Status (Done/Not Done)")
    print("3. By Priority (Low to High)")
    print("4. By Due Date (Earliest First)")
    choice = input("Choose a sort option (1-4): ").strip()

    if choice == "1":
        tasks.sort(key=lambda x: x["title"].lower())
        print("Tasks sorted by title.")
    elif choice == "2":
        tasks.sort(key=lambda x: (x["done"], x["title"].lower()))
        print("Tasks sorted by status.")
    elif choice == "3":
        priority_order = {"Low": 0, "Medium": 1, "High": 2}
        tasks.sort(key=lambda x: priority_order[x["priority"]])
        print("Tasks sorted by priority.")
    elif choice == "4":
        tasks.sort(key=lambda x: x.get("due_date") or "9999-12-31")
        print("Tasks sorted by due date.")
    else:
        print("Invalid choice.")

# Function to tell a secret joke
def tell_joke():
    """Display a hidden joke."""
    print("\nWhy does Python live on land?")
    print("Because it's above C-level! 😂")
    print("I never said it was a good joke...")

# Main program
def main():
    """Main function to run the To-Do List application."""
    load_tasks()
    while True:
        display_menu()
        try:
            choice = input("Enter choice: ").strip()
            if choice == "1":
                add_task()
            elif choice == "2":
                view_tasks()
            elif choice == "3":
                mark_task_as_complete()
            elif choice == "4":
                delete_task()
            elif choice == "5":
                sort_tasks()
            elif choice == "42":  # Secret joke code
                tell_joke()
            elif choice == "6":
                save_tasks()
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print("An error occurred: ", e)

if __name__ == "__main__":
    main()
