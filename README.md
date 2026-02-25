# 🏗️ Analytics Engineering Challenge: Data Modeling with SQLAlchemy

Este repositório documenta o desafio técnico de modelagem e extração de dados utilizando **SQLAlchemy**. Como **Analytics Engineer**, o objetivo aqui é dominar a camada de origem dos dados para garantir integridade e qualidade desde o início do pipeline. 📊✨

## 🎯 Objetivo do Desafio
Para um Analytics Engineer, entender como os dados são estruturados no banco transacional (Application Side) é fundamental para construir modelos de dados (Fatos e Dimensões) eficientes no Data Warehouse. 

Este projeto foca em:
1. **Source Data Modeling**: Mapear tabelas de sistemas operacionais usando Python.
2. **Data Integrity**: Garantir tipos de dados corretos e restrições (Primary Keys, Unicidade) na fonte.
3. **Connectivity**: Estabelecer a fundação para processos de ingestão de dados (ELT/ETL).

## 🛠️ Stack Tecnológica
* **Python 3.x**: Linguagem principal para automação de dados.
* **SQLAlchemy (ORM)**: Engine de conexão e mapeamento de esquemas.
* **Paradigma ORM**: Abstração de queries SQL para manipulação programática de dados.

## 🗂️ Modelagem de Origem (Sources)
O desafio foca em duas entidades principais que servem de base para análises de negócio:

### 👤 Dimensão Usuário (`users`)
Base para análises de comportamento, retenção (Churn) e segmentação.
- Estrutura: `id` (PK), `nome`, `telefone`, `email`, `endereco`.

### 📦 Dimensão Produto (`products`)
Base para análises de performance de vendas, SKU e catálogo.
- Estrutura: `id` (PK), `nome`, `descricao`, `preco`, `fornecedor_id`.

## 💻 Exemplo de Definição de Esquema

```python
from sqlalchemy import Column, Integer, String, Float, Numeric
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    # Nota de Analytics: Usar Float para preços pode gerar inconsistências. 
    # Em produção, priorizamos Numeric para precisão decimal! 📉
    price = Column(Float, nullable=False) 
🚀 Relevância para Analytics Engineering
Na vida real, o trabalho de um Analytics Engineer começa onde o SQLAlchemy atua:

Entendimento do Negócio: Ao ler as classes ORM, entendemos as regras de negócio aplicadas no backend.

Data Quality: Definir nullable=False ou unique=True evita que dados "sujos" cheguem ao Data Warehouse.

Pipelines de Ingestão: O SQLAlchemy é a biblioteca base usada por ferramentas de orquestração (como Airflow ou Prefect) para extrair dados de bancos transacionais.

✨ Documentando a jornada de transformação de dados brutos em insights estratégicos.