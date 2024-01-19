import tkinter as tk
from tkinter import messagebox

class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def display_info(self):
        return f"Name: {self.name}\nAge: {self.age}\nBreed: {self.breed}"

    @classmethod
    def oldest_dog_woof(cls, dog1, dog2):
        oldest_dog = dog1 if dog1.age > dog2.age else dog2
        messagebox.showinfo("Oldest Dog Woof", f"{oldest_dog.name} (Age: {oldest_dog.age}) says Woof!")

class DogGUI:
    def __init__(self, master):
        self.master = master
        master.title("Dog Information")

        self.dog1 = Dog("Buddy", 5, "Labrador")
        self.dog2 = Dog("Max", 7, "Golden Retriever")

        self.label_dog1 = tk.Label(master, text=self.dog1.display_info())
        self.label_dog1.pack()

        self.label_dog2 = tk.Label(master, text=self.dog2.display_info())
        self.label_dog2.pack()

        self.woof_button = tk.Button(master, text="Oldest Dog Woof", command=self.oldest_dog_woof)
        self.woof_button.pack()

    def oldest_dog_woof(self):
        Dog.oldest_dog_woof(self.dog1, self.dog2)

root = tk.Tk()
dog_gui = DogGUI(root)
root.mainloop()