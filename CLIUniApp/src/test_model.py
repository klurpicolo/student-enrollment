import unittest

from model import Student, Admin, Subject 

class TestModels(unittest.TestCase):

    def test_create_object_without_error(self):
        _ = Student("Klur", "wb@gmail.com", "qwert")
        _ = Admin("123", "Goku")
        _ = Subject()

    def test_student_id_should_be_6_length(self):
        student = Student("Klur", "wb@gmail.com", "qwert")
        self.assertEqual(len(student.id), 6)
        
    def test_student_enrol_subjects_max_is_4(self):
        student = Student("Klur", "wb@gmail.com", "qwert")
        self.assertEqual(student.enrol_subjects, [], "Initial enrol subjects should be 0")
        student.enroll(Subject())
        student.enroll(Subject())
        student.enroll(Subject())
        student.enroll(Subject())
        self.assertEqual(len(student.enrol_subjects), 4, "Size should be 4")
        enrollment_result = student.enroll(Subject())
        self.assertEqual(enrollment_result, False, "Should be false because reach maximum")
        self.assertEqual(len(student.enrol_subjects), 4, "Size should still be 4")

if __name__ == '__main__':
    unittest.main()
