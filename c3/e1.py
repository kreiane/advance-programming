import tkinter as tk
from tkinter import ttk

class GreetingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Greeting App")

        self.input_frame = tk.Frame(root, bg="lightblue", padx=10, pady=10)
        self.input_frame.grid(row=0, column=0, padx=10, pady=10)

        title_label = tk.Label(self.input_frame, text="Personalized Greeting", font=("Helvetica", 14, "bold"), fg="blue", bg="lightblue")
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

        self.name_entry = tk.Entry(self.input_frame)
        self.name_entry.grid(row=1, column=0, columnspan=2, pady=(0, 10))

        color_label = tk.Label(self.input_frame, text="Select Color:", bg="lightblue")
        color_label.grid(row=2, column=0, sticky="E")

        self.color_var = tk.StringVar()
        self.color_var.set("black") 
        color_dropdown = ttk.Combobox(self.input_frame, textvariable=self.color_var, values=["black", "red", "green", "blue"])
        color_dropdown.grid(row=2, column=1, pady=(0, 10))

        update_button = tk.Button(self.input_frame, text="Update Greeting", command=self.update_greeting)
        update_button.grid(row=3, column=0, columnspan=2, pady=(10, 0))

        self.display_frame = tk.Frame(root, bg="lightgreen", padx=10, pady=10)
        self.display_frame.grid(row=0, column=1, padx=10, pady=10)

        self.greeting_label = tk.Label(self.display_frame, text="", font=("Helvetica", 12), bg="lightgreen")
        self.greeting_label.pack()

    def update_greeting(self):
        name = self.name_entry.get()
        selected_color = self.color_var.get()
        greeting_text = f"Hello, {name}!"

        self.greeting_label.config(text=greeting_text, fg=selected_color)


if __name__ == "__main__":
    root = tk.Tk()
    app = GreetingApp(root)
    root.mainloop()