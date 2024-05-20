from repository import StudentRepository
from model import Grade
from utilities import *


class AdminView:
    """
    The Admin System
    Admin menu offers the following actions:
        (c) clear database file: enables admin to clear the data file “students.data”
        (g) group students: shows the students organized with respect to the grade
        (p) partition students: shows the pass/fail distribution
        (r) remove student: enables admin to remove a student by ID
        (s) show: show the students from the data file
        (x) exit
    """

    def __init__(self, student_repository: StudentRepository):
        self.student_repository = student_repository

    def menu(self):
        while True:
            admin_choice = input_blue("Admin System (c/g/p/r/s/x): ")
            if admin_choice == "s":
                self.viewStudents()
            elif admin_choice == 'g':
                self.viewStudentsByGrade()
            elif admin_choice == 'p':
                self.filterByPassFail()
            elif admin_choice == 'r':
                self.removeStudent()
            elif admin_choice == 'c':
                self.clearStudentDataStore()
            elif admin_choice == 'x':
                break

    def viewStudents(self):
        students = self.student_repository.get_all_students()
        print_yellow("Student List")
        for student in students:
            print_white(f"{student.name} :: {student.id} --> Email: {student.email}")

    def viewStudentsByGrade(self):
        students = self.student_repository.get_all_students()
        print_yellow("Grade Grouping")
        gradeTitle = ['HD', 'D', 'C', 'P', 'Z']

        HD = []
        D = []
        C = []
        P = []
        Z = []
        gradeList = [HD, D, C, P, Z]

        for student in students:
            totalMark = 0
            courseCount = 0

            for course in student.enrolled_subjects:
                totalMark += course.mark
                courseCount += 1

            if courseCount == 0:
                continue
            avgMark = totalMark / courseCount
            avgGrade = Grade.from_mark(avgMark)
            if avgMark > 85:
                HD.append((student, avgMark, avgGrade))
            elif 75 <= avgMark < 85:
                D.append((student, avgMark, avgGrade))
            elif 65 <= avgMark < 75:
                C.append((student, avgMark, avgGrade))
            elif 50 <= avgMark < 65:
                P.append((student, avgMark, avgGrade))
            else:
                Z.append((student, avgMark, avgGrade))

        for index, grade in enumerate(gradeList):
            if len(grade) == 0:
                continue
            else:
                print_white(gradeTitle[index], ' --> ', end='')
            print_white('[', end='', is_indent=False)

            for student, avgMark, avgGrade in grade:
                print_white(f"{student.name} :: {student.id} --> Grade: {avgGrade} - Mark: {avgMark}, ", end='',
                            is_indent=False)
            print_white(']', is_indent=False)

    def filterByPassFail(self):
        students = self.student_repository.get_all_students()
        print_yellow("PASS/FAIL Partition")
        titles = ['Fail', 'Pass']
        pass_student = []
        fail_student = []
        all_student = [fail_student, pass_student]
        for student in students:
            total_mark = 0
            course_count = 0
            for course in student.enrolled_subjects:
                total_mark += course.mark
                course_count += 1

            if course_count == 0:
                continue
            avg_mark = total_mark / course_count
            avg_grade = Grade.from_mark(avg_mark)
            if avg_mark < 50:
                fail_student.append((student, avg_mark, avg_grade))
            else:
                pass_student.append((student, avg_mark, avg_grade))

        for index, status in enumerate(all_student):
            print_white(titles[index], ' --> ', end='')
            print_white('[', end='', is_indent=False)
            for student, avg_mark, avg_grade in status:
                print_white(f"{student.name} :: {student.id} --> Grade: {avg_grade} - Mark: {avg_mark}, ", end='',
                            is_indent=False)
            print_white(']', is_indent=False)

    def removeStudent(self):
        id_to_remove = input("Remove by ID: ")
        if self.student_repository.remove_student(id_to_remove):
            print_yellow("Removing Student " + id_to_remove + " Account")
        else:
            print_red("Student " + id_to_remove + " does not exist")

    def clearStudentDataStore(self):
        print_yellow("Clearing student database")
        confirm = input_red("Are you sure you want to clear the student database (Y)ES/(N)O ")
        if confirm in ["Y", "y"]:
            self.student_repository.clean_database()
            print_yellow("Student data cleared")


if __name__ == "__main__":
    stu_re = StudentRepository(
        "D:\Python\student-enrollment\CLIUniApp\src\data\student.data"
    )
    '''students = student_repository.get_all_students()
    for student in students:
        print(f"Student id {student.id}")
    print(students)'''

    admin_view2 = AdminView(stu_re)
    admin_choice2 = input_blue("Admin System (c/g/p/r/s/x): ")
    if admin_choice2 == "s":
        admin_view2.viewStudents()
    elif admin_choice2 == 'g':
        admin_view2.viewStudentsByGrade()
    elif admin_choice2 == 'p':
        admin_view2.filterByPassFail()
    elif admin_choice2 == 'r':
        admin_view2.removeStudent()
    elif admin_choice2 == 'c':
        admin_view2.clearStudentDataStore()
