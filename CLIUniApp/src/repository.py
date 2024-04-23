import json
from model import Student
import os

class StudentRepository:
    """
    Klur's Note: This is not proper implementation yet, just for you guys to development on view first.
    """

    def __init__(self, file_path):
        self.file_path = file_path
        # self.check_file_path(file_path)
        self.students: list[Student] = []

    def check_file_path(self, file_path: str):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f'File path {file_path} does not exist')

    def get_all_students(self) -> list[Student]:
        """
        Return all student data.
        """
        return self.students

    def add_student(self, student: dict) -> bool:
        """
        Add student to the file. Return True if success else False
        """
        self.students.append(student)
        return True

    def get_student_by_id(self, student_id: str) -> Student | None:
        """
        Return student given student id if exists else None.
        """
        for student in self.students:
            if student.id == student_id:
                return student
        return None

    def remove_student(self, student_id: str) -> bool:
        """
        Remove student from the file. Return True if success else False.
        """
        for student in self.students:
            if student.id == student_id:
                self.students.remove(student)
                return True
        return False
        

if __name__ == "__main__":
    repo =  StudentRepository(os.getcwd() + '/CLIUniApp/src/data/student.data')
    student = Student("Klur", "wb@gmail.com", "qwert")
    print(repo.add_student(student))