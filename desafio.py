from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.exc import SQLAlchemyError


Base = declarative_base()

#Declarando tabelas
class Fornecedor(Base):
    __tablename__ = 'fornecedores'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    telefone = Column(String(20))
    email = Column(String(50))
    endereco = Column(String(100))

class Produto(Base):
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    descricao = Column(String(200))
    preco = Column(Integer)
    fornecedor_id = Column(Integer, ForeignKey('fornecedores.id')) #coluna de relacionamento com a tabela de fornecedores
    
    # Estabelece relacionamento
    fornecedor = relationship("Fornecedor")
    

#Criando tabelas
engine =  create_engine('sqlite:///desafio.db', echo=True)
Base.metadata.create_all(engine)


#Abrindo as Sessões
Session = sessionmaker(bind=engine)
session = Session()

# Inserindo registros na tabela de Fornecedores

try:
    with Session() as session: #usando a sessão corretamente com o gerenciador de contexto
        fornecedores = [
            Fornecedor(nome='Fornecedor A', telefone='123-456-789', email='contato@fmail.com', endereco='Rua A, 123'),
            Fornecedor(nome='Fornecedor B', telefone='987-654-321', email='contato@fmail.com', endereco='Rua B, 456'),
            Fornecedor(nome='Fornecedor C', telefone='543-210-987', email='contato@fmail.com', endereco='Rua C, 458'),
            Fornecedor(nome='Fornecedor D', telefone='987-654-321', email='contato@fmail.com', endereco='Rua D, 732'),
            Fornecedor(nome='Fornecedor E', telefone='541-431-312', email='contato@fmail.com', endereco='Rua E, 891')                         
        ]
        session.add_all(fornecedores)
        session.commit()

except SQLAlchemyError as e: # Capturando exceções do SQLAlchemy
    session.rollback()
    

# Inserindo registros na tabela de Produtos
try:
    with Session() as session:
        produtos = [
            Produto(nome="Teclado Mecânico RGB", descricao="Teclado switch blue com iluminação customizável", preco=250, fornecedor_id=1),
            Produto(nome="Mouse Gamer 12000 DPI", descricao="Mouse ergonômico com 6 botões programáveis", preco=180, fornecedor_id=2),
            Produto(nome="Monitor 24' Full HD", descricao="Monitor 144Hz com painel IPS e tempo de resposta 1ms", preco=1200, fornecedor_id=1),
            Produto(nome="Headset Surround 7.1", descricao="Fone de ouvido com cancelamento de ruído e microfone", preco=350, fornecedor_id=3),
            Produto(nome="Webcam 1080p Ultra", descricao="Câmera Full HD com ajuste automático de foco", preco=220, fornecedor_id=2)
        ]
        session.add_all(produtos)
        session.commit()
        
except SQLAlchemyError as e: # Capturando exceções do SQLAlchemy
    session.rollback()




