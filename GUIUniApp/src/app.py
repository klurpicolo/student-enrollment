import tkinter as tk
from tkinter import ttk, Text, messagebox
from repository import StudentRepository
import os

LARGEFONT = ("Verdana", 35)
student_repository = StudentRepository(os.getcwd() + '/data/student.data')

class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.pages_frame = tk.Frame(container, width=200, bg="gray")
        self.pages_frame.grid(row=0, column=0, sticky="nsew")

        self.main_frame = tk.Frame(container)
        self.main_frame.grid(row=0, column=1, sticky="nsew")

        self.frames = {}
        for F in (StartPage, StudentLoginPage, AdminPage, StudentCoursePage):
            frame = F(self.main_frame, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        self.update_sidebar_buttons(frame)

    def update_sidebar_buttons(self, frame):
        for widget in self.pages_frame.winfo_children():
            widget.destroy()

        if isinstance(frame, StartPage):
            button1 = ttk.Button(self.pages_frame, text="As student", command=lambda: self.show_frame(StudentLoginPage))
            button1.pack(fill="x")
            button2 = ttk.Button(self.pages_frame, text="As admin", command=lambda: self.show_frame(AdminPage))
            button2.pack(fill="x")

        elif isinstance(frame, StudentLoginPage):
            button1 = ttk.Button(self.pages_frame, text="GUIUniApp", command=lambda: self.show_frame(StartPage))
            button1.pack(fill="x")

        elif isinstance(frame, AdminPage):
            button1 = ttk.Button(self.pages_frame, text="GUIUniApp", command=lambda: self.show_frame(StartPage))
            button1.pack(fill="x")

        elif isinstance(frame, StudentCoursePage):
            button1 = ttk.Button(self.pages_frame, text="GUIUniApp", command=lambda: self.show_frame(StartPage))
            button1.pack(fill="x")
            button2 = ttk.Button(self.pages_frame, text="LoginPage", command=lambda: self.show_frame(StudentLoginPage))
            button2.pack(fill="x")



class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="GUIUniApp", font=LARGEFONT)
        label.pack()

        select_label = ttk.Label(self, text="Select student or admin page", font=("Verdana", 12))
        select_label.pack()


class StudentLoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

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

    def login(self):
        email = self.email_entry_login.get()
        password = self.password_entry_login.get()
        students = student_repository.get_all_students()
        for student in students:
            if student.email == email and student.password == password:
                messagebox.showinfo("Success", f"Welcome {student.name}")
                self.controller.show_frame(StudentCoursePage)
                break

    def register_student(self):
        name = self.name_entry.get()
        email = self.email_entry_register.get()
        password = self.password_entry_register.get()
        # Not implement this yet


class StudentCoursePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = ttk.Label(self, text="Student course page", font=LARGEFONT)
        label.pack()
        notebook = ttk.Notebook(self)
        notebook.pack(fill="both", expand=True)

        # Show Tab
        show_frame = ttk.Frame(notebook)
        notebook.add(show_frame, text="Show")
        show_label = ttk.Label(show_frame, text="Show Courses", font=("Verdana", 20))
        show_label.pack()

        # Enroll Tab
        enroll_frame = ttk.Frame(notebook)
        notebook.add(enroll_frame, text="Enroll")
        enroll_label = ttk.Label(enroll_frame, text="Enroll in Courses", font=("Verdana", 20))
        enroll_label.pack()

        # Remove Tab
        remove_frame = ttk.Frame(notebook)
        notebook.add(remove_frame, text="Remove")
        remove_label = ttk.Label(remove_frame, text="Remove Courses", font=("Verdana", 20))
        remove_label.pack()

        # Change Password Tab
        change_password_frame = ttk.Frame(notebook)
        notebook.add(change_password_frame, text="Change Password")
        change_password_label = ttk.Label(change_password_frame, text="Change Password", font=("Verdana", 20))
        change_password_label.pack()

class AdminPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.create_notebook()

    def create_notebook(self):
        notebook = ttk.Notebook(self)
        notebook.pack(fill="both", expand=True)

        self.create_show_tab(notebook)
        self.create_group_tab(notebook)
        self.create_partition_tab(notebook)
        self.create_remove_tab(notebook)

    def create_show_tab(self, notebook):
        show_frame = ttk.Frame(notebook)
        notebook.add(show_frame, text="Show")

        tree = ttk.Treeview(show_frame, columns=("ID", "Name", "Email"), show="headings")
        tree.heading("ID", text="ID")
        tree.heading("Name", text="Name")
        tree.heading("Email", text="Email")
        tree.pack(fill="both", expand=True)

        students = student_repository.get_all_students()
        for student in students:
            tree.insert("", "end", values=(student.id, student.name, student.email))

    def create_group_tab(self, notebook):
        group_frame = ttk.Frame(notebook)
        notebook.add(group_frame, text="Group")
        group_label = ttk.Label(group_frame, text="Group students by grade", font=("Verdana", 20))
        group_label.pack()

    def create_partition_tab(self, notebook):
        partition_frame = ttk.Frame(notebook)
        notebook.add(partition_frame, text="Partition")
        partition_label = ttk.Label(partition_frame, text="Partition student by pass/fail", font=("Verdana", 20))
        partition_label.pack()

    def create_remove_tab(self, notebook):
        remove_frame = ttk.Frame(notebook)
        notebook.add(remove_frame, text="Remove")
        remove_label = ttk.Label(remove_frame, text="Remove student", font=("Verdana", 20))
        remove_label.pack()

        # Function to handle removal of a student
        def remove_student(event):
            item = tree.selection()[0]  # Get the selected item
            student_id = tree.item(item, "values")[0]  # Get the student ID
            student_name = tree.item(item, "values")[1]
            confirmation = messagebox.askyesno("Confirmation", f"Are you sure you want to remove {student_name} student?")
            if confirmation:
                if student_repository.remove_student(student_id):
                    tree.delete(item)  # Remove the selected item from the Treeview
                    messagebox.showinfo("Success", f"Student with ID {student_id} has been removed.")
                else:
                    messagebox.showerror("Error", "Failed to remove student.")

        # Populate Treeview with student data
        tree = ttk.Treeview(remove_frame, columns=("ID", "Name", "Email"), show="headings")
        tree.heading("ID", text="ID")
        tree.heading("Name", text="Name")
        tree.heading("Email", text="Email")
        tree.pack(fill="both", expand=True)

        students = student_repository.get_all_students()
        for student in students:
            tree.insert("", "end", values=(student.id, student.name, student.email))

        # Bind the remove_student function to the Button-1 event (left-click) on the Treeview
        tree.bind("<Button-1>", remove_student)


if __name__ == "__main__":
    app = tkinterApp()
    app.title("GUIUniApp")
    app.geometry("800x600")
    app.mainloop()
