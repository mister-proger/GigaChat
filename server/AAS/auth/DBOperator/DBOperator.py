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
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name TEXT UNIQUE,
            confirmation INTEGER,
            password TEXT,
            email TEXT UNIQUE,
            emails TEXT[],
            phone TEXT UNIQUE,
            nickname TEXT,
            profile TEXT,
            avatar BYTEA
        )
    ''')

    cursor.execute('''
        CREATE TABLE changes (
            id INTEGER PRIMARY KEY,
            name TIMESTAMP[],
            nickname TIMESTAMP[],
            password TIMESTAMP[],
            avatar TIMESTAMP[],
            FOREIGN KEY (id) REFERENCES users (id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE tokens (
            id INTEGER NOT NULL,
            agent TEXT NOT NULL,
            token TEXT NOT NULL,
            FOREIGN KEY (id) REFERENCES users (id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE channels (
            id SERIAL PRIMARY KEY,
            title TEXT,
            users INTEGER[],
            roles INTEGER[],
            guild INTEGER,
            date TIMESTAMP
        )
    ''')

    cursor.execute('''
        CREATE TABLE messages (
            id SERIAL PRIMARY KEY,
            channel INTEGER UNIQUE,
            sender INTEGER,
            person INTEGER,
            t_data TEXT,
            b_data BYTEA,
            files TEXT[],
            date TIMESTAMP,
            FOREIGN KEY (channel) REFERENCES channels (id)
        )
    ''')

    connection.commit()


def register(login, password, *, email=None, phone=None):
    cursor = connection.cursor()

    cursor.execute('''
        INSERT INTO users (name, password, email, phone) VALUES (%s, %s, %s, %s)
    ''', (login, generator.hasher(password), email, phone))

    connection.commit()

    return check('name', login)


def auth(login_type, login, password):
    cursor = connection.cursor()

    cursor.execute(f'''
        SELECT password FROM users WHERE {login_type} = %s
    ''', (login,))

    return cursor.fetchone() == generator.hasher(password)


def check(login_type, login):
    cursor = connection.cursor()

    cursor.execute(f'''
        SELECT id FROM users WHERE {login_type} = %s
    ''', (login,))

    try:
        return cursor.fetchone()[0]
    except TypeError:
        return None


def create_token(agent, id):
    cursor = connection.cursor()

    token = generator.gen_token(id)

    cursor.execute('''
        INSERT INTO tokens (id, agent, token) VALUES (%s, %s, %s)
    ''', (id, agent, generator.hasher(token)))

    connection.commit()

    return token


def auth_token(token, agent, id):
    cursor = connection.cursor()

    cursor.execute('''
        SELECT *
        FROM tokens
        WHERE id = %s AND agent = %s AND token = %s
    ''', (id, agent, generator.hasher(token)))

    return bool(cursor.fetchone())
