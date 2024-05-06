from view import BaseView
from admin_view import AdminView
from student_login_view import StudentLoginView
from utilities import *

class UniversityView(BaseView):
    """
    The University System
    The university menu system should enable users to choose to go the Admin menu or Student Menu
        (a) Admin
        (s) Student
        (x) exit
    """

    hint = """University System: (A)dmin, (S)tudent, or X: """

    def __init__(self, admin_view: AdminView, student_login_view: StudentLoginView):
        self.admin_view = admin_view
        self.student_login_view = student_login_view

    def menu(self):
        while True:
            choice = input_blue(self.hint)
            match choice:
                case "A":
                    self.admin_view.menu()
                case "S":
                    self.student_login_view.menu()
                case "X":
                    self.logout()
                case _:
                    print(f"The choice {choice} is not one of A, S, X). Please select a new valid choice.")
