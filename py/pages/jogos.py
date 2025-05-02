import streamlit as st
import pandas as pd
import numpy as np
import datetime
from datetime import date

st.title("Jogos do dia")

dia = st.date_input(
    "Data de análise",
    date.today()
)

def load_data_jogos():
    url = f"https://github.com/futpythontrader/YouTube/blob/main/Jogos_do_Dia/FootyStats/Jogos_do_Dia_FootyStats_{dia}.csv?raw=true"
    data_jogos = pd.read_csv(url)
    return data_jogos

df_jogos = load_data_jogos()

st.dataframe(df_jogos)