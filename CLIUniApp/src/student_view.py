from view import BaseView
from repository import StudentRepository
from model import Student, Subject

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

    def __init__(self, student_repository, student = None):
        self.student_repo: StudentRepository = student_repository
        self.student: Student = student

    hint = """
    Logged in as student , you can select the following option
    - (E) enrol subject
    - (D) display enroleld subjects
    - (W) withdraw subject
    - (X) log out
    - (C) change password
    """
    
    def menu(self):
        print(self.hint)
        # TO be implemented
        while True:
            choice = input("Please enter a choice: ")
            match choice:
                case "X":
                    self.logout()
                case "E":
                    self.enrolSubject()
                case "W":
                    self.withdrawEnrolment()
                case "D":
                    self.displayEnrolment()
                case "C":
                    self.changePassword()

    def enrolSubject(self):
        if len(self.student.enrolled_subjects) >= 4:
            print("You have already enrolled in the maximum number of subjects (4).")
            return
        
        new_subject = Subject()        
        # Testing the case where subject already exists...
        if new_subject not in student.enrolled_subjects:
            student.enrolled_subjects.append(new_subject)
            print(f"Success! Enrolled into Subject-{new_subject.id}")
        else:
            print("No action taken. You are already enrolled into this subject.")


    def displayEnrolment(self):
        if len(self.student.enrolled_subjects) > 0:
            print("Enrolled Subjects:")
            for i, subject in enumerate(self.student.enrolled_subjects):
                print(f'[ {subject} ]')
        else:
            print("You have yet to enrol into any subjects.")

    def withdrawEnrolment(self):
        withdraw_id = str(input("Remove subject by ID: "))
        print(f'withdraw_id {withdraw_id}')

        new_enrol_subject = [s for s in self.student.enrolled_subjects if s.id != withdraw_id]
        self.student.enrolled_subjects = new_enrol_subject
        for s in self.student.enrolled_subjects:
            print(f'[ {s} ]')
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
        new_password = input("Please enter a new password: ")
        student.student_password = new_password
        print("Password change successful.")

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