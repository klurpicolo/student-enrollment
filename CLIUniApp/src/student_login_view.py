from view import BaseView
from student_view import StudentView
from admin_view import AdminView
from repository import StudentRepository
from model import Admin, Student
import utilities as utils
import re


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
                    self.logout()
                case _:
                    print(f"The choice {choice} is not one of (L, R, X). Please select a new valid choice.")

    def login(self):
        utils.print_green("Student Sign In")
        email = input("Email: ")
        password = input("Password: ")
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
                    is_login_fail = False
                    StudentView(student, self.student_repository).menu()
            
    def register(self):
        utils.print_green("Student Sign Up")
        students = self.student_repository.get_all_students()
        existing_emails = [student.email for student in students] # our iterator

        while True:
            input_email = input("Email: ")
            input_password = input("Password: ")
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
                if student_exists == False:
                    fullname = input("Name: ")
                    utils.print_yellow(f"Enrolling Student {fullname}")
                    student_to_store = Student(fullname, input_email, input_password)
                    self.student_repository.add_student(student_to_store)
                    break
                
            
    def validate_email(self, email):
        """
        Will return true if email pattern matches email input.
        
        Email:
        - Contains '@university.com'
        """
        email_pattern = r"^[a-zA-Z]+[.][a-zA-Z]+@university[.]com$"
        return re.match(email_pattern, email)
    
    def validate_password(self, password):
        """
        Will return true if password pattern matches password input.
        
        Password:
        - Start with upper case
        - Minimum 6 letters
        - Following by minimum 3-digits
        """
        password_pattern = r"^[A-Z][a-zA-Z]{5,}[0-9]{3,}$"
        return re.match(password_pattern, password)

    def validate_credentials(self, email, password):

        if (self.validate_email(email) and self.validate_password(password)):
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
                StudentView(student, self.student_repository).menu()