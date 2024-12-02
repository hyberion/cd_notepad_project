---

# 📝 To-Do List App

A **simple and interactive command-line To-Do List application** built with Python. This app helps you manage your tasks effectively with features like priorities, due dates, sorting, and even a secret joke!

---

## 🚀 Features

- **Add Tasks**: Create tasks with optional priorities and due dates.
- **View Tasks**: See all tasks with their statuses, priorities, and due dates, displayed in a clean format with color-coded status indicators.
- **Mark Tasks as Complete**: Update a task's status to "Done" with a single command.
- **Delete Tasks**: Remove tasks from your list when they are no longer needed.
- **Sort Tasks**: Sort tasks by title, status, priority, or due date.
- **Data Persistence**: Your tasks are saved automatically to a file (`tasks.json`) and reloaded when you restart the app.
- **Secret Joke**: Discover a hidden joke by entering a special code. 😉
  
---

## 🎨 Color-Coded Status

- **❌ Not Done**: Shown in **red** for incomplete tasks.
- **✔️ Done**: Shown in **green** for completed tasks.

---

## 📥 Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/todo-list-app.git
   cd todo-list-app
   ```

2. **Install Python**:
   Ensure you have Python 3.7+ installed on your system. You can download it from [python.org](https://www.python.org/).

3. **Run the App**:
   ```bash
   python todo_list_app.py
   ```

---

## 🛠 Usage

When you run the app, you'll see the following menu:

```
******************************
          To-Do List App      
******************************
1. Add Task
2. View Tasks
3. Mark Task As Complete
4. Delete Task
5. Sort Tasks
6. Exit
******************************
```

### Menu Options:
1. **Add Task**:
   - Enter the task title.
   - Optionally, specify a priority (`Low`, `Medium`, `High`).
   - Optionally, provide a due date in `YYYY-MM-DD` format.

2. **View Tasks**:
   - See all tasks with their title, status, priority, due date, and creation timestamp.

3. **Mark Task As Complete**:
   - Select a task by its number to mark it as "Done."

4. **Delete Task**:
   - Select a task by its number to delete it from the list.

5. **Sort Tasks**:
   - Sort your tasks by:
     - Title (alphabetically)
     - Status (done/not done)
     - Priority (Low to High)
     - Due date (earliest first)

6. **Exit**:
   - Save your tasks to `tasks.json` and quit the app.

---

## 💾 Data Persistence

All tasks are saved automatically in a JSON file (`tasks.json`). When you restart the app, your tasks will be reloaded, so you can pick up where you left off.

---

## 🎉 Hidden Feature: The Secret Joke

Type `42` at the main menu to reveal a programmer's favorite joke. 🤫

---

## 🛡 Compatibility

- **Platforms**: Works on Linux, macOS, and Windows.
- **Terminal Support**: Ensure your terminal supports ANSI escape codes for color (e.g., PowerShell, macOS Terminal, or Windows Terminal).

---

## 📂 File Structure

```
todo-list-app/
├── tasks.json            # File to store tasks (auto-generated)
├── todo_list_app.py      # Main application script
├── README.md             # Documentation (this file)
```

---

## 👨‍💻 Contributing

Contributions are welcome! If you find bugs or want to add features, feel free to:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Submit a pull request.

---

## 📜 License

This project is licensed under the [WHY THE HELL NOT] Licence.
The proper benedictions have been performed.  The Machine spirt is appeased.

---

## ❤️ Acknowledgments

- Built with ❤️ , caffiene, and Python.
- The Emperor Protects

---

##### The machine god will be pleased ######
