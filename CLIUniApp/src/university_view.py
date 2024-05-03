from view import BaseView
from admin_view import AdminView
from student_login_view import StudentLoginView

class UniversityView(BaseView):
    """
    The University System
    The university menu system should enable users to choose to go the Admin menu or Student Menu
        (A) Admin
        (S) Student
        (X) exit
    """

    hint = """
    University main menu
    Please select the following option
    - (a) Admin
    - (s) Student
    - (X) Log out
    """

    def __init__(self, admin_view: AdminView, student_login_view: StudentLoginView):
        self.admin_view = admin_view
        self.student_login_view = student_login_view


    def menu(self):
        print(self.hint)
        while True:
            choice = input("Please enter the following choice(a, s, x): ")
            match choice:
                case "a":
                    "logged in as admin"
                    self.admin_view.menu()
                case "s":
                    "enter student"
                    self.student_login_view.menu()
                case "x":
                    self.logout()
                case _:
                    print(f"The choice {choice} is not one of a, s, x). Please select a new valid choice.")