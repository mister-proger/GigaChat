import re


def validate_name(name):
    return bool(re.match(r"[a-zA-Z0-9-_.<>{}!]{4,64}", name))


def validate_password(password):
    return bool(re.match(r'(?=.*[0-9])(?=.*[!@#$%^&*])[\w\W]{6,64}', password))
