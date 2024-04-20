from model import Student
import os

DATA_FILE = "./data/student.data"

class StudentRepository:

    def __init__(self, file_path):
        self.check_file_path(file_path)
        self.file_path = file_path

    def check_file_path(self, file_path: str):
        if os.path.exists(file_path):
            print(f'File path {file_path} check pass')
        else:
            raise Exception(f'File path {file_path} does not exist')

    def get_all_students(self) -> list[Student]:
        """
        Return all student data.
        """
        pass

    def add_student(self, student: str) -> bool:
        """
        Add student to the file. Return True if success else False
        """
        pass
    
    def get_student_by_id(self, student_id: str) -> Student | None:
        """
        Return student given student id if exists else None.
        """
        pass
    
    def remove_student(self, student_id: str) -> bool:
        """
        Remove student from the file. Return True if success else False.
        """
        pass

