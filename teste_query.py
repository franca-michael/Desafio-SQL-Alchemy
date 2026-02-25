from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, func 
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



# QUERY

resultado = session.query(
    Fornecedor.nome,
    func.sum(Produto.preco).label('soma_produto')
    ).join(Produto, Fornecedor.id == Produto.fornecedor_id
    ).group_by(Fornecedor.nome).all()
    
for nome, soma_produto in resultado:
    print(f"Fornecedor: {nome}, Soma dos Preços dos Produtos: {soma_produto}")


