import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

st.title("Dashboard użytkowników z Azure SQL")

# Parametry połączenia (w praktyce trzymaj je w zmiennych środowiskowych)
server = 'oleksiidb.database.windows.net'
database = 'alexdb'                             
username = 'alex'                           
password = 'qwertyQWERTY228'   

conn_str = f"mssql+pymssql://{username}:{password}@{server}/{database}"
engine = create_engine(conn_str)

df = pd.read_sql("SELECT * FROM uzytkownicy", con=engine)

st.write("Tabela danych:")
st.dataframe(df)

st.write("Wykres rozrzutu:")
st.scatter_chart(df, x='wiek', y='zarobki', color='ocena')
