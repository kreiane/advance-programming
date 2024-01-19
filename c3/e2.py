import tkinter as tk
from tkinter import ttk, messagebox

class CoffeeVendingMachine:
    def __init__(self, root):
        self.root = root
        self.root.title("Coffee Vending Machine")

        self.coffee_frame = tk.Frame(root, bg="lightblue", padx=10, pady=10)
        self.coffee_frame.grid(row=0, column=0, padx=10, pady=10)

        title_label = tk.Label(self.coffee_frame, text="Coffee Vending Machine", font=("Helvetica", 14, "bold"), fg="blue", bg="lightblue")
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

        coffee_label = tk.Label(self.coffee_frame, text="Select Coffee:", bg="lightblue")
        coffee_label.grid(row=1, column=0, sticky="E")

        self.coffee_var = tk.StringVar()
        self.coffee_var.set("Espresso")  
        coffee_dropdown = ttk.Combobox(self.coffee_frame, textvariable=self.coffee_var, values=["Espresso", "Latte", "Cappuccino"])
        coffee_dropdown.grid(row=1, column=1, pady=(0, 10))

        self.sugar_var = tk.BooleanVar()
        sugar_checkbox = tk.Checkbutton(self.coffee_frame, text="Sugar", variable=self.sugar_var, bg="lightblue")
        sugar_checkbox.grid(row=2, column=0, columnspan=2, pady=(0, 5), sticky="W")

        self.milk_var = tk.BooleanVar()
        milk_checkbox = tk.Checkbutton(self.coffee_frame, text="Milk", variable=self.milk_var, bg="lightblue")
        milk_checkbox.grid(row=3, column=0, columnspan=2, pady=(0, 10), sticky="W")

        self.money_frame = tk.Frame(root, bg="lightgreen", padx=10, pady=10)
        self.money_frame.grid(row=0, column=1, padx=10, pady=10)

        money_label = tk.Label(self.money_frame, text="Insert Money (in $):", bg="lightgreen")
        money_label.grid(row=0, column=0, sticky="E")

        self.money_entry = tk.Entry(self.money_frame)
        self.money_entry.grid(row=0, column=1, pady=(0, 10))

        buy_button = tk.Button(self.money_frame, text="Buy Coffee", command=self.buy_coffee)
        buy_button.grid(row=1, column=0, columnspan=2)

    def buy_coffee(self):
        coffee_type = self.coffee_var.get()
        sugar_option = "with Sugar" if self.sugar_var.get() else "without Sugar"
        milk_option = "with Milk" if self.milk_var.get() else "without Milk"
        money_inserted = self.money_entry.get()

        try:
            money_inserted = float(money_inserted)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount.")
            return

        price_map = {"Espresso": 2.0, "Latte": 3.0, "Cappuccino": 3.5}
        coffee_price = price_map.get(coffee_type, 0.0)

        if money_inserted < coffee_price:
            messagebox.showinfo("Insufficient Funds", f"Please insert at least ${coffee_price} to buy {coffee_type}.")
        else:
            change = money_inserted - coffee_price
            message = f"You have purchased a {coffee_type} coffee {sugar_option} {milk_option}.\n"
            message += f"Thank you! Your change is ${change:.2f}."
            messagebox.showinfo("Purchase Successful", message)


if __name__ == "__main__":
    root = tk.Tk()
    app = CoffeeVendingMachine(root)
    root.mainloop()