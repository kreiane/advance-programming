import tkinter as tk
from tkinter import ttk

class ArithmeticOperations:
    def __init__(self):
        self.result = 0.0

    def calculate(self, operation, num1, num2):
        try:
            num1 = float(num1)
            num2 = float(num2)
            if operation == "Addition":
                self.result = num1 + num2
            elif operation == "Subtraction":
                self.result = num1 - num2
            elif operation == "Multiplication":
                self.result = num1 * num2
            elif operation == "Division":
                if num2 != 0:
                    self.result = num1 / num2
                else:
                    raise ValueError("Cannot divide by zero.")
        except ValueError as e:
            return str(e)

class CalculatorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Arithmetic Operations Calculator")

        self.arithmetic_operations = ArithmeticOperations()

        self.label_instruction = tk.Label(master, text="Select an operation:")
        self.label_instruction.grid(row=0, column=0, columnspan=2, pady=10)

        self.combobox_operations = ttk.Combobox(master, values=["Addition", "Subtraction", "Multiplication", "Division"])
        self.combobox_operations.grid(row=1, column=0, columnspan=2, pady=10)
        self.combobox_operations.set("Addition")

        self.label_num1 = tk.Label(master, text="Enter number 1:")
        self.label_num1.grid(row=2, column=0, pady=5)

        self.entry_num1 = tk.Entry(master)
        self.entry_num1.grid(row=2, column=1, pady=5)

        self.label_num2 = tk.Label(master, text="Enter number 2:")
        self.label_num2.grid(row=3, column=0, pady=5)

        self.entry_num2 = tk.Entry(master)
        self.entry_num2.grid(row=3, column=1, pady=5)

        self.button_calculate = tk.Button(master, text="Calculate", command=self.perform_calculation)
        self.button_calculate.grid(row=4, column=0, columnspan=2, pady=10)

        self.label_result = tk.Label(master, text="")
        self.label_result.grid(row=5, column=0, columnspan=2, pady=10)

    def perform_calculation(self):
        operation = self.combobox_operations.get()
        num1 = self.entry_num1.get()
        num2 = self.entry_num2.get()

        result = self.arithmetic_operations.calculate(operation, num1, num2)

        if isinstance(result, float):
            self.label_result.config(text=f"Result: {result:.2f}")
        else:
            self.label_result.config(text=f"Error: {result}")

root = tk.Tk()
calculator_gui = CalculatorGUI(root)
root.mainloop()
