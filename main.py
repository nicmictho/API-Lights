from fastapi import FastAPI, Form
from typing import Annotated
from fastapi.responses import HTMLResponse
import uvicorn
from pydantic import BaseModel

app = FastAPI()

class Colour(BaseModel):
      R:int
      G:int
      B:int

@app.get("/", response_class=HTMLResponse)
def test():
    with open("homepage.html") as page:
        return page.read()

@app.get("/solid", response_class=HTMLResponse)
def solid_get():
        with open("subpages\solid.html") as page:
            return page.read()
        
@app.post("/solid")
def solid_post(fname):
    return fname


@app.get("/aura", response_class=HTMLResponse)
def aura_get():
        return "BEANs"

@app.get("/flash", response_class=HTMLResponse)
def flash_get():
        return "BEANs"

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')