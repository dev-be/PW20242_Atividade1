SQL_CRIAR_TABELA = """
    CREATE TABLE IF NOT EXISTS produto (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(50) NOT NULL,
        descricao VARCHAR(100) NOT NULL UNIQUE,
        estoque Integer NOT NULL UNIQUE,
        preco float DATE NOT NULL,
        categoria VARCHAR(50) NOT NULL
    )
"""

SQL_INSERIR = """
    INSERT INTO produto (
        nome, descricao, estoque, preco, categoria)
    VALUES (?, ?, ?, ?, ?)
"""

SQL_EXCLUIR = """
    DELETE FROM USUARIO
    WHERE id=?
"""