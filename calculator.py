import tkinter as tk

# Function to update the display
def click(button):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(button))

# Function to clear the display
def clear():
    entry.delete(0, tk.END)

# Function to evaluate the expression
def evaluate():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Main application window
root = tk.Tk()
root.title("Casio-Style Calculator")
root.geometry("342x354")
root.resizable(True,True)
root.configure(bg="#666666")  # light grey background for the calculator

# Display Entry
entry = tk.Entry(root, width=17, font=('Arial', 24), bd=15, insertwidth=2, bg="#ffffff", fg="#000000", justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Button styling
button_font = ('Arial', 18)
button_bg = "#333333"  # Dark grey for buttons
button_fg = "#000000"  # Black text on buttons
button_active_bg = "#A2BBCF"  # blue when button is active

# Create button function for layout
def create_button(text, row, col, width=1, height=1, command=None):
    button = tk.Button(root, text=text, padx=20, pady=20, width=width, height=height, font=button_font, bg=button_bg,
                       fg=button_fg, activebackground=button_active_bg, command=command)
    button.grid(row=row, column=col)

# Numeric buttons
create_button('7', 1, 0, command=lambda: click('7'))
create_button('8', 1, 1, command=lambda: click('8'))
create_button('9', 1, 2, command=lambda: click('9'))
create_button('4', 2, 0, command=lambda: click('4'))
create_button('5', 2, 1, command=lambda: click('5'))
create_button('6', 2, 2, command=lambda: click('6'))
create_button('1', 3, 0, command=lambda: click('1'))
create_button('2', 3, 1, command=lambda: click('2'))
create_button('3', 3, 2, command=lambda: click('3'))
create_button('0', 4, 0, width=1, command=lambda: click('0'))  # Double width for '0'

# Operation buttons
create_button('+', 1, 3, command=lambda: click('+'))
create_button('-', 2, 3, command=lambda: click('-'))
create_button('*', 3, 3, command=lambda: click('*'))
create_button('/', 4, 3, command=lambda: click('/'))

# Special buttons
create_button('C', 4, 2, command=clear)
create_button('=', 4, 1, command=evaluate)

# Run the application
root.mainloop()
