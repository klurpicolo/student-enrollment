import unittest

from model import Student, Admin, Subject, Grade


class TestModels(unittest.TestCase):

    def setUp(self):
        self.sample_subjects = [
            Subject(), Subject(), Subject()
        ]

    def test_create_object_without_error(self):
        _ = Student("Klur", "wb@gmail.com", "qwert")
        _ = Admin("123", "Goku")
        _ = Subject()

    def test_student_id_should_be_6_length(self):
        student = Student("Klur", "wb@gmail.com", "qwert")
        self.assertEqual(len(student.id), 6)
        
    def test_student_enrol_subjects_max_is_4(self):
        student = Student("Klur", "wb@gmail.com", "qwert")
        self.assertEqual(student.enrolled_subjects, [], "Initial enrol subjects should be 0")
        student.enroll(Subject())
        student.enroll(Subject())
        student.enroll(Subject())
        student.enroll(Subject())
        self.assertEqual(len(student.enrolled_subjects), 4, "Size should be 4")
        enrollment_result = student.enroll(Subject())
        self.assertEqual(enrollment_result, False, "Should be false because reach maximum")
        self.assertEqual(len(student.enrolled_subjects), 4, "Size should still be 4")

    def test_student_deserialize(self):
        # Create a sample JSON data
        json_data = {
            "id": "123456",
            "name": "John Doe",
            "email": "john@example.com",
            "password": "password123",
            "enrolled_subjects": [
                {"id": "001", "mark": 80, "grade": "HD"},
                {"id": "002", "mark": 60, "grade": "C"}
            ]
        }
        deserialized_student = Student.deserialize(json_data)
        self.assertEqual(deserialized_student.id, "123456")
        self.assertEqual(deserialized_student.name, "John Doe")
        self.assertEqual(deserialized_student.email, "john@example.com")
        self.assertEqual(deserialized_student.password, "password123")
        self.assertEqual(len(deserialized_student.enrolled_subjects), 2)
        self.assertEqual(deserialized_student.enrolled_subjects[0].id, "001")
        self.assertEqual(deserialized_student.enrolled_subjects[0].mark, 80)
        self.assertEqual(deserialized_student.enrolled_subjects[0].grade, Grade.HD)
        self.assertEqual(deserialized_student.enrolled_subjects[1].id, "002")
        self.assertEqual(deserialized_student.enrolled_subjects[1].mark, 60)
        self.assertEqual(deserialized_student.enrolled_subjects[1].grade, Grade.C)

    def test_to_json(self):
        subject = Subject()
        subject.id = "001"
        subject.mark = 80
        subject.grade = Grade.HD

        enrolled_subjects = [subject]
        student = Student("John Doe", "john@example.com", "password123", enrolled_subjects)

        json_data = student.to_json()
        self.assertEqual(json_data['name'], "John Doe")
        self.assertEqual(json_data['email'], "john@example.com")
        self.assertEqual(json_data['password'], "password123")
        self.assertEqual(len(json_data['enrolled_subjects']), 1)
        self.assertEqual(json_data['enrolled_subjects'][0]['id'], "001")
        self.assertEqual(json_data['enrolled_subjects'][0]['mark'], 80)
        self.assertEqual(json_data['enrolled_subjects'][0]['grade'], "HD")

    def test_withdraw_existing_subject(self):
        enrolled_subjects = [self.sample_subjects[0], self.sample_subjects[1]]
        student = Student("John Doe", "john@example.com", "password123", enrolled_subjects)

        subject_to_withdraw = self.sample_subjects[0]
        is_withdrawn = student.withdraw_subject(subject_to_withdraw)

        self.assertTrue(is_withdrawn)
        self.assertEqual(len(student.enrolled_subjects), 1)
        self.assertNotIn(subject_to_withdraw, student.enrolled_subjects)


if __name__ == '__main__':
    unittest.main()
