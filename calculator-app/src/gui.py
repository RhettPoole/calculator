import tkinter as tk
from calculator import add, subtract, multiply, divide

class CalculatorApp:
    # "self" reference to current instance of the class, "root" represents the main window of our tkinter application.
    def __init__(self, root):
        self.root = root
        self.root.title("My first Calculator")

        # Create an entry widget to take user input and display the result
        self.entry = tk.Entry(root, width=16, font=("Arial", 24), borderwidth=2, relief="solid")
        self.entry.grid(row=0, column=0, columnspan=5)

        # Create a text widget to display the history of calculations
        self.history = tk.Text(root, height=10, width=40, font=("Arial", 12), state=tk.DISABLED)
        self.history.grid(row=6, column=0, columnspan=4)

        # Create buttons using a list
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+', 'C'
        ]

        row_val = 1
        col_val = 0
        for button in buttons:
            # lambda is used to create an anonymous function, common in GUI programming
            action = lambda x=button: self.click_event(x)
            tk.Button(root, text=button, width=5, height=2, font=("Arial", 18), command=action).grid(row=row_val, column=col_val)
                      # This section handles the structure of our grid to form buttons in the calculater
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def click_event(self, key):
        # Handle click event for each button
        if key == '=':
            try:
                # Evaluate the expression and display the result to the user, and store it for the user to see after completing currnent calculation
                expression = self.entry.get()
                result = eval(self.entry.get())
                # Delete what is currently displayed to the user
                self.entry.delete(0, tk.END)
                # Insert the result into the entry widget
                self.entry.insert(tk.END, str(result))
                # Append the expression and result to the history text widget
                self.history.config(state=tk.NORMAL)
                self.history.insert(tk.END, f"{expression} = {result}\n")
                self.history.config(state=tk.DISABLED)
            except Exception as e:
                # Display an error message if an exception occurs
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif key == 'C':
            # Clear the entry widget
            self.entry.delete(0, tk.END)
        elif key in ('+', '-', '*', '/'):
            # Add the operator to the entry widget
            self.entry.insert(tk.END, key)
        else:
            # Add the number or decimal point to the entry widget
            self.entry.insert(tk.END, key)

if __name__ == "__main__":
    root = tk.Tk() # Create the main window
    app = CalculatorApp(root) # Pass the main window to the CalculatorApp class
    root.mainloop() # Start the main event loop of the application