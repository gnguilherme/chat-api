// frontend/script.js
document.getElementById('send-button').addEventListener('click', async () => {
    const userInput = document.getElementById('user-input').value;
    const messagesDiv = document.getElementById('messages');

    messagesDiv.innerHTML += `<div>You: ${userInput}</div>`;
    document.getElementById('user-input').value = '';

    const response = await fetch('http://localhost:8000/chat/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ user_message: userInput }),
    });

    const data = await response.json();
    messagesDiv.innerHTML += `<div>Bot: ${data.response}</div>`;
});