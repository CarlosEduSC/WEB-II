DROP TABLE IF EXISTS cliente;

CREATE TABLE cliente(
    id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    nome text NOT NULL,
    cpf text NOT NULL,
    email text NOT NULL,
    data_cadastro TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO cliente (nome, cpf, email)
VALUES
    ('admin', '1002000', 'admin@test.org'),
    ("Maria Silver", "949.282.111-82", "mariam@test.org"),
    ("Jairo Carlile", "144.217.577-11", "carlile@test.org"),
    ("Marcos Oliva", "433.144.644-52", "marcos@test.org");