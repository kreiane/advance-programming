import tkinter as tk
from tkinter import ttk

class StudentRegistrationForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Registration Form")

        # Style configuration
        self.style = ttk.Style()
        self.style.configure("TLabel", padding=(5, 5, 10, 10), font=('Helvetica', 12))
        self.style.configure("TEntry", padding=(5, 5, 10, 10), font=('Helvetica', 12))
        self.style.configure("TButton", padding=(5, 5, 10, 10), font=('Helvetica', 12))
        self.style.configure("TRadiobutton", padding=(5, 5, 10, 10), font=('Helvetica', 12))
        self.style.configure("TCheckbutton", padding=(5, 5, 10, 10), font=('Helvetica', 12))
        self.style.configure("TCombobox", padding=(5, 5, 10, 10), font=('Helvetica', 12))

        # Student Name
        self.label_name = ttk.Label(root, text="Student Name:")
        self.label_name.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.entry_name = ttk.Entry(root)
        self.entry_name.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        # Mobile Number
        self.label_mobile = ttk.Label(root, text="Mobile Number:")
        self.label_mobile.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.entry_mobile = ttk.Entry(root)
        self.entry_mobile.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        # Email ID
        self.label_email = ttk.Label(root, text="Email ID:")
        self.label_email.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.entry_email = ttk.Entry(root)
        self.entry_email.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        # Home Address
        self.label_address = ttk.Label(root, text="Home Address:")
        self.label_address.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.entry_address = ttk.Entry(root)
        self.entry_address.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        # Gender
        self.label_gender = ttk.Label(root, text="Gender:")
        self.label_gender.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.gender_var = tk.StringVar()
        self.gender_var.set("Male")  # Default value
        self.gender_menu = ttk.Combobox(root, textvariable=self.gender_var, values=["Male", "Female", "Other"])
        self.gender_menu.grid(row=4, column=1, padx=10, pady=10, sticky="w")

        # Course Enrolled
        self.label_course = ttk.Label(root, text="Course Enrolled:")
        self.label_course.grid(row=5, column=0, padx=10, pady=10, sticky="w")
        self.course_var = tk.StringVar()
        self.course_var.set("BSc CC")  # Default value

        course_options = ["BSc CC", "BSc CY", "BSc PSY", "BA & BM"]
        self.course_radios = []

        for i, course in enumerate(course_options):
            radio = ttk.Radiobutton(root, text=course, variable=self.course_var, value=course)
            radio.grid(row=5, column=1+i, padx=5, pady=5, sticky="w")
            self.course_radios.append(radio)

        # Language Known
        self.label_language = ttk.Label(root, text="Language Known:")
        self.label_language.grid(row=6, column=0, padx=10, pady=10, sticky="w")
        self.language_vars = [tk.BooleanVar() for _ in range(3)]
        language_options = ["English", "Tagalog", "Hindi/Urdu"]
        self.language_checkboxes = []

        for i, language in enumerate(language_options):
            checkbox = ttk.Checkbutton(root, text=language, variable=self.language_vars[i])
            checkbox.grid(row=6, column=1+i, padx=5, pady=5, sticky="w")
            self.language_checkboxes.append(checkbox)

        # Rate Your English Communication Skills
        self.label_rating = ttk.Label(root, text="Rate Your English Communication Skills:")
        self.label_rating.grid(row=7, column=0, padx=10, pady=10, sticky="w")
        self.rating_scale = ttk.Scale(root, from_=0, to=10, orient="horizontal", length=200)
        self.rating_scale.grid(row=7, column=1, padx=10, pady=10, sticky="w")

        # Submit Button
        self.submit_button = ttk.Button(root, text="Submit", command=self.submit_form)
        self.submit_button.grid(row=8, column=0, padx=10, pady=10, sticky="w")

        # Clear Button
        self.clear_button = ttk.Button(root, text="Clear", command=self.clear_form)
        self.clear_button.grid(row=8, column=1, padx=10, pady=10, sticky="w")

    def submit_form(self):
        # Add logic to process and store the form data
        print("Form submitted!")

    def clear_form(self):
        # Clear all form fields
        self.entry_name.delete(0, "end")
        self.entry_mobile.delete(0, "end")
        self.entry_email.delete(0, "end")
        self.entry_address.delete(0, "end")
        self.gender_var.set("Male")
        self.course_var.set("BSc CC")
        for checkbox in self.language_checkboxes:
            checkbox.deselect()
        self.rating_scale.set(0)

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentRegistrationForm(root)
    root.mainloop()