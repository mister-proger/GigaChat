document.addEventListener('DOMContentLoaded', () => {
    // создаем WebSocket-соединение
    const socket = new WebSocket('ws://localhost:8765/');

    // функция для добавления нового сообщения в чат
    function addMessage(jsonStr, time) {
        const data = JSON.parse(jsonStr);
        const message = data.message;

        const messageEl = document.createElement('div');
        messageEl.classList.add('message');
        messageEl.innerHTML = `[${new Date(time * 1000).toLocaleTimeString()}] ${message}`;
        messagesEl.appendChild(messageEl);

        messagesEl.scrollTop = messagesEl.scrollHeight;
        }


    // обрабатываем открытие соединения
    socket.addEventListener('open', (event) => {
        console.log('WebSocket connection established.');
    });

    // обрабатываем сообщения от сервера
    socket.addEventListener('message', (event) => {
        const data = JSON.parse(event.data);
        addMessage(data.message, data.time);
    });

    // обрабатываем отправку сообщения из формы
    const messageForm = document.getElementById('message-form');
    messageForm.addEventListener('submit', (event) => {
        event.preventDefault();
        const messageInput = document.getElementById('message-input');
        const message = messageInput.value;
        // отправляем сообщение, если оно не пустое
        if (message.trim() !== '') {
            const data = {
                message: message
            };
            socket.send(JSON.stringify(data));
            messageInput.value = '';
        }
    });

    // отправляем сообщение на Enter
    const messageInput = document.getElementById('message-input');
    messageInput.addEventListener('keypress', (event) => {
        if (event.key === 'Enter') {
            event.preventDefault();
            sendButton.click();
        }
    });

    // получаем элементы страницы
    const messagesEl = document.getElementById('messages');
    const sendButton = document.getElementById('send-button');
});
