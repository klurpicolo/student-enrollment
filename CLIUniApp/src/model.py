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

    def generate_id(self) -> int:
        digits = random.randint(1,999)
        with_leading_zero = str(digits).zfill(3)
        return with_leading_zero

    def generate_mark(self):
        random_mark = random.randint(25, 100)
        return random_mark
    
    def __eq__(self, other): 
        if not isinstance(other, Subject):
            return False
        return self.id == other.id and self.mark == other.mark and self.grade == other.grade

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

    def __init__(self, name: str, email: str, password: str):
        self.id = self.generate_id()
        self.name = name
        self.email = email
        self.password = password
        self.enrol_subjects: list[Subject] = []

    def generate_id(self):
        digits = random.randint(1, 999999)
        with_leading_zero = str(digits).zfill(6)
        return with_leading_zero
    
    def enroll(self, subject: Subject) -> bool:
        if len(self.enrol_subjects) >= 4:
            return False
        self.enrol_subjects.append(subject)
    
    def withdraw_subject(self, to_remove_subject: Subject) -> bool:
        for enrol_subject in self.enrol_subjects:
            if enrol_subject == to_remove_subject:
                self.enrol_subjects.remove(to_remove_subject)
                return True
        return False
