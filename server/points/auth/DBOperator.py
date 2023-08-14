import psycopg2
import generator


connection = psycopg2.connect(host='localhost', port=5432, user='postgres', password=_password)


# debug
def drop_all_tables():

    with connection.cursor() as cursor:
        cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public';")

        for table in cursor.fetchall():
            sql = "DROP TABLE IF EXISTS %s CASCADE" % (table[0])
            cursor.execute(sql)

    connection.commit()


# debug
def check_all_tables():
    with connection.cursor() as cursor:
        cursor.execute("select * from information_schema.tables WHERE table_schema='public';")

        for table in cursor.fetchall():
            cursor.execute(f"select * from {table[2]}")
            print(cursor.fetchall())


# debug
def setup():
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
            name TIMESTAMP,
            nickname TIMESTAMP,
            password TIMESTAMP,
            avatar TIMESTAMP,
            FOREIGN KEY (id) REFERENCES users(id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE tokens (
            id INTEGER PRIMARY KEY,
            client TEXT NOT NULL,
            token TEXT NOT NULL,
            FOREIGN KEY (id) REFERENCES users(id)
        )
    ''')

    connection.commit()


def register(login, password, *, email = None, phone = None):
    cursor = connection.cursor()

    cursor.execute('''
        INSERT INTO users (name, password, email, phone) VALUES (%s, %s, %s, %s)
    ''', (login, password, email, phone))

    connection.commit()

    return check('name', login)


def auth(login_type, login, password):
    cursor = connection.cursor()

    cursor.execute(f'''
        SELECT password FROM users WHERE %s = %s
    ''', (login_type, login))

    return cursor.fetchone()[0] == generator.hash(password)


def check(login_type, login):
    cursor = connection.cursor()

    cursor.execute(f'''
        SELECT id FROM users WHERE {login_type} = %s
    ''', (login,))

    return cursor.fetchone()[0]
