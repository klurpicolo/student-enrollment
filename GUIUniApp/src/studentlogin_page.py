import tkinter as tk
from tkinter import ttk, messagebox
from validator import validate_email, validate_password
from model import Student
from studentcourse_page import StudentCoursePage


class StudentLoginPage(tk.Frame):
    def __init__(self, parent, controller, student_repository):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.student_repository = student_repository

        notebook = ttk.Notebook(self)
        notebook.pack(fill="both", expand=True)

        # Login Tab
        login_frame = ttk.Frame(notebook)
        notebook.add(login_frame, text="Login")

        login_label = ttk.Label(login_frame, text="Login", font=("Verdana", 20))
        login_label.grid(row=0, column=0, columnspan=2, pady=10)

        email_label = ttk.Label(login_frame, text="Email:")
        email_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.email_entry_login = ttk.Entry(login_frame)
        self.email_entry_login.grid(row=1, column=1, padx=5, pady=5)

        password_label = ttk.Label(login_frame, text="Password:")
        password_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.password_entry_login = ttk.Entry(login_frame, show="*")
        self.password_entry_login.grid(row=2, column=1, padx=5, pady=5)

        login_button = ttk.Button(login_frame, text="Sign In", command=self.login)
        login_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Register Tab
        register_frame = ttk.Frame(notebook)
        notebook.add(register_frame, text="Register")

        register_label = ttk.Label(register_frame, text="Register", font=("Verdana", 20))
        register_label.grid(row=0, column=0, columnspan=2, pady=10)

        name_label = ttk.Label(register_frame, text="Name:")
        name_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.name_entry = ttk.Entry(register_frame)
        self.name_entry.grid(row=1, column=1, padx=5, pady=5)

        email_label = ttk.Label(register_frame, text="Email:")
        email_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.email_entry_register = ttk.Entry(register_frame)
        self.email_entry_register.grid(row=2, column=1, padx=5, pady=5)

        password_label = ttk.Label(register_frame, text="Password:")
        password_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.password_entry_register = ttk.Entry(register_frame, show="*")
        self.password_entry_register.grid(row=3, column=1, padx=5, pady=5)

        register_button = ttk.Button(register_frame, text="Sign Up", command=self.register_student)
        register_button.grid(row=4, column=0, columnspan=2, pady=10)

    def re_render(self):
        pass

    def login(self):
        email = self.email_entry_login.get()
        password = self.password_entry_login.get()
        students = self.student_repository.get_all_students()
        for student in students:
            if student.email == email and student.password == password:
                messagebox.showinfo("Success", f"Welcome {student.name}")
                self.controller.logged_in_student = student
                self.controller.show_frame(StudentCoursePage)
                break
        else:
            messagebox.showinfo("Fail", f"Email or Password incorrect")

    def register_student(self):
        name = self.name_entry.get()
        email = self.email_entry_register.get()
        password = self.password_entry_register.get()

        # Validating email and password
        if not validate_email(email):
            messagebox.showerror("Error", "Invalid email format. Email should be in the format "
                                          "'firstname.lastname@university.com'")
            return
        if not validate_password(password):
            messagebox.showerror("Error", "Invalid password format. Password should start with an uppercase letter, "
                                          "followed by at least 5 letters and end with at least 3 digits.")
            return

        # Registering student
        if self.student_repository.add_student(Student(name=name, email=email, password=password)):
            messagebox.showinfo("Success", "Registration successful!")
            # Clearing the entry fields after successful registration
            self.name_entry.delete(0, 'end')
            self.email_entry_register.delete(0, 'end')
            self.password_entry_register.delete(0, 'end')
        else:
            messagebox.showerror("Error", "Failed to register student.")
