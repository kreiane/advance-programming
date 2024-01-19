import tkinter as tk

class LoginPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Page")

        tk.Label(root, text="Username:").grid(row=0, column=0, padx=10, pady=10)
        self.username_entry = tk.Entry(root)
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=10)
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)

        login_button = tk.Button(root, text="Login", command=self.login)
        login_button.grid(row=2, column=1, pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "user" and password == "pass":
            print("Login successful")
        else:
            print("Login failed")

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginPage(root)
    root.mainloop()