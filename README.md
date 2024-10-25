# CLI Task Tracker
A command-line interface (CLI) task tracker that simplifies task management by allowing you to add, view, update, and track the status of your tasks efficiently.


## Features:
- **Add New Tasks**: Easily add tasks with descriptions to your task list.
- **View All Tasks**: List all tasks with their current status (`todo`, `in-progress`, or `done`).
- **Update Task Status**: Update the status of individual tasks.
- **Task Creation Timestamps**: Track when each task was created, along with updates if they occur.
- **Persistent Storage**: Keeps track of all tasks between sessions using JSON storage (`task.json`).

| Command             | Description                                           |
|---------------------|-------------------------------------------------------|
| `add`              | Create new task and saves it to JSON file              |
| `current-status`   | Create a table that displays the current status        |
| `delete`           | Delete an existing task                                |
| `mark-done`        | Change task state to done                              |
| `mark-in-progress` | Change task state to in-progress                       |
| `show-done`        | Display table with tasks in state 'done'               |
| `show-in-progress` | Display table with tasks in state 'in-progress'        |
| `show-todo`        | Display table with tasks in state 'todo'               |
| `update`           | Update an existing task                                |

---
## Installation:

To run the CLI Task Tracker on your local machine, ensure you have Python installed. Follow these steps:

1. Clone the Repository:
```bash
git clone https://github.com/yourusername/cli-task-tracker.git
cd cli-task-tracker
```
2. Install Dependencies: Use the requirements file to install dependencies.:
```bash
pip install -r requirements.txt
```
3. Run the Application: Start the CLI Task Tracker with:
```bash
task-cli add '.....' to add whatever task you need
```

---

## Usage:
After starting the application, you can use commands to interact with your tasks:

- Add Task: Add a new task by specifying the task description.
- List Tasks: View all tasks with their IDs, descriptions, and statuses.
- Update Task Status: Change a task’s status (e.g., todo to in-progress).

For more specific usage, refer to the command help:
```bash
python main.py --help
```

---
## Development:
For developers looking to contribute or modify the application:

- Code is modularized in Python files (e.g., main.py and os_handler.py).
- Use the setup.py to configure additional dependencies if needed.