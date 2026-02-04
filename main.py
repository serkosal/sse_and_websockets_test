from asyncio import sleep

from fastapi import FastAPI, Request, WebSocket
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import StreamingResponse
from fastapi.templating import Jinja2Templates

import requests

app = FastAPI()

app.mount('/static', StaticFiles(directory='static'), name='static')

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index(req: Request):
    
    return templates.TemplateResponse(
        request=req, name='index.html', context={"title": "Index page"}
    )
    
# region SSE

@app.get("/sse/", response_class=HTMLResponse)
async def sse(req: Request):
    
    return templates.TemplateResponse(
        request=req, 
        name='sse.html', 
        context={"title": "Server-sent events demo"}
    )


async def chuck_norris_jokes_generator():
    
    for _ in range(10):
        req = requests.get('https://api.chucknorris.io/jokes/random')
        
        if req.ok:
            data = f'{req.text}'
        else:
            data = "An error occured! We couldn't handle the joke!"
        
        yield f'data: {data}\n\n'
            
        await sleep(2)
        
    yield "event: done\ndata: finished\n\n"

@app.get("/sse/run/")
async def sse_run(req: Request):
    
    return StreamingResponse(
        chuck_norris_jokes_generator(), 
        media_type='text/event-stream'
    )

# endregion

# region Web-Sockets

@app.get("/ws", response_class=HTMLResponse)
async def ws(req: Request):
    
    return templates.TemplateResponse(
        request=req, name='ws.html', context={"title": "Web-Sockets demo"}
    )

@app.websocket("/ws/run")
async def ws_run(ws: WebSocket):
    await ws.accept()

    for i in range(10):
        await ws.send_text(str(i))
        await sleep(2)

    await ws.close()
    

# endregion 
