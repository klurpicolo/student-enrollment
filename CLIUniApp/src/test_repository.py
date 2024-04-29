import unittest
import os

from model import Student, Subject
from repository import StudentRepository

class TestStudentRepository(unittest.TestCase):

    def setUp(self):
        self.data_file = "./data/student.data"
        self.repo = StudentRepository(self.data_file)
        self.sample_students = [
            Student("1", "Alice", 20),
            Student("2", "Bob", 21),
            Student("3", "Charlie", 22)
        ]

    # def test_file_path_does_not_exist(self):
    #     with self.assertRaises(Exception):
    #         StudentRepository("nonexistent/path/student.data")

    def test_get_all_students_empty(self):
        self.assertEqual(self.repo.get_all_students(), [])

    def test_add_student(self):
        for student in self.sample_students:
            self.assertTrue(self.repo.add_student(student))

    def test_get_student_by_id(self):
        for student in self.sample_students:
            self.repo.add_student(student)
            self.assertEqual(self.repo.get_student_by_id(student.id), student)

    def test_get_student_by_id_not_found(self):
        self.assertIsNone(self.repo.get_student_by_id("nonexistent_id"))

    def test_remove_student(self):
        for student in self.sample_students:
            self.repo.add_student(student)
            self.assertTrue(self.repo.remove_student(student.id))

    def test_remove_student_not_found(self):
        self.assertFalse(self.repo.remove_student("nonexistent_id"))

    def test_update_existing_student_found(self):
        student = Student("klur", "klur@gmail.com", "12345")
        student_id = student.id

        updated_student = Student("klur", "klur@gmail.com", "12345")
        updated_student.id = student_id
        updated_student.enrol_subjects.append(Subject())

        self.repo.add_student(student)
        self.assertTrue(self.repo.update_student(updated_student))

        retrieved_student = self.repo.get_student_by_id(student_id)
        self.assertEqual(len(retrieved_student.enrol_subjects), 1)


if __name__ == '__main__':
    unittest.main()
