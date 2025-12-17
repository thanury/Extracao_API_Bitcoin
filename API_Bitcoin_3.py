import requests
from sqlalchemy import create_engine, Column, String, Float, Integer, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime
from time import sleep
from dotenv import load_dotenv
import os

load_dotenv()

# Configurações do banco de dados
DATABASE_URL = os.getenv("DATABASE_KEY")

# Criação do engine e sessão
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()

# Definição do modelo de dados
class BitcoinDados(Base):
    __tablename__ = "bitcoin_dados"

    id = Column(Integer, primary_key=True)
    valor = Column(Float)
    criptomoeda = Column(String(10))
    moeda = Column(String(10))
    timestamp = Column(DateTime)

# Criar a tabela (se não existir)
Base.metadata.create_all(engine)

def extrair_dados_bitcoin():
    url = "https://api.coinbase.com/v2/prices/spot"
    resposta = requests.get(url) 
    return resposta.json()

def tratar_dados_bitcoin(dados_json):
    valor = float(dados_json['data']['amount'])
    criptomoeda = dados_json['data']['base']
    moeda = dados_json['data']['currency']
    dados_tratados=BitcoinDados (
        valor=valor,
        criptomoeda=criptomoeda,
        moeda=moeda,
        timestamp=datetime.now()
    )
    return dados_tratados  

def salvar_dados_sqlalchemy(dados):
    with Session() as session:
        session.add(dados)
        session.commit()
        print('Dados salvos no PostgreSQL!')

if __name__ == "__main__":
    while True:
        dados_json = extrair_dados_bitcoin()
        dados_tratados = tratar_dados_bitcoin(dados_json)
        
        print("Dados Tratados:")
        print(dados_tratados.__dict__)

        salvar_dados_sqlalchemy(dados_tratados)

        print("Aguardando 15 segundos")
        sleep(15)