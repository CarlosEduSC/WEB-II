DROP TABLE IF EXISTS cliente;
DROP TABLE IF EXISTS produtos;
DROP TABLE IF EXISTS fornecedor;

CREATE TABLE cliente(
    id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    nome text NOT NULL,
    cpf text NOT NULL,
    email text NOT NULL,
    data_cadastro TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE produtos(
    id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    nome text NOT NULL,
    descricao text NOT NULL,
    preco float NOT NULL,
    quantidade int not null,
    data_cadastro TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    constraint fk_produtos foreign key (idFornecedor)
        references Fornecedor(idFornecedor)
);

CREATE TABLE fornecedor(
    idFornecedor integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    nome text NOT NULL,
    cnpj text not null unique,
    site text NOT NULL,
    pedidos int default=0,
    is_active boolean default=true,
    data_cadastro TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    constraint pk_fornecedor primary key (id)
);

INSERT INTO cliente (nome, cpf, email)
VALUES
    ('admin', '1002000', 'admin@test.org'),
    ("Maria Silver", "949.282.111-82", "mariam@test.org"),
    ("Jairo Carlile", "144.217.577-11", "carlile@test.org"),
    ("Marcos Oliva", "433.144.644-52", "marcos@test.org");

INSERT INTO produtos (nome, descricao, preco, quantidade)
VALUES
    ('Caneta', 'Caneta bic', '23.5', '12'),
    ("Lapis", 'Lapis fabbercasttle', "9.10", "29"),
    ("Caderno", 'caderno de surfista', "30.0", "18"),
    ("Borracha",'borracha apaga tudo', "5.25", "30");

INSERT INTO fornecedor (nome, cnpj, site, pedidos)
VALUES
    ('admin', '1002000', 'admin.com.br', '12'),
    ("Silver", "949.282.111-82", "silver.com.br", '13'),
    ("ghost", "144.217.577-11", "ghost.com.br", '14'),
    ("Oliva enlatados", "433.144.644-52", "olivaenlatados.com.br", '15');

