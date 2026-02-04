const ws = new WebSocket('/ws/run');

const cont = document.getElementById("ws-container");

ws.addEventListener('open', (_) => {
    console.debug('ws opened');
});

ws.addEventListener('error', (ev) => {
    console.debug('error', ev);
});

ws.addEventListener('close', (_) => {
    console.debug('ws closed')
})

ws.addEventListener('message', (ev) => {

    const el = document.createElement('li');

    el.textContent = ev.data;

    cont.appendChild(el);
});
