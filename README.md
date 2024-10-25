# To-Do-List
Enhanced Todo List Application

This is a user-friendly Todo List application built with Python and Tkinter, featuring task categories, due dates, and filtering options. Users can add tasks, mark them as completed, delete selected tasks, and filter tasks by category. The app is visually appealing and supports persistent storage of tasks.
Features

    Add Tasks: Enter new tasks along with categories and due dates.
    Completion Checkboxes: Mark tasks as completed using checkboxes.
    Delete Tasks: Select and delete one or multiple tasks at once.
    Task Categories: Organize tasks into categories (e.g., Personal, Work, Urgent, Other).
    Due Dates: Assign due dates to tasks for better organization.
    Filter by Category: Easily filter tasks to view specific categories.
    Persistent Storage: All tasks are saved locally in a tasks.json file and are loaded automatically each time the app starts.
    Scrollable Interface: If tasks exceed the window size, a scrollbar appears for easy navigation.

Technologies Used

    Python: Core programming language.
    Tkinter: For building the graphical interface.
    JSON: For saving and loading tasks to/from a file.

Installation and Setup
Requirements

    Python 3.x

Installation Steps

    Clone this repository or download the code files.

    Make sure Python 3 is installed on your system.

    Install Tkinter if it’s not installed (usually Tkinter is included with Python, but you can install it separately if needed).

    bash

# If Tkinter is not installed, you can install it with:
sudo apt-get install python3-tk

Run the todo_list_with_categories.py script:

bash

    python todo_list_with_categories.py

Usage

    Add a Task:
        Type a task in the input field.
        Select a category from the dropdown menu.
        Enter a due date (format: YYYY-MM-DD).
        Click "Add Task."

    Mark a Task as Completed: Click the checkbox next to a task to mark it as completed.

    Delete a Task:
        Select the task(s) you want to delete by checking them.
        Click "Delete Selected Task(s)."

    Filter Tasks:
        Select a category from the "Filter by Category" dropdown.
        Click "Apply Filter" to view tasks in that category.

    Close and Reopen: When you close and reopen the app, all tasks, their categories, due dates, and completion statuses will be restored.

File Structure

    todo_list_with_categories.py: The main script for the Todo List application.
    tasks.json: This file stores tasks, categories, due dates, and their completion statuses. It’s created automatically when the app runs.

Example Screenshot

(You can add a screenshot here if you’d like)
Future Improvements

Some features that could be added in the future include:

    Task Priorities: Allow users to set priority levels for tasks.
    Notifications: Implement reminders for tasks nearing their due dates.
    Search Functionality: Enable searching tasks by keywords or phrases.
