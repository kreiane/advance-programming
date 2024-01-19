import tkinter as tk
from tkinter import messagebox

class BioInfoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Bio Information App")

        self.create_widgets()

    def create_widgets(self):
        # Create labels and entry widgets for user input
        tk.Label(self.master, text="Name:").grid(row=0, column=0, sticky='e')
        self.name_entry = tk.Entry(self.master)
        self.name_entry.grid(row=0, column=1, pady=5)

        tk.Label(self.master, text="Age:").grid(row=1, column=0, sticky='e')
        self.age_entry = tk.Entry(self.master)
        self.age_entry.grid(row=1, column=1, pady=5)

        tk.Label(self.master, text="Hometown:").grid(row=2, column=0, sticky='e')
        self.hometown_entry = tk.Entry(self.master)
        self.hometown_entry.grid(row=2, column=1, pady=5)

        # Create buttons
        tk.Button(self.master, text="Save to File", command=self.save_to_file).grid(row=3, column=0, columnspan=2, pady=10)
        tk.Button(self.master, text="Read from File", command=self.read_from_file).grid(row=4, column=0, columnspan=2, pady=10)

        # Display result
        self.result_label = tk.Label(self.master, text="")
        self.result_label.grid(row=5, column=0, columnspan=2, pady=10)

    def save_to_file(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        hometown = self.hometown_entry.get()

        if name and age and hometown:
            with open("bio.txt", "w") as file:
                file.write(f"Name: {name}\nAge: {age}\nHometown: {hometown}")

            self.result_label.config(text="Data saved to bio.txt")
        else:
            messagebox.showwarning("Incomplete Information", "Please enter Name, Age, and Hometown.")

    def read_from_file(self):
        try:
            with open("bio.txt", "r") as file:
                content = file.read()

            if content:
                self.result_label.config(text=content)
            else:
                self.result_label.config(text="No data found in bio.txt")
        except FileNotFoundError:
            self.result_label.config(text="bio.txt not found")

if __name__ == "__main__":
    root = tk.Tk()
    app = BioInfoApp(root)
    root.mainloop()