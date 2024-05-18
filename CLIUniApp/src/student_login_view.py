from student_view import StudentView
from repository import StudentRepository
from model import Student
import utilities as utils
from validator import validate_password, validate_email


class StudentLoginView:
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

    hint = "Student System (l/r/x): "

    def menu(self):
        while True:
            choice = utils.input_blue(self.hint)
            match choice:
                case "l":
                    self.login()
                case "r":
                    self.register()
                case "x":
                    break
                case _:
                    utils.print_red(f"The choice {choice} is not one of (L, R, X). Please select a new valid choice.")

    def login(self):
        utils.print_green("Student Sign In")
        email = utils.input_white("Email: ")
        password = utils.input_white("Password: ")
        all_students = self.student_repository.get_all_students()
        all_emails = [student.email for student in all_students]
        is_login_fail = self.validate_credentials(email=email, password=password)
        if not is_login_fail:
            return
        # nested if - check if the email already exists in students repository...
        if email not in all_emails:
            utils.print_red("Student does not exist")
        else:
            for student in all_students:
                if student.email == email and student.password == password:
                    StudentView(self.student_repository, student).menu()

    def register(self):
        utils.print_green("Student Sign Up")
        students = self.student_repository.get_all_students()

        while True:
            input_email = utils.input_white("Email: ")
            input_password = utils.input_white("Password: ")
            # Success - saving student to student_repository from here...
            if self.validate_credentials(input_email, input_password):
                # check if student exists
                student_exists = False
                for i, student in enumerate(students):
                    iter_email = student.email
                    iter_name = student.name
                    if input_email == iter_email:
                        utils.print_red(f"Student {iter_name} already exists")
                        student_exists = True
                # If student doesn't exist, after checking for all students...
                if not student_exists:
                    fullname = utils.input_white("Name: ")
                    utils.print_yellow(f"Enrolling Student {fullname}")
                    student_to_store = Student(fullname, input_email, input_password)
                    self.student_repository.add_student(student_to_store)
                    break

    def validate_credentials(self, email, password):
        if validate_email(email) and validate_password(password):
            utils.print_yellow("email and password formats acceptable")
            return True
        else:
            utils.print_red("Incorrect email or password format")
            return False

    def check_email_exists(self, email, password):
        students = self.student_repository.get_all_students()
        for student in students:
            if student.email == email and student.password == password:
                print("Login Success!")
                StudentView(self.student_repository, student).menu()
