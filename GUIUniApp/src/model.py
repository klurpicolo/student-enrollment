import random
from enum import StrEnum


class Grade(StrEnum):
    """
    Grade criteria
        mark < 50 -> Z 
        50 <= mark < 65 -> P
        65 <= mark < 75 -> C 
        75 <= mark < 85 -> D
        mark >= 85 -> HD
    """

    Z = 'Z'
    P = 'P'
    C = 'C'
    D = 'D'
    HD = 'HD'

    @classmethod
    def deserialize(cls, grade):
        if grade == 'Z':
            return cls.Z
        if grade == 'P':
            return cls.P
        if grade == 'C':
            return cls.C
        if grade == 'D':
            return cls.D
        if grade == 'HD':
            return cls.HD

    @classmethod
    def from_mark(cls, mark):
        if mark < 50:
            return cls.Z
        elif 50 <= mark < 65:
            return cls.P
        elif 65 <= mark < 75:
            return cls.C
        elif 75 <= mark < 85:
            return cls.D
        else:
            return cls.HD


class Subject:

    def __init__(self):
        self.id = self.generate_id()
        self.mark = self.generate_mark()
        self.grade = Grade.from_mark(self.mark)

    @classmethod
    def deserialize(cls, raw: dict):
        subject = cls()
        subject.id = raw['id']
        subject.mark = raw['mark']
        subject.grade = Grade.deserialize(raw['grade'])
        return subject

    def to_json(self):
        return {
            'id': self.id,
            'mark': self.mark,
            'grade': self.grade
        }

    def generate_id(self) -> str:
        digits = random.randint(1, 999)
        with_leading_zero = str(digits).zfill(3)
        return with_leading_zero

    def generate_mark(self):
        random_mark = random.randint(25, 100)
        return random_mark

    def __eq__(self, other):
        if not isinstance(other, Subject):
            return False
        return self.id == other.id and self.mark == other.mark and self.grade == other.grade

    def __str__(self) -> str:
        return f'Subject::{self.id}, mark = {self.mark}, grade = {self.grade}'


class Admin:
    """
    Represent Admin
    """

    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name


class Student:
    """
    The Student class has the fields:
        - ID randomly generated 1 <= ID <= 999999, unique and formatted as 6-digits width.
        IDs less than 6-digits width should be completed with zeroes from the left.
        - name, email, password, and a list of subjects
    """

    def __init__(self, name: str, email: str, password: str, enrolled_subjects: list[Subject] = []):
        self.id = self.generate_id()
        self.name = name
        self.email = email
        self.password = password
        self.enrolled_subjects: list[Subject] = enrolled_subjects

    @classmethod
    def deserialize(cls, raw: dict):
        enrolled_subjects = [Subject.deserialize(each) for each in raw['enrolled_subjects']]
        new_student = cls(raw['name'], raw['email'], raw['password'], enrolled_subjects)
        new_student.id = raw['id']
        return new_student

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "enrolled_subjects": [subject.to_json() for subject in self.enrolled_subjects]
        }

    def generate_id(self):
        digits = random.randint(1, 999999)
        with_leading_zero = str(digits).zfill(6)
        return with_leading_zero

    def enroll(self, subject: Subject) -> bool:
        if len(self.enrolled_subjects) >= 4:
            return False
        self.enrolled_subjects.append(subject)
        return True

    def withdraw_subject(self, to_remove_subject: Subject) -> bool:
        for enrol_subject in self.enrolled_subjects:
            if enrol_subject == to_remove_subject:
                self.enrolled_subjects.remove(to_remove_subject)
                return True
        return False

    def __eq__(self, other):
        if not isinstance(other, Student):
            return False
        return self.id == other.id and self.name == other.name and self.email == other.email

    def __str__(self):
        return (f"Student::{self.id}, name = {self.name}, email = {self.email}, "
                f"subject = {[s.__str__() for s in self.enrolled_subjects]}")


if __name__ == "__main__":
    student = Student("123456", "<NAME>", "<EMAIL>", [])
    print(student)
