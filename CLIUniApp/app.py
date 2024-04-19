import repository
import model
import view


if __name__ == "__main__":
    print("Application started")

    student_repo = repository.StudentRepository([
        model.Student(111, 'aaa', 'sss')
    ])
    system = view.LoginView(student_repo)
    system.menu()