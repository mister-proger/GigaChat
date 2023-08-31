import random
import string

import bcrypt


class Hasher:
    @staticmethod
    def hash(data):
        return bcrypt.hashpw(data.encode(), bcrypt.gensalt())

    @staticmethod
    def verify(data, hash):
        return bcrypt.checkpw(data.encode(), hash)


def gen_token(id):
    return f'user.{id}.' + ''.join(
        random.choice(string.ascii_letters + string.digits) for _ in range(66 - len(str(id)))
    )
