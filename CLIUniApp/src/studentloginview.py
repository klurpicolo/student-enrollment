import re
from view import BaseView
from student_view import StudentView
from repository import StudentRepository
from model import Student


class StudentLoginView(BaseView):
    def __init__(self, student_repository: StudentRepository, student_view: StudentView):
        self.student_repository = student_repository
        self.student_view = student_view

    hint = """
    Please select the following option
    - (l) Login
    - (r) Register
    - (x) Log out
    """

    def menu(self):
        print(self.hint)
        while True:
            choice = input("Please enter the following choice(L, R, X): ").lower()
            match choice:
                case "l":
                    self.login()
                case "r":
                    self.register()
                case "x":
                    print("Exiting system...")
                    break
                case _:
                    print(f"The choice {choice} is not one of (l, r, x). Please select a new valid choice.")

    def login(self):
        email = input("Email: ")
        password = input("Password: ")
        if self.student_repository.authenticate(email, password):
            print("Login successful!")
            student = self.student_repository.find_student_by_email(email)
            self.student_view.student_menu(student)
        else:
            print("Invalid email or password.")

    def register(self):
        name = input("Name: ")
        email = input("Email: ")
        if not re.match(r"^[a-zA-Z]+\.[a-zA-Z]+@university\.com$", email):
            print("Email does not match the required format: firstname.lastname@university.com")
            return
        password = input("Password: ")
        if not re.match(r"^[A-Z][a-zA-Z]{4,}[0-9]{3,}$", password):
            print("Password must start with an uppercase letter, followed by at least 4 more letters and at least 3 digits.")
            return
        student_id = self.student_repository.generate_student_id()
        if self.student_repository.add_student(student_id, name, email, password):
            print(f"Registration successful! Your student ID is: {student_id}")
        else:
            print("Registration failed. Email might already be in use.")

    def logout(self):
        print("You have been logged out.")
        # Additional cleanup actions can be performed here
    

    def generate_student_id(self):
        return str(random.randint(1, 999999)).zfill(6)

    def find_student_by_email(self, email):
        students = self.student_repository.get_all_students()
        for student in students:
            if student.email == email:
                return student
        return None