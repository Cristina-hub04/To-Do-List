import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from datetime import datetime

# Define the filename for saving tasks
TASKS_FILENAME = "tasks.json"

# Load tasks from a JSON file
def load_tasks():
    if os.path.exists(TASKS_FILENAME):
        with open(TASKS_FILENAME, 'r') as f:
            return json.load(f)
    return []

# Save tasks to a JSON file
def save_tasks(tasks):
    with open(TASKS_FILENAME, 'w') as f:
        json.dump(tasks, f)

# Function to add a task
def add_task():
    task_text = task_entry.get()
    category = category_var.get()
    due_date = due_date_entry.get()

    if task_text:
        tasks.append({"task": task_text, "category": category, "completed": False, "due_date": due_date})
        save_tasks(tasks)
        update_task_list()
        task_entry.delete(0, tk.END)  # Clear the input box
        due_date_entry.delete(0, tk.END)  # Clear the due date
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# Function to delete selected tasks
def delete_task():
    selected_task_indices = [i for i, var in enumerate(check_vars) if var.get()]
    if not selected_task_indices:
        messagebox.showwarning("Warning", "Please select a task to delete.")
        return
    for index in reversed(selected_task_indices):  # Delete from the end to avoid index shifting
        del tasks[index]
        del check_vars[index]
    save_tasks(tasks)
    update_task_list()

# Function to update the frame with current tasks
def update_task_list():
    for widget in task_frame.winfo_children():
        widget.destroy()
    check_vars.clear()

    for task in tasks:
        var = tk.BooleanVar(value=task["completed"])
        check_vars.append(var)
        
        # Display task, category, and due date in a single line
        task_display_text = f'{task["task"]} - {task["category"]} (Due: {task["due_date"]})'
        checkbutton = tk.Checkbutton(task_frame, text=task_display_text, variable=var,
                                     onvalue=True, offvalue=False, 
                                     command=lambda v=var: mark_task_complete(v))
        checkbutton.pack(anchor='w', padx=5, pady=2)

# Function to mark task as completed
def mark_task_complete(var):
    index = check_vars.index(var)
    tasks[index]["completed"] = var.get()  # Update task status
    save_tasks(tasks)

# Function to filter tasks
def filter_tasks():
    category_filter = filter_category_var.get()
    filtered_tasks = [task for task in tasks if task["category"] == category_filter or category_filter == "All"]
    return filtered_tasks

# Function to apply filter and refresh display
def apply_filter():
    update_task_list(filter_tasks())

# Create the main application window
root = tk.Tk()
root.title("Enhanced Todo List with Categories, Due Dates, and Filtering")
root.geometry("450x600")
root.configure(bg="#E6F2FF")  # Light blue background color

# Load tasks from file
tasks = load_tasks()  # This will start empty if the JSON file is empty

# Define colors
bg_color = "#E6F2FF"  # Light blue
button_color = "#66B2FF"  # Bright blue
entry_bg = "#CCE5FF"  # Light blue for entry field

# Apply styles
style = ttk.Style(root)
style.configure("TButton", font=("Arial", 10, "bold"), background=button_color, foreground="white")
style.map("TButton", background=[("active", "#4C99D6")])

# Task entry widget
task_entry = tk.Entry(root, width=40, bg=entry_bg, fg="black", font=("Arial", 12))
task_entry.pack(pady=10)

# Category selection
category_label = tk.Label(root, text="Category:", bg=bg_color, font=("Arial", 10))
category_label.pack()
category_var = tk.StringVar(value="Personal")
category_dropdown = ttk.Combobox(root, textvariable=category_var, values=["Personal", "Work", "Urgent", "Other"])
category_dropdown.pack(pady=5)

# Due date entry
due_date_label = tk.Label(root, text="Due Date (YYYY-MM-DD):", bg=bg_color, font=("Arial", 10))
due_date_label.pack()
due_date_entry = tk.Entry(root, width=20, bg=entry_bg, fg="black", font=("Arial", 10))
due_date_entry.pack(pady=5)

# Buttons
add_button = ttk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

delete_button = ttk.Button(root, text="Delete Selected Task(s)", command=delete_task)
delete_button.pack(pady=5)

# Filter selection
filter_category_label = tk.Label(root, text="Filter by Category:", bg=bg_color, font=("Arial", 10))
filter_category_label.pack()
filter_category_var = tk.StringVar(value="All")
filter_category_dropdown = ttk.Combobox(root, textvariable=filter_category_var, values=["All", "Personal", "Work", "Urgent", "Other"])
filter_category_dropdown.pack(pady=5)
filter_button = ttk.Button(root, text="Apply Filter", command=apply_filter)
filter_button.pack(pady=5)

# Scrollable frame for tasks
task_frame = tk.Frame(root, bg=bg_color)
task_frame.pack(pady=10, fill='both', expand=True)

# Scrollbar for the task frame
canvas = tk.Canvas(task_frame, bg=bg_color)
scrollbar = ttk.Scrollbar(task_frame, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg=bg_color)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

# Packing the canvas and scrollbar
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# List to hold checkbox variables
check_vars = []

# Update the listbox with loaded tasks
update_task_list()

# Start the application
root.mainloop()
