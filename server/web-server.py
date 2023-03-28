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
            print(message)
            for connection in connections:
                await connection.send(message)
    finally:
        # удаляем соединение из списка при отключении клиента
        connections.remove(websocket)

# запускаем сервер
async def main():
    async with websockets.serve(handler, "localhost", 8080):
        await asyncio.Future()  # бесконечный цикл

asyncio.run(main())
