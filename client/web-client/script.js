document.addEventListener('DOMContentLoaded', () => {
    // создаем TCP-соединение
    const socket = new TcpSocket('127.0.0.1', 1042);

    // функция для добавления нового сообщения в чат
    function addMessage(jsonStr, time) {
        const data = JSON.parse(jsonStr);
        const sender = data.sender;
        const recipient = data.recipient;
        const message = data.text;

        const messageEl = document.createElement('div');
        messageEl.classList.add('message');
        let messageText = `[${new Date(time * 1000).toLocaleTimeString()}] `;
        if (recipient === 'all') {
            messageText += `${sender}: `;
        } else {
            messageText += `${sender} -> ${recipient}: `;
        }
        messageText += message;
        messageEl.textContent = messageText;
        messagesEl.appendChild(messageEl);

        messagesEl.scrollTop = messagesEl.scrollHeight;
    }

    // обрабатываем установку соединения
    socket.onconnect = () => {
        console.log('TCP connection established.');
        socket.send('BRW');
    };

    // обрабатываем прием данных от сервера
    socket.ondata = (event) => {
        const data = JSON.parse(event.data);
        addMessage(data.message, data.time);
    };

    // обрабатываем отправку сообщения из формы
    const messageForm = document.getElementById('message-form');
    messageForm.addEventListener('submit', (event) => {
        event.preventDefault();
        const messageInput = document.getElementById('message-input');
        const message = messageInput.value;
        // отправляем сообщение, если оно не пустое
        if (message.trim() !== '') {
            const data = {
                type: 'mess',
                sender: 'BRW',
                text: message,
                recipient: 'all'
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
