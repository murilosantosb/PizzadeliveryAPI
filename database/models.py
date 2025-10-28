from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base

"""
    1- criar a conexão do seu banco
    2- Como usamos sqlite, passamos somente a onde ficará
    armazenado nosso db na nossa maquina
    3- Quando você for fazer um deploy da API, pode alocar esse banco 
    de dados na AWS, Azure, Neon ...
"""
db = create_engine("sqlite:///database/banco.db")

# cria a base do banco de dados
Base = declarative_base()

# criar as classes/tabelas do banco
#  Tabela dos usuários
class Usuario(Base):
    __tablename__ = "usuarios" # Nome da tabela
    
    # Parametros que teram no nosso banco
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String, nullable=False)
    email = Column("email", String, nullable=False)
    senha = Column("senha", String, nullable=False)
    ativo = Column("ativo", Boolean)
    admin = Column("admin", Boolean, default=False)
    
    # O que vamos enviar para API cadastrar o user no banco
    def __init__(self, nome, email, senha, ativo=True, admin=False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin

# Tabela dos pedidos
class Pedido(Base):
    __tablename__ = "pedidos"
    
    # STATUS_PEDIDOS = (
    #     ("PENDENTE", "PENDENTE"),
    #     ("CANCELADO", "CANCELADO"),
    #     ("FINALIZADO", "FINALIZADO")
    # )
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    status = Column("status", String, default="PENDENTE")
    usuario_id = Column("usuario_id", Integer, ForeignKey("usuarios.id"), nullable=False)
    preco = Column("preco", Float, nullable=False)
    # itens =
    
    def __init__(self, usuario_id, preco=0, status="PENDENTE"):
        self.usuario_id = usuario_id
        self.preco = preco
        self.status = status


class ItemPedido(Base):
    __tablename__ = "itens_pedido"
    
    # TAMANHO_PEDIDO = (
    #     ("PEQUENO", "PEQUENO"),
    #     ("MEDIO", "MEDIO"),
    #     ("GRANDE", "GRANDE")
    # )
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    quantidade = Column("quantidade", Integer, nullable=False)
    sabor = Column("sabor", String, nullable=False)
    tamanho = Column("tamanho", String, nullable=False)
    preco_unitario = Column("preco_unitario", Float, nullable=False)
    pedido = Column("id_pedido", Integer, ForeignKey("pedidos.id"))
    
    def __init__(self, quantidade, sabor, tamanho, preco_unitario, pedido):
        self.quantidade = quantidade
        self.sabor = sabor
        self.tamanho = tamanho
        self.preco_unitario = preco_unitario
        self.pedido = pedido 
    
# executa a criação dos metadados do seu banco (cria efetivamente o banco de dados)
