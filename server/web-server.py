import asyncio
import json
import websockets

# список соединений клиентов
connections = set()

# функция обработки нового клиентского соединения
async def handler(websocket, path):
    # добавляем новое соединение в список
    connections.add(websocket)
    try:
        # ожидаем сообщения от клиента
        async for message in websocket:
            # добавляем время сообщения и отправляем всем клиентам
            data = {
                'time': asyncio.get_event_loop().time(),
                'message': message
            }
            data_str = json.dumps(data)
            for connection in connections:
                await connection.send(data_str)
    finally:
        # удаляем соединение из списка при отключении клиента
        connections.remove(websocket)

# запускаем сервер
async def main():
    async with websockets.serve(handler, "localhost", 8765):
        await asyncio.Future()  # бесконечный цикл

asyncio.run(main())
