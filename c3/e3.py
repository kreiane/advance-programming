import tkinter as tk
from tkinter import ttk, messagebox
import math

class GeometryCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Geometry Calculator")

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(padx=10, pady=10)

        self.add_circle_tab()
        self.add_square_tab()
        self.add_rectangle_tab()

    def add_circle_tab(self):
        circle_tab = ttk.Frame(self.notebook)
        self.notebook.add(circle_tab, text="Circle")

        radius_label = tk.Label(circle_tab, text="Enter Radius:")
        radius_label.grid(row=0, column=0, padx=10, pady=10)

        radius_entry = tk.Entry(circle_tab)
        radius_entry.grid(row=0, column=1, padx=10, pady=10)

        calculate_button = tk.Button(circle_tab, text="Calculate Area", command=lambda: self.calculate_circle_area(radius_entry.get()))
        calculate_button.grid(row=1, column=0, columnspan=2, pady=10)

    def add_square_tab(self):
        square_tab = ttk.Frame(self.notebook)
        self.notebook.add(square_tab, text="Square")

        side_label = tk.Label(square_tab, text="Enter Side Length:")
        side_label.grid(row=0, column=0, padx=10, pady=10)

        side_entry = tk.Entry(square_tab)
        side_entry.grid(row=0, column=1, padx=10, pady=10)

        calculate_button = tk.Button(square_tab, text="Calculate Area", command=lambda: self.calculate_square_area(side_entry.get()))
        calculate_button.grid(row=1, column=0, columnspan=2, pady=10)

    def add_rectangle_tab(self):
        rectangle_tab = ttk.Frame(self.notebook)
        self.notebook.add(rectangle_tab, text="Rectangle")

        length_label = tk.Label(rectangle_tab, text="Enter Length:")
        length_label.grid(row=0, column=0, padx=10, pady=10)

        width_label = tk.Label(rectangle_tab, text="Enter Width:")
        width_label.grid(row=1, column=0, padx=10, pady=10)

        length_entry = tk.Entry(rectangle_tab)
        length_entry.grid(row=0, column=1, padx=10, pady=10)

        width_entry = tk.Entry(rectangle_tab)
        width_entry.grid(row=1, column=1, padx=10, pady=10)

        calculate_button = tk.Button(rectangle_tab, text="Calculate Area", command=lambda: self.calculate_rectangle_area(length_entry.get(), width_entry.get()))
        calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

    def calculate_circle_area(self, radius):
        try:
            radius = float(radius)
            area = math.pi * radius ** 2
            messagebox.showinfo("Result", f"The area of the circle is: {area:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid radius.")

    def calculate_square_area(self, side):
        try:
            side = float(side)
            area = side ** 2
            messagebox.showinfo("Result", f"The area of the square is: {area:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid side length.")

    def calculate_rectangle_area(self, length, width):
        try:
            length = float(length)
            width = float(width)
            area = length * width
            messagebox.showinfo("Result", f"The area of the rectangle is: {area:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid length and width values.")


if __name__ == "__main__":
    root = tk.Tk()
    app = GeometryCalculator(root)
    root.mainloop()