from tkinter import Toplevel, Label, Button, Tk, messagebox

class StudentLoginPage:
    def __init__(self, master):
        self.master = master
        self.master.title("Student Login")
        self.master.geometry('300x200')
        
        self.label = Label(self.master, text="Student Login Page")
        self.label.pack()

        self.back_button = Button(self.master, text="Go Back", command=self.go_back)
        self.back_button.pack(pady=10)

    def go_back(self):
        self.master.destroy()
        window.deiconify()

class AdminManagementPage:
    def __init__(self, master):
        self.master = master
        self.master.title("Admin Management")
        self.master.geometry('300x200')
        
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

        self.student_button = Button(self.master, text="Student System", command=self.open_student_page)
        self.student_button.pack(pady=20)

        self.admin_button = Button(self.master, text="Admin System", command=self.open_admin_page)
        self.admin_button.pack(pady=20)

    def open_student_page(self):
        self.master.withdraw()
        student_login_window = Toplevel(self.master)
        StudentLoginPage(student_login_window)

    def open_admin_page(self):
        self.master.withdraw()
        admin_management_window = Toplevel(self.master)
        AdminManagementPage(admin_management_window)

if __name__ == "__main__":
    window = Tk()
    app = MainWindow(window)
    window.mainloop()
