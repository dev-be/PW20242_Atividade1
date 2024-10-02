@dataclass
class Usuario:
    id: Optional[int] = None
    nome: Optional[str] = None
    descricao: Optional[str] = None
    estoque: Optional[int] = None
    preco: Optional[int] = None
    categoria: Optional[str] = None