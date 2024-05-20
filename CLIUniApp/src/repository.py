import json
from model import Student
import os


class StudentRepository:
    def __init__(self, file_path):
        self.file_path = file_path
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w+') as file:
                json.dump([], file, indent=4)

    def load_students(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                return json.load(file)
        raise FileNotFoundError(self.file_path)

    def save_students(self, students):
        try:
            with open(self.file_path, 'w') as file:
                json.dump(students, file, indent=4)
        except FileNotFoundError:
            with open(self.file_path, 'w+') as file:
                json.dump([], file, indent=4)

    def get_all_students(self) -> list[Student]:
        return [Student.deserialize(student_dict) for student_dict in self.load_students()]

    def add_student(self, to_add):
        students = self.load_students()
        students.append(to_add.to_json())
        self.save_students(students)
        return True

    def get_student_by_id(self, student_id):
        students = self.load_students()
        for student_dict in students:
            student = Student.deserialize(student_dict)
            if student.id == student_id:
                return student
        return None

    def remove_student(self, student_id):
        students = self.load_students()
        for student_dict in students:
            student = Student.deserialize(student_dict)
            if student.id == student_id:
                students.remove(student_dict)
                self.save_students(students)
                return True
        return False

    def update_student(self, to_update):
        students = self.load_students()
        for i, student_dict in enumerate(students):
            student = Student.deserialize(student_dict)
            if student.id == to_update.id:
                students[i] = to_update.to_json()
                self.save_students(students)
                return True
        return False

    def clean_database(self):
        self.save_students([])


if __name__ == "__main__":
    repo = StudentRepository(os.getcwd() + '/data/student.data')
    klur = Student("Klur", "wb@gmail.com", "qwert")
    print(repo.add_student(klur))
