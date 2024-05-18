from repository import StudentRepository
from model import Student, Subject
from utilities import *
from validator import validate_password


class StudentView:
    """
    The Student Course System
    Logged in students can access this menu to perform the following actions:
        (c) change: enables a student to change their password
        (e) enrol: Student enrols in a subject. A student can enrol in maximum 4 subjects.
        (r) remove: Student can remove a subject from the subjects enrolment list
        (s) show: Shows the enrolled subjects and the marks and grades for each subject
        (x) exit
    """

    def __init__(self, student_repository, student: Student = None):
        self.student_repo: StudentRepository = student_repository
        self.student: Student = student

    hint = "Student Course Menu (c/e/r/s/x): "

    def menu(self):
        while True:
            choice = input_blue(self.hint)
            match choice:
                case "x":
                    break
                case "e":
                    self.enrolSubject()
                case "r":
                    self.withdrawEnrolment()
                case "s":
                    self.displayEnrolment()
                case "c":
                    self.changePassword()

    def enrolSubject(self):
        if len(self.student.enrolled_subjects) >= 4:
            print_red("Students are allowed to enroll in 4 subjects only")
            return

        new_subject = Subject()
        if new_subject not in self.student.enrolled_subjects:
            self.student.enrolled_subjects.append(new_subject)
            self.student_repo.update_student(self.student)
            print_yellow(f"Enrolling in subject-{new_subject.id}")
            print_yellow(f"You are now enrolled in {len(self.student.enrolled_subjects)} out of 4 subjects")

    def displayEnrolment(self):
        print_yellow(f"Showing {len(self.student.enrolled_subjects)} subjects")
        for i, subject in enumerate(self.student.enrolled_subjects):
            print_white(f'[ {subject} ]')

    def withdrawEnrolment(self):
        withdraw_id = str(input_white("Remove subject by ID: "))
        print_yellow(f'Dropping subject-{withdraw_id}')

        new_enrol_subject = [s for s in self.student.enrolled_subjects if s.id != withdraw_id]
        self.student.enrolled_subjects = new_enrol_subject

        print_yellow(f"You are now enrolled in {len(self.student.enrolled_subjects)} out of 4 subjects")
        # print(f'self.student.enrolled_subjects {self.student.enrolled_subjects}')
        self.student_repo.update_student(self.student)

    def changePassword(self):
        print_yellow("Updating password")
        new_password = input_white("New password: ")
        if not validate_password(new_password):
            print_red("Incorrect password format")
            return
        while True:
            confirm_password = input_white("Confirm password: ")
            if new_password == confirm_password:
                break
            else:
                print_red("Password does not match - try again")
        self.student.password = new_password
        self.student_repo.update_student(self.student)

    def exit(self):
        pass


if __name__ == "__main__":
    repo2 = StudentRepository("asds")
    student2 = Student("George", "asd@gmail.com", "1234")
    repo2.add_student(student2)
    student_view = StudentView(
        student_repository=repo2,
        student=student2
    )
    student_view.menu()
