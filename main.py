from fastapi import FastAPI, Form
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from starlette.responses import RedirectResponse
import uvicorn
from models.produto_model import Produto
from repositories.produto_repo import criar_tabela, inserir
from util import obter_conexao

criar_tabela()

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/cadastro")
async def get_cadastro(request: Request):
    return templates.TemplateResponse("cadastro.html", {"request": request})

@app.post("/post_cadastro")
async def post_cadastro(
    nome: str = Form(...),
    descricao: str = Form(...),
    estoque: int = Form(...),
    preco: float = Form(...),
    categoria: str = Form(...)
):
    produto = Produto(nome=nome, descricao=descricao, estoque=estoque, preco=preco, categoria=categoria)
    try:
        inserir(produto)
        return RedirectResponse(url="/cadastro_recebido", status_code=303)
    except Exception as e:
        print(f"Erro ao inserir produto: {e}")
        return RedirectResponse(url="/cadastro", status_code=303)


@app.get("/cadastro_recebido")
async def cadastro_recebido(request: Request):
    return templates.TemplateResponse("cadastro_recebido.html", {"request": request})

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
