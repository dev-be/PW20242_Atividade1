from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
def get_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

if __name__ == "__main__":     
    uvicorn.run("main:app", port=8000, reload=True)