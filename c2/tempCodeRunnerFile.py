import tkinter as tk

root = tk.Tk()

root.geometry("600x600")
root.resizable(False, False)
root.configure(bg="#E0F4FF")
root.title("Exercise 1")

label = tk.Label(root, text="Welcome to my GUI", font=('Arial', 18, 'bold'))
label.pack(pady=10)

root.mainloop()