document.addEventListener('DOMContentLoaded', () => {

    // Connect to websocket
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

    // When connected, configure button
    socket.on('connect', () => {

        // 'Enter' key on textarea also sends a message
        // https://developer.mozilla.org/en-US/docs/Web/Events/keydown
        document.querySelector('#comment').addEventListener("keydown", event => {
            if (event.code == "Enter") {
                document.getElementById("send-button").click();
            }
        });
        
        // Send button should emit a "message sent" event
        document.querySelector('#send-button').addEventListener("click", () => {
            const data = document.getElementById("comment").value;
            socket.emit('send message', {'data': data});
            
            // Clear textarea
            document.getElementById("comment").value = '';
        });
    });
    
    // When a message is announced, add it to the DOM
    socket.on('announce message', msg => {
        const li = document.createElement('li');
        li.innerHTML = `New message: ${msg.msg}`;
        document.querySelector('#messages').append(li)
    })
});