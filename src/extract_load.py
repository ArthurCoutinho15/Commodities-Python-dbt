import yfinance as yf
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

def connect_mysql(host, user, password, database):
    try:
        connection_url = f'mysql+pymysql://{user}:{password}@{host}/{database}'
        engine = create_engine(connection_url)
        print("Successfully connected to MySQL")
        return engine
    except Exception as err:
        print(f"Error: {err}")
        return None


def buscar_dados_commodities(simbolo, periodo='5d', intervalo='1d'):
    ticker = yf.Ticker(simbolo)
    dados = ticker.history(period=periodo, interval=intervalo)[['Close']]
    if dados.empty:
        print(f"{simbolo}: No data found, symbol may be delisted")
    else:
        dados['simbolo'] = simbolo
    return dados

def buscar_todos_dados_commodities(commodities):
    todos_dados = []
    for simbolo in commodities:
        dados = buscar_dados_commodities(simbolo)
        if not dados.empty:
            todos_dados.append(dados)
    return pd.concat(todos_dados)

def salvar_no_mysql(df, engine, table_name='commodities'):
    df.to_sql(name=table_name, con=engine, if_exists='replace', index=True, index_label='Date')
    print(f"Dados salvos na tabela '{table_name}' no MySQL")

if __name__ == '__main__':
    HOST_NAME = os.getenv('HOST')
    USER = os.getenv('USER')
    PASSWORD = os.getenv('PASSWORD')
    DATABASE = os.getenv('DB_NAME_PROD')

    if None in [HOST_NAME, USER, PASSWORD, DATABASE]:
        print("Erro: Variável de ambiente não definida corretamente.")
    else:
        engine = connect_mysql(HOST_NAME, USER, PASSWORD, DATABASE)
        if engine:
            commodities = ['CL=F', 'SI=F']  
            dados_concatenados = buscar_todos_dados_commodities(commodities)
            if not dados_concatenados.empty:
                salvar_no_mysql(dados_concatenados, engine)
            else:
                print("Nenhum dado foi encontrado para as commodities fornecidas.")
