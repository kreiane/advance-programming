import tkinter as tk
from tkinter import filedialog

class CharacterCounterApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Character Counter App")

        self.create_widgets()

    def create_widgets(self):
        # Create labels and entry for user input
        tk.Label(self.master, text="Enter a character:").pack(pady=5)
        self.char_entry = tk.Entry(self.master, width=5)
        self.char_entry.pack(pady=5)

        # Create buttons
        tk.Button(self.master, text="Open File", command=self.open_file).pack(pady=10)
        tk.Button(self.master, text="Count Occurrences", command=self.count_occurrences).pack(pady=10)

        # Display result
        self.result_label = tk.Label(self.master, text="")
        self.result_label.pack(pady=10)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            self.file_path = file_path
            tk.messagebox.showinfo("File Opened", "File opened successfully!")

    def count_occurrences(self):
        if hasattr(self, 'file_path'):
            with open(self.file_path, 'r') as file:
                content = file.read()

            char_to_count = self.char_entry.get()

            if char_to_count:
                count = content.count(char_to_count)
                result_text = f'The character "{char_to_count}" appears {count} times in the file.'
                self.result_label.config(text=result_text)
            else:
                tk.messagebox.showwarning("Missing Character", "Please enter a character.")
        else:
            tk.messagebox.showwarning("File Not Opened", "Please open a file first.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CharacterCounterApp(root)
    root.mainloop()