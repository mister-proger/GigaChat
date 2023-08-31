import re
from . import DBOperator


def validate_name(name):
    return bool(re.match(r"[a-zA-Z0-9-_.<>{}!]{4,64}", name))


def validate_password(password):
    return bool(re.match(r'(?=.*[0-9])(?=.*[!@#$%^&*])[\w\W]{6,64}', password))


class CheckAvailability:
    @staticmethod
    def username(username):
        return DBOperator.check('username', username)

    @staticmethod
    def email(email):
        return DBOperator.check('email', email)

    @staticmethod
    def phone(phone):
        return DBOperator.check('phone', phone)
