from view import BaseView
from repository import StudentRepository
from model import Grade
from utilities import *

# Mark is working on this
class AdminView(BaseView):
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

    hint = """
    Logged in as admin, you can select the following option
    - (c) clear database file: enables admin to clear the data file “students.data”
    - (g) group students: shows the students organized with respect to the grade
    - (p) partition students: shows the pass/fail distribution
    - (r) remove student: enables admin to remove a student by ID
    - (s) show: show the students from the data file
    - (x) exit
    - TBD
    """
    
    def menu(self):
        # TO be implemented
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
            self.logout()


    
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
        gradeList = [HD,D,C,P,Z]
        
        for student in students:
            totalMark = 0
            courseCount = 0
            
            for course in student.enrolled_subjects:
                totalMark += course.mark
                courseCount += 1
                
            if courseCount == 0:
                continue
            avgMark = totalMark/courseCount
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
                print_white(gradeTitle[index], ' --> ',end = '')
            print_white('[',end = '', is_indent= False)
            
            for student, avgMark, avgGrade in grade:
                
                print_white(f"{student.name} :: {student.id} --> Grade: {avgGrade} - Mark: {avgMark}, ", end = '', is_indent=False)
            print_white(']', is_indent= False)
            

    def filterByPassFail(self):
        students = self.student_repository.get_all_students()
        print_yellow("PASS/FAIL Partition")
        Titles = ['Fail', 'Pass']
        Pass = []
        Fail = []
        PnF = [Fail, Pass]
        for student in students:
            totalMark = 0
            courseCount = 0
            for course in student.enrolled_subjects:
                totalMark += course.mark
                courseCount += 1
                
            if courseCount == 0:
                continue
            avgMark = totalMark/courseCount
            avgGrade = Grade.from_mark(avgMark)
            if avgMark < 50:
                Fail.append((student, avgMark, avgGrade))
            else:
                Pass.append((student, avgMark, avgGrade))
                
        for index, status in enumerate(PnF):
           
            print_white(Titles[index], ' --> ',end = '')
            print_white('[',end = '', is_indent=False)
        
            
            for student, avgMark, avgGrade in status:
                
                print_white(f"{student.name} :: {student.id} --> Grade: {avgGrade} - Mark: {avgMark}, ", end = '', is_indent=False)
            print_white(']',is_indent=False)
                

    def removeStudent(self):
        idToRemove = input("Remove by ID: ")
        if self.student_repository.remove_student(idToRemove) == True:
            print_yellow("Removing Student "+idToRemove+" Account")
        else:
            print_red("Student "+idToRemove+" does not exist")
            
         
        
    

    def clearStudentDataStore(self):
        print_yellow("Clearing student database")
        confirm = input_red("Are you sure you want to clear the student database (Y)ES/(N)O ")
        if confirm in ["Y","y"]:
            self.student_repository.clean_database()
            print_yellow("Student data cleared")
        
            
        


if __name__ == "__main__":
    student_repository = StudentRepository(
        "D:\Python\student-enrollment\CLIUniApp\src\data\student.data"
    )
    '''students = student_repository.get_all_students()
    for student in students:
        print(f"Student id {student.id}")
    print(students)'''
    
    admin_view = AdminView(student_repository)
    admin_choice = input_blue("Admin System (c/g/p/r/s/x): ")
    if admin_choice == "s":
        admin_view.viewStudents()
    elif admin_choice == 'g':
        admin_view.viewStudentsByGrade()
    elif admin_choice == 'p':
        admin_view.filterByPassFail()
    elif admin_choice == 'r':
        admin_view.removeStudent()
    elif admin_choice == 'c':
        admin_view.clearStudentDataStore()
    
    

        