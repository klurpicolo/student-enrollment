from view import BaseView
from repository import StudentRepository
from model import Student, Subject
from utilities import *
from validator import validate_password
import re


class StudentView(BaseView):
    """
    The Student Course System
    Logged in students can access this menu to perform the following actions:
        (c) change: enables a student to change their password
        (e) enrol: Student enrols in a subject. A student can enrol in maximum 4 subjects.
        (r) remove: Student can remove a subject from the subjects enrolment list
        (s) show: Shows the enrolled subjects and the marks and grades for each subject
        (x) exit
    """

    def __init__(self, student_repository, student=None):
        self.student_repo: StudentRepository = student_repository
        self.student: Student = student

    hint = "Student Course Menu (c/e/r/s/x): "

    def menu(self):
        # TO be implemented
        while True:
            choice = input_blue(self.hint)
            match choice:
                case "x":
                    self.logout()
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
        # Testing the case where subject already exists...
        if new_subject not in self.student.enrolled_subjects:
            self.student.enrolled_subjects.append(new_subject)
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

        # new_subject_list = []
        # for subject in student.enrolled_subjects:
        #     if withdraw_id == subject.id:
        #         continue

        #     new_subject_list.append(subject)
        #     print("Subject ID does not exist in enrolment list.")

        # if withdraw_id not in student.enrolled_subjects:
        # else:
        #     new_subject_list = []
        #     for subject in student.enrolled_subjects:
        #         if subject.id == withdraw_id:
        #             continue
        #         else:
        #             new_subject_list.append(subject)
        #             print(f"Have successfully withdrawn from {subject}")

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
    repo = StudentRepository("asds")
    student = Student("George", "asd@gmail.com", "1234")
    repo.add_student(student)
    student_view = StudentView(
        student_repository=repo,
        student=student
    )
    student_view.menu()
