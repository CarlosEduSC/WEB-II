
# Framework ORM SQLAlchemy
## 1. Implementar Caso de uso manter Fornecedor
## 2. Implementar Caso de uso manter Produto 
> manter == CRUD (create, read, update, delete)
## 3. Associação 1-N entre Fornecedor e Produto.

Obs: fazer funcionar primeiro na routes.py
     estando ok, fazer os formulários (manter produto e fornecedor)
     

# ORM - Object Relational Mapper

SQLAlchemy - é a biblioteca ORM que 
realiza o mapeamento entre as Classes e tabelas.

## Install SqlAlchemy
```python
pip install SQLAlchemy
pip install -U Flask-SQLAlchemy
```

### Configurar o __init__.py
### Criar classe models
### Adicionar rotas

Delete
```python
db.session.delete(f1)
db.session.commit()
```

## Filter by
```python
# get by primary key
User.query.get(1)
mary = User.query.filter_by(username='mary').first()
User.query.filter(User.email.endswith('@example.com')).all()
rfiles = RFile.query.filter_by(repo_id=repo.id).order_by(RFile.st_commits.desc())
```

---

# Finalizar CRUD cliente
- [x] findall
- [ ] Save
- [ ] Update/editar
- [ ] findby nome

## Arquitetura MVC
- Model - entities.py (Cliente), Dao
- View - html + jinja
- Controller - routes.py

# Flask + SQLite
- database.py: abre uma conexão com o banco de dados
- dao.py: Interface CRUD para entidade Cliente
- schemas.sql: define a estrutura do banco de dados,
ou seja, as tabelas e as relações.

## Atividade CRUD Produto
Criar no script tabela
- id:  PK auto increment
- nome: text
- desc: text
- preco: FLOAT
- quantidade: INT

Implementar DaoProduto

Entity Produto

Criar a Route para listar todos produtos
/produto/findall

Redefinir cliente para:
/cliente/findall
