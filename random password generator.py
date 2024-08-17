import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate the password
def generate_password():
    length = length_var.get()
    
    # Validate the length input
    try:
        length = int(length)
        if length < 1:
            raise ValueError("Length must be a positive number.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid positive integer for the length.")
        return

    # Collect the characters based on user selection
    characters = ""
    if include_uppercase.get():
        characters += string.ascii_uppercase
    if include_lowercase.get():
        characters += string.ascii_lowercase
    if include_numbers.get():
        characters += string.digits
    if include_special.get():
        characters += string.punctuation

    if not characters:
        messagebox.showerror("Invalid Selection", "Please select at least one character type.")
        return

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    result_var.set(password)

# Main application window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.configure(bg="#2C3E50")  # Dark blue background

# Variables
length_var = tk.StringVar()
result_var = tk.StringVar()
include_uppercase = tk.BooleanVar(value=True)
include_lowercase = tk.BooleanVar(value=True)
include_numbers = tk.BooleanVar(value=True)
include_special = tk.BooleanVar(value=True)

# Labels and Entry
tk.Label(root, text="Password Length:", font=('Arial', 14), fg="#ECF0F1", bg="#2C3E50").pack(pady=10)
tk.Entry(root, textvariable=length_var, font=('Arial', 14), width=15).pack()

# Checkbuttons for character types
tk.Checkbutton(root, text="Include Uppercase (A-Z)", variable=include_uppercase, font=('Arial', 12), fg="#ECF0F1", bg="#2C3E50").pack(anchor='w')
tk.Checkbutton(root, text="Include Lowercase (a-z)", variable=include_lowercase, font=('Arial', 12), fg="#ECF0F1", bg="#2C3E50").pack(anchor='w')
tk.Checkbutton(root, text="Include Numbers (0-9)", variable=include_numbers, font=('Arial', 12), fg="#ECF0F1", bg="#2C3E50").pack(anchor='w')
tk.Checkbutton(root, text="Include Special Characters (@, #, etc.)", variable=include_special, font=('Arial', 12), fg="#ECF0F1", bg="#2C3E50").pack(anchor='w')

# Generate Button
tk.Button(root, text="Generate Password", command=generate_password, font=('Arial', 14), bg="#3498DB", fg="#000000").pack(pady=20)

# Result Display
tk.Entry(root, textvariable=result_var, font=('Arial', 14), width=30, bd=0, state='readonly', readonlybackground="#FFFFFF", fg="#000000").pack(pady=10)

# Run the application
root.mainloop()
