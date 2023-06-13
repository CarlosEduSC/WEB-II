from manter.database import Database

class DaoCliente:
    """
    dao == Data Access Object ou persistence
    Implementa operacoes "CRUD"
        - Create
        - Read
        - Update
        - Delete
    """
    def save(self, cliente):    # C
        conn = Database.get_connection()
        conn.execute(
            f"""
            INSERT INTO cliente (nome, cpf, email )
            VALUES (?, ?, ?)
            """,
            ( cliente.nome, cliente.cpf, cliente.email )
        )
        conn.commit()

    def find(self):    # R
        pass
    def update(self, cliente):  # U
        conn = Database.get_connection()
        conn.execute(
            f"""
            UPDATE cliente SET nome = ?, cpf = ? , email = ?
            WHERE id = ?
            """,
            (cliente.nome, cliente.cpf, cliente.email, cliente.id)
        )
        conn.commit()

    def delete(self, id):  # D
        conn = Database.get_connection()
        conn.execute(
            f"""
            DELETE from cliente
            WHERE id = ?    
            """, (id)
        )
        conn.commit()

    def find_by_id(self, id): # R
        # pegar da Database a conexao com o BD
        conn = Database.get_connection()
        res = conn.execute(
            "SELECT * FROM cliente where id = ?",
            (id)
        )
        return res.fetchone()

    def findall(self): # R
        # pegar da Database a conexao com o BD
        conn = Database.get_connection()
        res = conn.execute(
            "SELECT * FROM cliente"
        )
        return res.fetchall()

class DaoProduto:
    """
    dao == Data Access Object ou persistence
    Implementa operacoes "CRUD"
        - Create
        - Read
        - Update
        - Delete
    """
    def save(self, produtos):    # C
        conn = Database.get_connection()
        conn.execute(
            f"""
            INSERT INTO produtos (nome, descricao, preco, quantidade )
            VALUES (?, ?, ?, ?)
            """,
            (produtos.nome, produtos.descricao, produtos.preco, produtos.quantidade)
        )
        conn.commit()

    def find(self):    # R
        pass
    def update(self, produtos):  # U
        conn = Database.get_connection()
        conn.execute(
            f"""
            UPDATE produtos SET nome = ?, descricao = ? , preco = ?, quantidade = ?
            WHERE id = ?
            """,
            (produtos.nome, produtos.descricao, produtos.preco, produtos.quantidade, produtos.id)
        )
        conn.commit()

    def delete(self, id):  # D
        conn = Database.get_connection()
        conn.execute(
            f"""
            DELETE from produtos
            WHERE id = ?    
            """, (id)
        )
        conn.commit()

    def find_by_id(self, id): # R
        # pegar da Database a conexao com o BD
        conn = Database.get_connection()
        res = conn.execute(
            "SELECT * FROM produtos where id = ?",
            (id)
        )
        return res.fetchone()

    def findall(self): # R
        # pegar da Database a conexao com o BD
        conn = Database.get_connection()
        res = conn.execute(
            "SELECT * FROM produtos"
        )
        return res.fetchall()

class DaoFornecedor:
    """
    dao == Data Access Object ou persistence
    Implementa operacoes "CRUD"
        - Create
        - Read
        - Update
        - Delete
    """
    def save(self, fornecedor):    # C
        conn = Database.get_connection()
        conn.execute(
            f"""
            INSERT INTO fornecedor (nome, cnpj, site, pedidos )
            VALUES (?, ?, ?, ?)
            """,
            (fornecedor.nome, fornecedor.cnpj, fornecedor.site, fornecedor.pedidos)
        )
        conn.commit()

    def find(self):    # R
        pass
    def update(self, fornecedor):  # U
        conn = Database.get_connection()
        conn.execute(
            f"""
            UPDATE fornecedor SET nome = ?, cnpj = ? , site = ?, pedidos = ?
            WHERE idFornecedor = ?
            """,
            (fornecedor.nome, fornecedor.cnpj, fornecedor.site, fornecedor.pedidos, fornecedor.idFornecedor)
        )
        conn.commit()

    def delete(self, idFornecedor):  # D
        conn = Database.get_connection()
        conn.execute(
            f"""
            DELETE from fornecedor
            WHERE idFornecedor = ?    
            """, (idFornecedor)
        )
        conn.commit()

    def find_by_id(self, idFornecedor): # R
        # pegar da Database a conexao com o BD
        conn = Database.get_connection()
        res = conn.execute(
            "SELECT * FROM fornecedor where idFornecedor = ?",
            (idFornecedor)
        )
        return res.fetchone()

    def findall(self): # R
        # pegar da Database a conexao com o BD
        conn = Database.get_connection()
        res = conn.execute(
            "SELECT * FROM fornecedor"
        )
        return res.fetchall()
