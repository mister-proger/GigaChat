from django.http import HttpResponse
import sqlite3


class DBOperator:
    db_connect = sqlite3.connect(r'E:\Projects\GigaChat\server\test.db', check_same_thread=False)

    @staticmethod
    def check_user(login):
        pass

    @staticmethod
    def register_user(login, password):

        cursor = DBOperator.db_connect.cursor()

        cursor.execute("SELECT MAX(id) FROM users")
        max_id = cursor.fetchone()[0]
        if max_id is None:
            next_id = 1
        else:
            next_id = max_id + 1

        cursor.execute("INSERT INTO users (id, login, password) VALUES (?, ?, ?)",
                       (next_id, login, password))

        DBOperator.db_connect.commit()

        return next_id

    @staticmethod
    def auth_user(login, password):
        cursor = DBOperator.db_connect.cursor()
        cursor.execute("SELECT id FROM users WHERE login=? AND password=?", (login, password))
        row = cursor.fetchone()
        if row:
            return row[0]
        else:
            return None


def register(request):
    data = dict(request.GET)
    login = data.get('login', None)
    password = data.get('password', None)
    if login is not None and password is not None:
        login = login[0];
        password = password[0]
    else:
        return HttpResponse("Ошибка в параметрах запроса!")

    _id = DBOperator.register_user(login, password)

    return HttpResponse(f"Ваш ID | {_id} |")


def auth(request):
    data = dict(request.GET)
    login = data.get('login', None)
    password = data.get('password', None)
    if login is not None and password is not None:
        login = login[0];
        password = password[0]

    response = DBOperator.check_user(login, password)

    if response is not None:
        return HttpResponse(f"Авторизация прошла успешно, ваш ID | {response} |")
    else:
        return HttpResponse("Неверное имя пользователя или пароль")


def index(request):
    print(request.GET)
    print(request.POST)
    return HttpResponse("Hello, world. You're at the polls index.")
