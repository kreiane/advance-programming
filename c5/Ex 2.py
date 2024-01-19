import tkinter as tk
from tkinter import messagebox

class Students:
    def __init__(self, name, mark1, mark2, mark3):
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

    def calcGrade(self):
        average = (self.mark1 + self.mark2 + self.mark3) / 3
        return average

    def display(self):
        return f"Student Name: {self.name}\nGrade Average: {self.calcGrade():.2f}"

class StudentGUI:
    def __init__(self, master):
        self.master = master
        master.title("Student Information")

        self.student1 = Students("John Doe", 85, 90, 78)

        self.label_student1 = tk.Label(master, text=self.student1.display())
        self.label_student1.pack()

        self.input_button = tk.Button(master, text="Enter Student 2 Data", command=self.get_user_input)
        self.input_button.pack()

    def get_user_input(self):
        name = input("Enter Student 2 Name: ")
        mark1 = int(input("Enter Mark 1 for Student 2: "))
        mark2 = int(input("Enter Mark 2 for Student 2: "))
        mark3 = int(input("Enter Mark 3 for Student 2: "))

        self.student2 = Students(name, mark1, mark2, mark3)

        self.label_student2 = tk.Label(self.master, text=self.student2.display())
        self.label_student2.pack()

root = tk.Tk()
student_gui = StudentGUI(root)
root.mainloop()