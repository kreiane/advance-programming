import tkinter as tk
from tkinter import ttk

class Shape:
    def __init__(self):
        self.sides = []

    def inputSides(self):
        pass

    def area(self):
        pass

class Circle(Shape):
    def inputSides(self):
        radius = float(input("Enter the radius of the circle: "))
        self.sides = [radius]

    def area(self):
        return 3.14 * self.sides[0] ** 2

class Rectangle(Shape):
    def inputSides(self):
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        self.sides = [length, width]

    def area(self):
        return self.sides[0] * self.sides[1]

class Triangle(Shape):
    def inputSides(self):
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        self.sides = [base, height]

    def area(self):
        return 0.5 * self.sides[0] * self.sides[1]

class ShapeCalculatorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Shape Area Calculator")

        self.shape_var = tk.StringVar()
        self.shape_var.set("Select Shape")

        self.label_shape = tk.Label(master, text="Select a Shape:")
        self.label_shape.pack()

        self.shape_menu = ttk.Combobox(master, textvariable=self.shape_var, values=("Circle", "Rectangle", "Triangle"))
        self.shape_menu.pack()

        self.button_select = tk.Button(master, text="Select Shape", command=self.select_shape)
        self.button_select.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    def select_shape(self):
        selected_shape = self.shape_var.get()

        if selected_shape == "Select Shape":
            self.result_label.config(text="Please select a valid shape.")
            return

        shape_object = self.get_shape_object(selected_shape)
        shape_object.inputSides()

        area_result = shape_object.area()

        self.result_label.config(text=f"Area of {selected_shape}: {area_result:.2f}")

    def get_shape_object(self, shape_name):
        if shape_name == "Circle":
            return Circle()
        elif shape_name == "Rectangle":
            return Rectangle()
        elif shape_name == "Triangle":
            return Triangle()

root = tk.Tk()
calculator_gui = ShapeCalculatorGUI(root)
root.mainloop()