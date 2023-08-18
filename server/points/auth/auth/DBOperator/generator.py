import random
import string
import hashlib


def hasher(data):
    return hashlib.sha512(data.encode()).hexdigest()


def gen_token(id):
    return f'user.{id}.' + ''.join(
        random.choice(string.ascii_letters + string.digits) for _ in range(251 - len(str(id)))
    )
