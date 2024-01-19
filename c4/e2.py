import tkinter as tk
from tkinter import filedialog

class StringCounterApp:
    def __init__(self, master):
        self.master = master
        self.master.title("String Counter App")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="Enter a string for free search:").pack(pady=5)
        self.search_entry = tk.Entry(self.master, width=40)
        self.search_entry.pack(pady=5)
        
        tk.Button(self.master, text="Open File", command=self.open_file).pack(pady=10)
        tk.Button(self.master, text="Count Strings", command=self.count_strings).pack(pady=10)

        self.result_label = tk.Label(self.master, text="")
        self.result_label.pack(pady=10)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            self.file_path = file_path
            tk.messagebox.showinfo("File Opened", "File opened successfully!")

    def count_strings(self):
        if hasattr(self, 'file_path'):
            with open(self.file_path, 'r') as file:
                content = file.read()

            search_string = self.search_entry.get().strip()
            if search_string:
                count = content.count(search_string)
                result_text = f'The string "{search_string}" appears {count} times.'
            else:
                strings_to_count = [
                    "Hello my name is Peter Parker",
                    "I love Python Programming",
                    "Love",
                    "Enemy"
                ]
                results = {string: content.count(string) for string in strings_to_count}
                result_text = "\n".join([f'{string}: {count}' for string, count in results.items()])

            self.result_label.config(text=result_text)
        else:
            tk.messagebox.showwarning("File Not Opened", "Please open a file first.")

if __name__ == "__main__":
    root = tk.Tk()
    app = StringCounterApp(root)
    root.mainloop()