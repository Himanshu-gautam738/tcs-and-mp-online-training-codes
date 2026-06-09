import re

def check_password(password):
    if len(password) < 8:
        return "Weak"

    if not re.search(r"[A-Z]", password):
        return "Weak"

    if not re.search(r"[a-z]", password):
        return "Weak"

    if not re.search(r"[0-9]", password):
        return "Weak"

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Weak"

    return "Strong"


pwd = input("Enter Password: ")
print(check_password(pwd))