import datetime

import psycopg2

try:
    from . import generator
except ImportError:
    import generator

_password = 'pRN|$jZAKC@XefDBaTxdkQoOWi5VuvbFl~m*U1H0tRsa*oeUDypN@Z#4~xGg@O@F'

connection = psycopg2.connect(host='localhost', port=5432, user='postgres', password=_password)


# debug
def drop_all_tables():
    with connection.cursor() as cursor:
        cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public';")

        for table in cursor.fetchall():
            cursor.execute("DROP TABLE IF EXISTS %s CASCADE" % (table[0],))

    connection.commit()


# debug
def check_all_tables():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM information_schema.tables WHERE table_schema='public';")

        for table in cursor.fetchall():
            cursor.execute(f"select * from {table[2]}")
            print(cursor.fetchall())


# debug
def setup():
    drop_all_tables()

    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE accounts (
            id SERIAL PRIMARY KEY,
            username TEXT UNIQUE,
            confirmation INTEGER DEFAULT 1,
            password TEXT NOT NULL,
            email TEXT UNIQUE,
            emails TEXT[],
            phone TEXT UNIQUE
        )
    ''')

    cursor.execute('''
        CREATE TABLE changes (
            account_id INTEGER PRIMARY KEY,
            nickname TIMESTAMP[],
            password TIMESTAMP[],
            avatar TIMESTAMP[],
            FOREIGN KEY (account_id) REFERENCES accounts (id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE tokens (
            account_id INTEGER NOT NULL,
            agent TEXT NOT NULL,
            token TEXT NOT NULL,
            last_login TIMESTAMP,
            start TIMESTAMP NOT NULL,
            ending TIMESTAMP,
            FOREIGN KEY (account_id) REFERENCES accounts (id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE ttokens (
            account_id INTEGER NOT NULL,
            token TEXT NOT NULL,
            extradition TIMESTAMP NOT NULL,
            target TEXT NOT NULL,
            intentions TEXT NOT NULL,
            comments TEXT[],
            FOREIGN KEY (account_id) REFERENCES accounts (id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE profiles (
            account_id INTEGER NOT NULL,
            username TEXT NOT NULL,
            nickname TEXT NOT NULL,
            fast_avatar BYTEA,
            FOREIGN KEY (account_id) REFERENCES accounts (id),
            FOREIGN KEY (username) REFERENCES accounts (username)
        )
    ''')

    cursor.execute('''
        CREATE TABLE channels (
            id SERIAL PRIMARY KEY,
            owner INTEGER NOT NULL,
            users INTEGER[],
            rights INTEGER[][],
            name TEXT NOT NULL,
            description TEXT NOT NULL,
            created TIMESTAMP NOT NULL,
            pinned INTEGER[],
            FOREIGN KEY (owner) REFERENCES accounts (id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE messages (
            id SERIAL PRIMARY KEY,
            channel INTEGER NOT NULL,
            author INTEGER NOT NULL,
            type CHAR(1) NOT NULL,
            text_content TEXT,
            bytea_content BYTEA,
            attachments INTEGER[],
            shipped TIMESTAMP NOT NULL,
            forwarded INTEGER,
            FOREIGN KEY (channel) REFERENCES channels (id),
            FOREIGN KEY (author) REFERENCES accounts (id)
        )
    ''')

    connection.commit()


def register(login, password, *, email=None, phone=None):
    cursor = connection.cursor()

    cursor.execute('''
        INSERT INTO accounts (username, password, email, phone)
        VALUES (%s, %s, %s, %s)
    ''', (login, generator.Hasher.hash(password).decode(), email, phone))

    cursor.execute('''
        SELECT id
        FROM accounts
        WHERE username = %s
    ''', (login,))

    try:
        id = cursor.fetchone()[0]
    except TypeError:
        return
    else:
        cursor.execute('''
            INSERT INTO changes (account_id, nickname, password)
            VALUES (%s, %s, %s)
        ''', (id, [datetime.datetime.now()], [datetime.datetime.now()]))

        connection.commit()

        return id


def auth(login_type, login, password):
    cursor = connection.cursor()

    match login_type:
        case 'username':
            cursor.execute('''
                SELECT password
                FROM accounts
                WHERE username = %s
            ''', (login,))
        case 'email':
            cursor.execute('''
                SELECT password
                FROM accounts
                WHERE email = %s
            ''', (login,))
        case 'phone':
            cursor.execute('''
                SELECT password
                FROM accounts
                WHERE phone = %s
            ''', (login,))
        case _:
            raise ValueError(f'Unknown login type: {login_type}')

    try:
        return generator.Hasher.verify(password, cursor.fetchone()[0].encode())
    except TypeError:
        return None


def check(login_type, login):
    cursor = connection.cursor()

    match login_type:
        case 'username':
            cursor.execute('''
                SELECT id
                FROM accounts
                WHERE username = %s
            ''', (login,))
        case 'email':
            cursor.execute('''
                SELECT id
                FROM accounts
                WHERE email = %s
            ''', (login,))
        case 'phone':
            cursor.execute('''
                SELECT id
                FROM accounts
                WHERE phone = %s
            ''', (login,))
        case _:
            raise ValueError(f'Unknown login type: {login_type}')

    try:
        return bool(cursor.fetchone())
    except TypeError:
        return False


def create_token(agent, id):
    cursor = connection.cursor()

    token = generator.gen_token(id)

    cursor.execute('''
        INSERT INTO tokens (account_id, agent, token, start)
        VALUES (%s, %s, %s, %s)
    ''', (id, agent, generator.Hasher.hash(token).decode(), datetime.datetime.now()))

    connection.commit()

    return token


def auth_token(id, token):
    cursor = connection.cursor()

    cursor.execute('''
        SELECT token
        FROM tokens
        WHERE account_id = %s
    ''', (id,))

    try:
        hash = cursor.fetchone()[0]
    except TypeError:
        return False
    else:
        return generator.Hasher.verify(token, hash.encode())
