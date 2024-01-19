import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        self.entry_var = tk.StringVar()
        entry = tk.Entry(root, textvariable=self.entry_var, font=('Arial', 14), justify='right', bd=10, insertwidth=4, width=14)
        entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+'
        ]

        row_val, col_val = 1, 0
        for button in buttons:
            tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 14), command=lambda b=button: self.button_click(b)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def button_click(self, button):
        current_entry = self.entry_var.get()

        if button == 'C':
            self.entry_var.set('')
        elif button == '=':
            try:
                result = eval(current_entry)
                self.entry_var.set(result)
            except Exception as e:
                self.entry_var.set('Error')
        else:
            self.entry_var.set(current_entry + button)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()