import sys
from .model import Student, Admin
from .repository import StudentRepository

class BaseView:

    def logout(self):
        print('Logging out, Good bye')
        sys.exit(0)


class LoginView(BaseView):

    def __init__(self, student_repo: StudentRepository):
        self.student_repo = student_repo

    admins = [
        Admin(123,'asd','456'),
        Admin(234,'sdf','567')
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

            
class AdminView(BaseView):

    hint = """
    Logged in as admin, you can select the following option
    - (V) view students
    - (D) delete all data
    - (X) log out
    - TBD
    """
    
    def menu(self):
        print(self.hint)
        choice = input("Please enter the choice: ")
        # TO be implemented
        match choice:
            case "X":
                self.logout()
        pass

    def viewStudentsByGrade():
        pass

    def filterByPassFail():
        pass

    def viewRegisteredStudents():
        pass

    def removeStudent():
        pass

    def clearStudentDataStore():
        pass



class StudentView(BaseView):

    def __init__(self, student, student_repo):
        self.student = student
        self.student_repo = student_repo


    hint = """
    Logged in as student , you can select the following option
    - (E) enroll subject
    - (W) withdraw subject
    - (X) log out
    - TBD
    """
    
    def menu(self):
        print(self.hint)
        choice = input("Please enter the choice: ")
        # TO be implemented
        match choice:
            case "X":
                self.logout()

    def enrollSubject():
        pass

    def displayEnrolment():
        pass

    def withdrawEnrolment():
        pass

    def changePassword():
        pass

    def exit():
        pass

