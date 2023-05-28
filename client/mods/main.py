import json
import datetime


def main(data):

    print(data)

    message = json.loads(data[1].decode())

    time = f'<{datetime.datetime.now().strftime("%H:%M")}>'

    if message['recipient'] == 'all':

        opp = message['sender']

    else:

        opp = f"{message['sender']} -> {message['recipient']}"

    return f"{time} {opp}: {message['text']}"
