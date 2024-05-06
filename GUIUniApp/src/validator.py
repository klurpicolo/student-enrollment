import re


def validate_email(email: str):
    email_pattern = r"^[a-zA-Z]+[.][a-zA-Z]+@university[.]com$"
    return re.match(email_pattern, email)


def validate_password(password: str):
    password_pattern = r"^[A-Z][a-zA-Z]{5,}[0-9]{3,}$"
    return re.match(password_pattern, password)
