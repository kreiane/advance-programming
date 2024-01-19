
import tkinter as tk

class PackLayoutApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pack Layout App")

        left_frame = tk.Frame(root, bd=5, relief=tk.SOLID)
        left_frame.pack(side="left", fill="both", expand=True)

        label_a = tk.Label(left_frame, text="Label A", bg="grey", width=20, height=2, bd=5)
        label_a.pack(side="top", fill="both", expand=True)

        label_b = tk.Label(left_frame, text="Label B", bg="white", width=20, height=2, bd=5)
        label_b.pack(side="bottom", fill="both", expand=True)

        right_frame = tk.Frame(root, bd=5, relief=tk.SOLID)
        right_frame.pack(side="right", fill="both", expand=True)

        label_c = tk.Label(right_frame, text="Label C", bg="white", width=20, height=2, bd=5)
        label_c.pack(side="top", fill="both", expand=True)

        label_d = tk.Label(right_frame, text="Label D", bg="grey", width=20, height=2, bd=5)
        label_d.pack(side="bottom", fill="both", expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    app = PackLayoutApp(root)
    root.mainloop()