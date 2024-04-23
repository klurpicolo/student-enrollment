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

    def __init__(self, admin_view: AdminView, student_login_view: StudentLoginView):
        self.admin_view = admin_view
        self.student_login_view = student_login_view


    def menu(self):
        pass