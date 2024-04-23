from view import BaseView
from student_view import StudentView
from admin_view import AdminView
from repository import StudentRepository
from model import Admin

class StudentLoginView(BaseView):
    """
    The Student System
    The student menu system should enable students to Login and Register as follows:
        (l) login
        (r) register
        (x) exit
    """

    def __init__(self, student_repository: StudentRepository, student_view: StudentView):
        self.student_repository = student_repository
        self.student_view = student_view

    admins = [
        Admin(123,'asd'),
        Admin(234,'sdf')
    ]

    hint = """
    Please select the following option
    - (L) Login
    - (R) Register
    - (X) Log out
    """

    def menu(self):
        print(self.hint)
        while True:
            choice = input("Please enter the following choice(L, R, X): ")
            match choice:
                case "L":
                    self.login()
                case "R":
                    self.register()
                case "X":
                    self.logout()
                case _:
                    print(f"The choice {choice} is not one of (L, R, X). Please select a new valid choice.")
                

    def login(self):
        print("Please enter email and password")
        email = input("Email: ")
        password = input("Password: ")
        for admin in self.admins:
            if admin.email == email and admin.password == password:
                AdminView().menu()
        students = self.student_repo.get_all_students()
        for student in students:
            if student.email == email and student.password == password:
                StudentView(student, self.student_repo).menu()

    def register(self):
        print("Register is not implemented yet")
