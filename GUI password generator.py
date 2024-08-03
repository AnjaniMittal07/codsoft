import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(entry_length.get())
        if length <= 0:
            raise ValueError("Length must be a positive integer")
        
        characters = string.ascii_lowercase
        if var_uppercase.get():
            characters += string.ascii_uppercase
        if var_numbers.get():
            characters += string.digits
        if var_special.get():
            characters += string.punctuation
        
        if not characters:
            raise ValueError("At least one character type must be selected")

        password = ''.join(random.choice(characters) for _ in range(length))
        result_label.config(text=password)

    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.configure(bg='light blue')  # Set background color of the main window

# Create and place widgets
tk.Label(root, text="Password Length:", padx=10, pady=5, bg='light blue', fg='black').grid(row=0, column=0, padx=10, pady=5, sticky='e')
entry_length = tk.Entry(root, bg='white')
entry_length.grid(row=0, column=1, padx=10, pady=5)

var_uppercase = tk.BooleanVar()
tk.Checkbutton(root, text="Include Uppercase Letters", variable=var_uppercase, bg='light blue', fg='black').grid(row=1, columnspan=2, padx=10, pady=5, sticky='w')

var_numbers = tk.BooleanVar()
tk.Checkbutton(root, text="Include Numbers", variable=var_numbers, bg='light blue', fg='black').grid(row=2, columnspan=2, padx=10, pady=5, sticky='w')

var_special = tk.BooleanVar()
tk.Checkbutton(root, text="Include Special Characters", variable=var_special, bg='light blue', fg='black').grid(row=3, columnspan=2, padx=10, pady=5, sticky='w')

tk.Button(root, text="Generate Password", command=generate_password, bg='lightgreen').grid(row=4, columnspan=2, pady=10)

tk.Label(root, text="Generated Password:", padx=10, pady=5, bg='light blue', fg='black').grid(row=5, column=0, padx=10, pady=5, sticky='e')
result_label = tk.Label(root, text="", font=('Helvetica', 16, 'bold'), fg='blue', bg='white')  # Bold and larger font
result_label.grid(row=5, column=1, padx=10, pady=5)

# Run the application
root.mainloop()
