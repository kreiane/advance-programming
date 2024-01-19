import tkinter as tk
from tkinter import messagebox

class Employee:
    def __init__(self):
        self.name = ""
        self.position = ""
        self.salary = 0.0
        self.id = 0

    def setData(self, name, position, salary, employee_id):
        self.name = name
        self.position = position
        self.salary = salary
        self.id = employee_id

    def getData(self):
        return f"{self.name}\t{self.position}\t{self.salary}\t{self.id}"

class EmployeeGUI:
    def __init__(self, master):
        self.master = master
        master.title("Employee Information")

        self.employees = []

        self.add_button = tk.Button(master, text="Add Employee Details", command=self.add_employee_details)
        self.add_button.pack()

        self.display_button = tk.Button(master, text="Display Employee Details", command=self.display_employee_details)
        self.display_button.pack()

    def add_employee_details(self):
        for i in range(5):
            name = input(f"Enter name for Employee {i + 1}: ")
            position = input(f"Enter position for Employee {i + 1}: ")
            salary = float(input(f"Enter salary for Employee {i + 1}: "))
            employee_id = i + 1

            employee = Employee()
            employee.setData(name, position, salary, employee_id)

            self.employees.append(employee)

        messagebox.showinfo("Employee Details Added", "Details for 5 employees added successfully.")

    def display_employee_details(self):
        print("\nName\tPosition\tSalary\tID")

        for employee in self.employees:
            print(employee.getData())

root = tk.Tk()
employee_gui = EmployeeGUI(root)
root.mainloop()