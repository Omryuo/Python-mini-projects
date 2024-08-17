import tkinter as tk
from tkinter import messagebox, font

# Function to add a task with a selected priority
def add_task():
    task = task_entry.get()
    priority = priority_var.get()
    if task:
        if priority == "High":
            tasks_listbox.insert(tk.END, f"🔥 {task}")
            tasks_listbox.itemconfig(tk.END, {'fg': 'red'})
        elif priority == "Medium":
            tasks_listbox.insert(tk.END, f"⚠ {task}")
            tasks_listbox.itemconfig(tk.END, {'fg': 'orange'})
        elif priority == "Low":
            tasks_listbox.insert(tk.END, f"⬇ {task}")
            tasks_listbox.itemconfig(tk.END, {'fg': 'green'})
        else:
            tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

# Function to delete the selected task
def delete_task():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        tasks_listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning", "You must select a task to delete.")

# Function to toggle the completion status of a task
def toggle_task_completion():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        task = tasks_listbox.get(selected_task_index)
        if task.startswith("✔ "):
            # Unmark task
            task = task[2:]
            tasks_listbox.delete(selected_task_index)
            tasks_listbox.insert(selected_task_index, task)
            tasks_listbox.itemconfig(selected_task_index, {'fg': 'black', 'font': task_font})
        else:
            # Mark task as completed
            task = "✔ " + task
            tasks_listbox.delete(selected_task_index)
            tasks_listbox.insert(selected_task_index, task)
            tasks_listbox.itemconfig(selected_task_index, {'fg': 'gray', 'font': completed_task_font})
    else:
        messagebox.showwarning("Warning", "You must select a task to mark/unmark.")

# Main application window
root = tk.Tk()
root.title("To-Do List")

# Color theme variables
bg_color = "#556B2F"  # Forest Green
button_color = "#8F9779"  # Moss Green
listbox_color = "#F5F5DC"  # Beige for better contrast

# Fonts for tasks
task_font = font.Font(family='Helvetica', size=12)
completed_task_font = font.Font(family='Helvetica', size=12, slant='italic')

# Configure window colors
root.configure(bg=bg_color)

# Task entry and add button
task_entry = tk.Entry(root, width=40, font=task_font)
task_entry.pack(pady=10)

priority_var = tk.StringVar(value="Normal")
priority_label = tk.Label(root, text="Set Priority:", bg=bg_color, font=task_font, fg="white")
priority_label.pack()

priority_frame = tk.Frame(root, bg=bg_color)
priority_frame.pack()

tk.Radiobutton(priority_frame, text="High", variable=priority_var, value="High", bg=bg_color, font=task_font, fg="white").pack(side=tk.LEFT, padx=5)
tk.Radiobutton(priority_frame, text="Medium", variable=priority_var, value="Medium", bg=bg_color, font=task_font, fg="white").pack(side=tk.LEFT, padx=5)
tk.Radiobutton(priority_frame, text="Low", variable=priority_var, value="Low", bg=bg_color, font=task_font, fg="white").pack(side=tk.LEFT, padx=5)
tk.Radiobutton(priority_frame, text="Normal", variable=priority_var, value="Normal", bg=bg_color, font=task_font, fg="white").pack(side=tk.LEFT, padx=5)

# Button font color adjusted for better visibility
add_task_button = tk.Button(root, text="Add Task", width=20, command=add_task, bg=button_color, fg="black", font=task_font)
add_task_button.pack(pady=5)

# Listbox to display tasks
tasks_listbox = tk.Listbox(root, width=50, height=15, font=task_font, selectbackground="lightgreen", bg=listbox_color)
tasks_listbox.pack(pady=10)

# Buttons for task actions
toggle_task_button = tk.Button(root, text="Mark/Unmark Task", width=20, command=toggle_task_completion, bg=button_color, fg="black", font=task_font)
toggle_task_button.pack(pady=5)

delete_task_button = tk.Button(root, text="Delete Task", width=20, command=delete_task, bg=button_color, fg="black", font=task_font)
delete_task_button.pack(pady=5)

# Adjusting padding for better appearance
root.configure(padx=20, pady=20)

root.mainloop()
