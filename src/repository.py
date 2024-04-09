from .model import Student


DATA_FILE = "./data/student.data"

class StudentRepository:

    def __init__(self, init_students = []):
        self.students = init_students

    def get_all_students(self) -> list[Student]:
        return self.students
    
    