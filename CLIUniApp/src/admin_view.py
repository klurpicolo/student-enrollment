from view import BaseView
from repository import StudentRepository
from model import Grade

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
        print(self.hint)
        choice = input("Please enter the choice: ")
        # TO be implemented
        match choice:
            case "X":
                self.logout()
        pass

    
    def viewStudents(self):
        students = self.student_repository.get_all_students()
        for student in students:
            print(f"Student id:  {student.id}")
            print(f"Student Name:  {student.name}")
            print(f"Student Email: {student.email}")
        
    def viewStudentsByGrade(self):
        students = student_repository.get_all_students()
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
            if avgMark > 85:
                HD.append(student)
            elif 75 <= avgMark < 85:
                D.append(student)
            elif 65 <= avgMark < 75:
                C.append(student)
            elif 50 <= avgMark < 65: 
                P.append(student)
            else:
                Z.append(student)
                
        for index, grade in enumerate(gradeList):
            print(gradeTitle[index], ':')
            for student in grade:
                print(f"{student.name} :: {student.id} --> Mark: {avgMark}")
                #print(f"Student Name:  {student.name}")
                #print(f"Student Email: {student.email}")         
            

    def filterByPassFail(self):
        students = student_repository.get_all_students()
        Titles = ['Pass', 'Fail']
        Pass = []
        Fail = []
        PnF = [Pass, Fail]
        for student in students:
            totalMark = 0
            courseCount = 0
            for course in student.enrolled_subjects:
                totalMark += course.mark
                courseCount += 1
                
            if courseCount == 0:
                continue
            avgMark = totalMark/courseCount
            if avgMark < 50:
                Fail.append(student)
            else:
                Pass.append(student)
                
        for index, status in enumerate(PnF):
            print(Titles[index], ' --> ', end='')
            for student in status:
                print(f"{student.name} :: {student.id} --> Mark: {avgMark}")
                

    def removeStudent(self):
        pass

    def clearStudentDataStore(self):
        pass


if __name__ == "__main__":
    print("start from admin view")
    student_repository = StudentRepository(
        "D:\Python\student-enrollment\CLIUniApp\src\data\student.data"
    )
    '''students = student_repository.get_all_students()
    for student in students:
        print(f"Student id {student.id}")
    print(students)'''
    
    admin_view = AdminView(student_repository)
    admin_choice = input("Enter your choice...")
    if admin_choice == "s":
        admin_view.viewStudents()
    elif admin_choice == 'g':
        admin_view.viewStudentsByGrade()
    elif admin_choice == 'p':
        admin_view.filterByPassFail()
        
    

        