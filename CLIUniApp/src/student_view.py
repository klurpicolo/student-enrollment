from view import BaseView

class StudentView(BaseView):
    """
    The Student Course System
    Logged in students can access this menu to perform the following actions:
        (c) change: enables a student to change their password
        (e) enrol: Student enrols in a subject. A student can enrol in maximum 4 subjects.
        (r) remove: Student can remove a subject from the subjects’ enrolment list
        (s) show: Shows the enrolled subjects and the marks and grades for each subject
        (x) exit
    """

    def __init__(self, student_repository, student = None):
        self.student_repo = student_repository
        self.student = student

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