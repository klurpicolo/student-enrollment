from repository import StudentRepository
from admin_view import AdminView
from student_login_view import StudentLoginView
from student_view import StudentView
from university_view import UniversityView

import os


if __name__ == "__main__":
    # Inject Dependency
    student_repository = StudentRepository(
        '/Users/georgeluther/Desktop/Master/FSD/UniversityApplication/student-enrollment/CLIUniApp/src/data/student.data'
    )
    admin_view = AdminView(student_repository)
    student_view = StudentView(student_repository=student_repository)
    student_login_view = StudentLoginView(
        student_repository=student_repository, student_view=student_view
    )
    university_view = UniversityView(
        admin_view=admin_view, student_login_view=student_login_view
    )
    university_view.menu()