from src.repository import StudentRepository
from src.model import Student
from src.view import LoginView


if __name__ == "__main__":
    print("Application started")

    student_repo = StudentRepository([
        Student(111, 'aaa', 'sss')
    ])
    system = LoginView(student_repo)
    system.menu()