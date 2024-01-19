import tkinter as tk
from tkinter import messagebox

class Animal:
    def __init__(self):
        self.Type = ""
        self.Name = ""
        self.Colour = ""
        self.Age = 0
        self.Weight = 0.0
        self.Noise = ""

    def sayHello(self):
        print(f"{self.Type} says: Hello, my name is {self.Name}.")

    def makeNoise(self):
        print(f"{self.Type} makes noise: {self.Noise}")

    def animalDetails(self):
        return f"Type: {self.Type}\nName: {self.Name}\nColour: {self.Colour}\nAge: {self.Age}\nWeight: {self.Weight}\nNoise: {self.Noise}"

class AnimalGUI:
    def __init__(self, master):
        self.master = master
        master.title("Animal Information")

        self.dog = Animal()
        self.cow = Animal()

        self.dog.Type = "Dog"
        self.dog.Name = "Buddy"
        self.dog.Colour = "Brown"
        self.dog.Age = 3
        self.dog.Weight = 25.5
        self.dog.Noise = "Woof"

        self.cow.Type = "Cow"
        self.cow.Name = "Daisy"
        self.cow.Colour = "Black and White"
        self.cow.Age = 5
        self.cow.Weight = 500.0
        self.cow.Noise = "Moo"

        self.button_dog = tk.Button(master, text="Dog Methods", command=self.invoke_dog_methods)
        self.button_dog.pack()

        self.button_cow = tk.Button(master, text="Cow Methods", command=self.invoke_cow_methods)
        self.button_cow.pack()

    def invoke_dog_methods(self):
        self.dog.sayHello()
        self.dog.makeNoise()
        messagebox.showinfo("Dog Details", self.dog.animalDetails())

    def invoke_cow_methods(self):
        self.cow.sayHello()
        self.cow.makeNoise()
        messagebox.showinfo("Cow Details", self.cow.animalDetails())

root = tk.Tk()
animal_gui = AnimalGUI(root)
root.mainloop()