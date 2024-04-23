from view import BaseView
from repository import StudentRepository

# Mark is working on this
class AdminView(BaseView):
    """
    The Admin System
    Admin menu offers the following actions:
        (c) clear database file: enables admin to clear the data file “students.data”
        (g) group students: shows the students organized with respect to the grade
        (p) partition students: shows the pass/fail distribution
        (r) remove student: enables admin to remove a student by ID
        (s) show: show the students from the data file
        (x) exit
    """

    def __init__(self, student_repository: StudentRepository):
        self.student_repository = student_repository

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
