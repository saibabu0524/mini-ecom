import re

def validate_email_password(email, password):
    email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(email_pattern, email):
        return "Invalid email format"


    if len(password) < 8:
        return "Password must be at least 8 characters long"
    if not any(char.isdigit() for char in password):
        return "Password must contain at least one digit"
    if not any(char.islower() for char in password):
        return "Password must contain at least one lowercase letter"
    if not any(char.isupper() for char in password):
        return "Password must contain at least one uppercase letter"
    if not any(char in '!@#$%^&*()-_=+[]{}|;:,.<>?' for char in password):
        return "Password must contain at least one special character"


    return True