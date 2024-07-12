import yfinance as yf
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os
import streamlit as st

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

def get_data(engine):
    query = f""" SELECT * FROM commodities.dm_commodities; """
    df = pd.read_sql(query, engine)
    return df 

def page_config():
    st.set_page_config(page_title='Dashboard do diretor', layout='wide')

def titulo():
    st.title('Vendas')

def descricao():
    st.write("""
        Este dashboard mostra os dados de commodities e suas transações.
    """)

def dashboard(df):
    st.dataframe(df)


if __name__ == '__main__':
    
    HOST_NAME = os.getenv('HOST')
    USER = os.getenv('USER')
    PASSWORD = os.getenv('PASSWORD')
    DATABASE = os.getenv('DB_NAME_PROD')
    
    if None in [HOST_NAME, USER, PASSWORD, DATABASE]:
        print("Erro: Variável de ambiente não definida corretamente.")
    else:
        engine = connect_mysql(HOST_NAME, USER, PASSWORD, DATABASE)
    
    df = get_data(engine)
    page_config()
    titulo()
    descricao()
    dashboard(df)