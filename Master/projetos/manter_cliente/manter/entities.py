from sqlalchemy import (
    Column, Integer, String, Boolean
)

from webapp import db
Base = db.Model

class Fornecedor:
    def __init__(self, nome, cnpj, site, pedidos):
        """ init eh o construtor """
        self.nome = nome
        self.cnpj = cnpj
        self.site = site
        self.pedidos = pedidos

    def exibir(self):
        print(self.nome, self.cnpj, self.site, self.pedidos)


# mapear objeto para o banco de dados:
class Cliente:
    def __init__(self, nome, cpf, email):
        """ init eh o construtor """
        self.nome = nome
        self.cpf = cpf
        self.email = email

    def exibir(self):
        print(self.nome, self.cpf, self.email)

class Produto:
    def __init__(self, nome, descricao, preco, quantidade):
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.quantidade = quantidade

    def exibir(self):
        print(self.nome, self.descricao, self.preco, self.quantidade)

if __name__ == '__main__':
    maria = Cliente("Maria", 939393, "test@org.com")
    julia = Cliente("Julia", 111111, "aaa@org.com")
    print(maria.cpf)
    maria.exibir()
    julia.exibir()
    pasta = Produto("Pasta", "pasta de papeis rosa", 10.50, 23)
    print(pasta.preco)
    pasta.exibir()
    TF_Alimentos = Fornecedor("TF Alimentos", "12345", "tfalimentos.com.br", "15")
    print(TF_Alimentos.cnpj)
    TF_Alimentos.exibir()

