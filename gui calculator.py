import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = var_operation.get()

        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            if num2 == 0:
                raise ZeroDivisionError
            result = num1 / num2
        else:
            raise ValueError("Invalid operation")

        result_label.config(text=f"Result: {result:.2f}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")
    except ZeroDivisionError:
        messagebox.showerror("Math Error", "Cannot divide by zero.")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.configure(bg='orange') 

# Create and place widgets
tk.Label(root, text="Enter first number:", font=('Helvetica', 12, 'bold')).grid(row=0, column=0, padx=10, pady=5, sticky='e')
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Enter second number:", font=('Helvetica', 12, 'bold')).grid(row=1, column=0, padx=10, pady=5, sticky='e')
entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Select operation:").grid(row=2, column=0, padx=10, pady=5)
var_operation = tk.StringVar(value="Add")
operations = ["Add", "Subtract", "Multiply", "Divide"]
for op in operations:
    tk.Radiobutton(root, text=op, variable=var_operation, value=op).grid(row=2, column=operations.index(op) + 1, padx=5, pady=5)

tk.Button(root, text="Calculate", command=calculate).grid(row=3, columnspan=4, pady=10)
result_label = tk.Label(root, text="Result: ")
result_label.grid(row=4, columnspan=4, pady=5)

# Run the application
root.mainloop()
