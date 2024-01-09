from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn
from pydantic import BaseModel
import functions

app = FastAPI()
templates = Jinja2Templates(directory="templates")

current_colour = {
     'R': 0,
     'G': 0,
     'B': 0
     }

current_function = 'Solid'
lights: list = [(0,0,0)]*30

@app.get("/", response_class=HTMLResponse)
def test(request: Request):
    global current_colour
    global current_function
    R = current_colour['R']
    G = current_colour['G']
    B = current_colour['B']
    return templates.TemplateResponse(
        name="homepage.html", context={"request": request, "R": R, "G": G, "B": B, 'function': current_function}
    )

@app.get("/API")
def tell_the_lights(current_colour = current_colour):
    return functions.solid(current_colour)

@app.get("/solid", response_class=HTMLResponse)
def solid_get(request: Request, R:int = current_colour['R'], G:int = current_colour['G'], B:int = current_colour['B']):
    global current_function
    R = current_colour['R']
    G = current_colour['G']
    B = current_colour['B']
    print(current_colour)
    print(R,G,B)
    return templates.TemplateResponse(
        name="subpage.html", context={"request": request, "R": R, "G": G, "B": B, 'function': current_function}
        )

@app.post("/solid", response_class=HTMLResponse)
def solid_post(request: Request, R: int = Form(...), G: int = Form(...), B: int = Form(...)):
    global current_function
    global current_colour
    current_function = 'Solid'
    current_colour['R'] = R
    current_colour['G'] = G
    current_colour['B'] = B
    print(R,G,B)
    return solid_get(request, R, G, B)

@app.get("/aura", response_class=HTMLResponse)
def aura_get(request: Request, R:int = current_colour['R'], G:int = current_colour['G'], B:int = current_colour['B']):
    global current_function
    R = current_colour['R']
    G = current_colour['G']
    B = current_colour['B']
    return templates.TemplateResponse(
        name="subpage.html", context={"request": request, "R": R, "G": G, "B": B, 'function': current_function}
        )

@app.post("/aura", response_class=HTMLResponse)
def aura_post(request: Request, R: int = Form(...), G: int = Form(...), B: int = Form(...)):
    global current_function
    global current_colour
    current_function = 'Aura'
    current_colour['R'] = R
    current_colour['G'] = G
    current_colour['B'] = B
    print(R,G,B)
    return aura_get(request, R, G, B)

@app.get("/moving", response_class=HTMLResponse)
def moving_get(request: Request, R:int = current_colour['R'], G:int = current_colour['G'], B:int = current_colour['B']):
    global current_function
    R = current_colour['R']
    G = current_colour['G']
    B = current_colour['B']
    return templates.TemplateResponse(
        name="subpage.html", context={"request": request, "R": R, "G": G, "B": B, 'function': current_function}
        )

@app.post("/moving", response_class=HTMLResponse)
def moving_post(request: Request, R: int = Form(...), G: int = Form(...), B: int = Form(...)):
    global current_function
    global current_colour
    current_function = 'Moving'
    current_colour['R'] = R
    current_colour['G'] = G
    current_colour['B'] = B
    print(R,G,B)
    return moving_get(request, R, G, B)

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')