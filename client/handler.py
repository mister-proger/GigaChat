import json
import datetime


def audio(data):

    pass


def mess(data):

    message = json.loads(data[1].decode())

    time = f'<{datetime.datetime.now().strftime("%H:%M")}>'

    if message['recipient'] == 'all':

        opp = message['sender']

    else:

        opp = f"{message['sender']} -> {message['recipient']}"

    return f'window_chat("{time} {opp}: {message["text"]}")'


def command(data):

    comm = data[1].decode()

    if comm == 'users':

        return f"window_chat(f'<{datetime.datetime.now().strftime('%H:%M')}> Подключённые клиенты: {' | '.join([x.decode() for x in data[2:]])}')"

    else:

        return f'window_chat(f"Неизвестный тип пакета: {data[1].decode()}")'
