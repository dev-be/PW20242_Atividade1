from sql.produto_sql import SQL_CRIAR_TABELA, SQL_INSERIR
from models.produto_model import Produto
from util import obter_conexao

def criar_tabela():
    conexao = obter_conexao()
    cursor = conexao.cursor()
    cursor.execute(SQL_CRIAR_TABELA)
    conexao.commit()
    conexao.close()

def inserir(produto: Produto):
    conexao = obter_conexao()
    cursor = conexao.cursor()
    cursor.execute(SQL_INSERIR, (produto.nome, produto.descricao, produto.estoque, produto.preco, produto.categoria))
    conexao.commit()
    conexao.close()

def obter_todos():
    conexao = obter_conexao()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM produto")
    produtos = [Produto(*linha) for linha in cursor.fetchall()]
    conexao.close()
    return produtos
