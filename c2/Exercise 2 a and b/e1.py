import tkinter as tk

class ResizableApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Resizable App")
        
        # Label A (top, expands horizontally)
        label_a = tk.Label(root, text="Label A", bg="red")
        label_a.pack(side="top", fill="x", expand=True)

        # Labels C and D (middle side by side)
        frame_cd = tk.Frame(root, bg="blue")
        frame_cd.pack(side="top", fill="both", expand=False)

        label_c = tk.Label(root, text="Label C", bg="blue", width=20, height=2, bd=5)
        label_c.pack(side="left", fill="none", expand=False, padx=5)

        label_d = tk.Label(frame_cd, text="Label D", bg="white", width=10)
        label_d.pack(side="right", fill="none", expand=False)

        # Label B (bottom, fixed)
        label_b = tk.Label(root, text="Label B", bg="yellow")
        label_b.pack(side="top", fill="none", expand=False)

if __name__ == "__main__":
    root = tk.Tk()
    app = ResizableApp(root)
    root.mainloop()