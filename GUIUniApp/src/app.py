import os
import tkinter as tk
from tkinter import ttk
from model import Student
from repository import StudentRepository
from admin_page import AdminPage
from start_page import StartPage
from studentlogin_page import StudentLoginPage
from studentcourse_page import StudentCoursePage

LARGEFONT = ("Verdana", 35)
student_repository = StudentRepository(os.getcwd() + '/data/student.data')


class UniversityGuiApp(tk.Tk):
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
        self.logged_in_student: Student | None = None
        for F in (StartPage, StudentLoginPage, AdminPage, StudentCoursePage):
            frame = F(self.main_frame, self, student_repository)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.re_render()
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


if __name__ == "__main__":
    app = UniversityGuiApp()
    app.title("GUIUniApp")
    app.geometry("800x600")
    app.mainloop()
