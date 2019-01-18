document.addEventListener('DOMContentLoaded', () => {

    // Connect to websocket
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

    // When connected, configure button
    socket.on('connect', () => {

        // Send button should emit a "message sent" event
        document.querySelector('#send-button').addEventListener("click", () => {
            const data = 'hi';
            socket.emit('send message', {'data': data});
        });
    });
    
    // When a message is announced, add it to the DOM
    socket.on('announce message', msg => {
        const li = document.createElement('li');
        li.innerHTML = `New message: ${msg.msg}`;
        document.querySelector('#messages').append(li)
    })
});