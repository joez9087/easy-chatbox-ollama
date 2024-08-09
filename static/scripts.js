// static/scripts.js
document.getElementById('chat-form').addEventListener('submit', async function(event) {
    event.preventDefault();
    
    const formData = new FormData(this);
    
    const response = await fetch('/chat', {
        method: 'POST',
        body: formData
    });

    const data = await response.json();
    const chatOutput = document.getElementById('chat-output');
    const newMessage = document.createElement('div');
    newMessage.textContent = data.response;
    chatOutput.appendChild(newMessage);
});
