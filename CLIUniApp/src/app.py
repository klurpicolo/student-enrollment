from repository import StudentRepository
import model
from view import UniversityView, StudentLoginView, StudentView, AdminView
import os


if __name__ == "__main__":
    print("Initialize application")

    # Inject Dependency
    student_repository = StudentRepository(
        os.getcwd() + '/CLIUniApp/src/data/student.data'
    )
    admin_view = AdminView(student_repository)
    student_view = StudentView(student_repository=student_repository)
    student_login_view = StudentLoginView(
        student_repository=student_repository, student_view=student_view
    )
    university_view = UniversityView(
        admin_view=admin_view, student_login_view=student_login_view
    )

    print("Application started")
    university_view.menu()