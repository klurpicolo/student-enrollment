import re


def validate_password(password):
    """
    Will return true if password pattern matches password input.

    Password:
    - Start with upper case
    - Minimum 6 letters
    - Following by minimum 3-digits
    """
    password_pattern = r"^[A-Z][a-zA-Z]{5,}[0-9]{3,}$"
    return re.match(password_pattern, password)


def validate_email(email):
    """
    Will return true if email pattern matches email input.

    Email:
    - Contains '@university.com'
    """
    email_pattern = r"^[a-zA-Z]+[.][a-zA-Z]+@university[.]com$"
    return re.match(email_pattern, email)
