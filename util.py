from datetime import datetime
import sqlite3

NOME_PASTA_HTML='html/'
NOME_PASTA_CONTATOS = "dados/cadastros_estoque/"
NOME_PASTA_CADASTRO = "dados/cadastros_estoque/"

def ler_html(nome_arquivo:str) -> str:
    caminho = f"{NOME_PASTA_HTML}{nome_arquivo}.html"
    with open(caminho, "r", encoding="utf-8") as arquivo:
        conteudo_html = arquivo.read()
    return conteudo_html


def salvar_contato(nome, descricao, estoque, preco):
    agora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nome_arquivo = f"{NOME_PASTA_CONTATOS}{agora}cadastro.txt"
    conteudo = f"Nome: {nome}\nDescrição: {descricao}\nEstoque: {estoque}\nPreço: {preco}\n"
    with open(nome_arquivo, "w") as arquivo:
        arquivo.write(conteudo)

def salvar_cadastro(nome, descricao, estoque, preco, categoria):
    agora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nome_arquivo = f"{NOME_PASTA_CADASTRO}{agora}cadastro_.txt"
    conteudo = f"Nome: {nome}\nDescrição: {descricao}\nEstoque:{estoque}\nSenha:{preco}\nCategoria:{categoria}"
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(conteudo)

def obter_conexao():
    return sqlite3.connect("dados.db")