from tkinter import Toplevel, Label, Button, Tk, messagebox, Entry
import os
from repository import StudentRepository

class StudentEnrollmentPage:
    def __init__(self, master):
        self.master = master

class StudentLoginPage:
    def __init__(self, master, student_repo):
        self.master = master
        self.student_repo = student_repo
        self.master.title("Student Login")
        self.master.geometry('500x500')

        self.label = Label(self.master, text="Student Login Page")
        self.label.pack()

        self.email_label = Label(self.master, text="Email:")
        self.email_label.pack()
        self.email_entry = Entry(self.master)
        self.email_entry.pack()

        self.password_label = Label(self.master, text="Password:")
        self.password_label.pack()
        self.password_entry = Entry(self.master, show="*")
        self.password_entry.pack()

        self.login_button = Button(self.master, text="Login", command=self.login_page)
        self.login_button.pack(pady=20)

        self.register_button = Button(self.master, text="Register", command=self.register_page)
        self.register_button.pack(pady=20)

        self.back_button = Button(self.master, text="Go Back", command=self.go_back)
        self.back_button.pack(pady=10)

    def go_back(self):
        self.master.destroy()
        window.deiconify()

    def login_page(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        # Check if email and password match any student's credentials
        students = self.student_repo.get_all_students()
        for student in students:
            if student.email == email and student.password == password:
                # Navigate to student enrollment page
                self.master.destroy()  # Close current window
                student_enrollment_window = Toplevel(self.master)
                StudentEnrollmentPage(student_enrollment_window, student)
                return

        # If no match found, show a pop-up dialog
        messagebox.showerror("Login Failed", "Incorrect email or password")

    def register_page(self):
        pass

class AdminManagementPage:
    def __init__(self, master):
        self.master = master
        self.master.title("Admin Management")
        self.master.geometry('500x500')

        self.label = Label(self.master, text="Admin Management Page")
        self.label.pack()

        self.back_button = Button(self.master, text="Go Back", command=self.go_back)
        self.back_button.pack(pady=10)

    def go_back(self):
        self.master.destroy()
        window.deiconify()


class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Student Enrolment Application")
        self.master.geometry('500x500')

        self.label = Label(self.master, text="Student Login Page")
        self.label.pack()

        self.student_button = Button(self.master, text="Student System", command=self.open_student_page)
        self.student_button.pack(pady=20, padx=10, side='top')

        self.admin_button = Button(self.master, text="Admin System", command=self.open_admin_page)
        self.admin_button.pack(pady=20, padx=20, side='top')

    def open_student_page(self):
        self.master.withdraw()
        student_login_window = Toplevel(self.master)
        StudentLoginPage(student_login_window, StudentRepository(os.getcwd() + '/src/data/student.data'))

    def open_admin_page(self):
        self.master.withdraw()
        admin_management_window = Toplevel(self.master)
        AdminManagementPage(admin_management_window)


if __name__ == "__main__":
    window = Tk()
    app = MainWindow(window)
    window.mainloop()
