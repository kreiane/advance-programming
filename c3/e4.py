import tkinter as tk
from tkinter import ttk

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Shape Drawer")

        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack(padx=10, pady=10)

        shape_label = tk.Label(root, text="Select Shape:")
        shape_label.pack(pady=(0, 5))

        self.shape_var = tk.StringVar()
        shape_dropdown = ttk.Combobox(root, textvariable=self.shape_var, values=["Oval", "Rectangle", "Square", "Triangle"])
        shape_dropdown.pack(pady=(0, 10))
        shape_dropdown.set("Oval")

        coord_label = tk.Label(root, text="Enter Coordinates (comma-separated):")
        coord_label.pack(pady=(0, 5))

        self.coord_entry = tk.Entry(root)
        self.coord_entry.pack(pady=(0, 10))

        draw_button = tk.Button(root, text="Draw", command=self.draw_shape)
        draw_button.pack()

    def draw_shape(self):
        shape = self.shape_var.get().lower()
        coords_str = self.coord_entry.get()

        try:
            coords = [float(coord) for coord in coords_str.split(",")]
        except ValueError:
            tk.messagebox.showerror("Error", "Please enter valid numeric coordinates.")
            return

        if shape == "oval":
            self.canvas.create_oval(coords, outline="black", width=2)
        elif shape == "rectangle":
            self.canvas.create_rectangle(coords, outline="black", width=2)
        elif shape == "square":
            x1, y1, x2, y2 = coords
            side_length = min(x2 - x1, y2 - y1)
            self.canvas.create_rectangle(x1, y1, x1 + side_length, y1 + side_length, outline="black", width=2)
        elif shape == "triangle":
            if len(coords) != 6:
                tk.messagebox.showerror("Error", "Please enter three pairs of coordinates for a triangle.")
                return
            self.canvas.create_polygon(coords, outline="black", width=2)

if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()