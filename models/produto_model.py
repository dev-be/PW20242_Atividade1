from dataclasses import dataclass

@dataclass
class Produto:
    id: int = None
    nome: str = None
    descricao: str = None
    estoque: int = None
    preco: float = None
    categoria: str = None
