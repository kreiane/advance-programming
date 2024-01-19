import tkinter as tk
from tkinter import messagebox

class PasswordCheckerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Checker App")

        self.attempts_left = 5

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="Enter Password:").pack(pady=5)
        self.password_entry = tk.Entry(self.master, show="*")
        self.password_entry.pack(pady=5)

        tk.Button(self.master, text="Submit", command=self.check_password).pack(pady=10)

        self.attempts_label = tk.Label(self.master, text=f"Attempts left: {self.attempts_left}")
        self.attempts_label.pack(pady=5)

    def check_password(self):
        password = self.password_entry.get()

        if self.validate_password(password):
            messagebox.showinfo("Password Valid", "Password is valid!")
            self.master.destroy()
        else:
            self.attempts_left -= 1
            self.attempts_label.config(text=f"Attempts left: {self.attempts_left}")

            if self.attempts_left == 0:
                messagebox.showwarning("Authorities Alerted", "Maximum attempts reached. Authorities have been alerted!")
                self.master.destroy() 
            else:
                messagebox.showwarning("Invalid Password", f"Invalid password! Attempts left: {self.attempts_left}")

    def validate_password(self, password):
        if (any(c.islower() for c in password) and
            any(c.isdigit() for c in password) and
            any(c.isupper() for c in password) and
            any(c in ['$', '#', '@'] for c in password) and
            6 <= len(password) <= 12):
            return True
        else:
            return False

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordCheckerApp(root)
    root.mainloop()