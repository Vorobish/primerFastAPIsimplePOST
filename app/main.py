from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")


@app.post('/register')
async def register(request: Request, username: str = Form()
                   , password: str = Form()) -> HTMLResponse:
    print(username)
    print(password)
    context = {
        'request': request,
        'username': username,
    }
    return templates.TemplateResponse("welcome_user.html", context)

# python -m uvicorn app.main:app
