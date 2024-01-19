import tkinter as tk

class FourLabelsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Four Labels GUI")

        # Label A
        label_a = tk.Label(root, text="A", bg="red", width=10, relief=tk.RIDGE)
        label_a.pack(fill="x", expand=True)

        # Label B
        label_b = tk.Label(root, text="B", bg="yellow", width=10, relief=tk.RAISED)
        label_b.pack(side="bottom", fill="none", expand=False)

        # Frame for Labels C and D (50% width each)
        frame1 = tk.Frame(root)
        frame1.pack(side="left", fill="x", expand=True)

        frame2 = tk.Frame(root)
        frame2.pack(side="left", fill="x", expand=True)
        # Label C
        label_c = tk.Label(frame1, text="C", bg="blue", width=10)
        label_c.pack(side="right", fill="none", expand=False)

        # Label D
        label_d = tk.Label(frame2, text="D", bg="white", width=10)
        label_d.pack(side="right", fill="none", expand=False)

if __name__ == "__main__":
    root = tk.Tk()
    app = FourLabelsGUI(root)
    root.mainloop()