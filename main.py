from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount('/static', StaticFiles(directory='static'), name='static')

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index(req: Request):
    
    return templates.TemplateResponse(
        request=req, name='index.html', context={"title": "Index page"}
    )
    
@app.get("/sse/", response_class=HTMLResponse)
async def sse(req: Request):
    
    return templates.TemplateResponse(
        request=req, 
        name='sse.html', 
        context={"title": "Server-sent events demo"}
    )
    
@app.get("/ws", response_class=HTMLResponse)
async def ws(req: Request):
    
    return templates.TemplateResponse(
        request=req, name='ws.html', context={"title": "Web-Sockets demo"}
    )