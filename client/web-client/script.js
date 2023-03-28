const socket = new WebSocket('ws://localhost:8080');

// функция для добавления нового сообщения в чат
function addMessage(dataJson) {
  const data = JSON.parse(dataJson);
  const messageEl = document.createElement('div');
  messageEl.classList.add('message');
  let messageText = `[${new Date(data.time * 1000).toLocaleTimeString()}] `;
  if (data.recipient === 'all') { 
    messageText += `${data.sender}: `;
  } else {
    messageText += `${data.sender} -> ${data.recipient}: `;
  }
  messageText += data.text;
  messageEl.textContent = messageText;
  messagesEl.appendChild(messageEl);

  messagesEl.scrollTop = messagesEl.scrollHeight;
}


// обрабатываем установку соединения
socket.addEventListener('open', () => {
  console.log('WebSocket connection established.');
});

// обрабатываем прием данных от сервера
socket.addEventListener('message', (event) => {
  const dataJson = event.data;
  addMessage(dataJson);
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
