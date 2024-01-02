from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn
from pydantic import BaseModel

app = FastAPI()
templates = Jinja2Templates(directory="templates")

current_function = 'Solid'

@app.get("/", response_class=HTMLResponse)
def test():
    with open("homepage.html") as page:
        return page.read()

@app.get("/API")
def tell_the_lights(r,g,b):
     pass

@app.get("/solid", response_class=HTMLResponse)
def solid_get(request: Request, R:int = 0, G:int = 0, B:int = 0):
    global current_function
    return templates.TemplateResponse(
        name="subpage.html", context={"request": request, "R": R, "G": G, "B": B, 'function': current_function}
        )

@app.post("/solid", response_class=HTMLResponse)
def solid_post(request: Request, R: int = Form(...), G: int = Form(...), B: int = Form(...)):
    global current_function
    print(R,G,B)
    return solid_get(request, R, G, B)

@app.get("/aura", response_class=HTMLResponse)
def aura_get():
        return "BEANs"

@app.get("/flash", response_class=HTMLResponse)
def flash_get():
        return "BEANs"

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')