import streamlit as st
import pandas as pd
import numpy as np


st.title('Football Data App')

# Montagem do Sidebar
st.sidebar.header('Leagues')
selected_league = st.sidebar.selectbox(
    'League',
    ['England', 'Spain', 'Germany', 'France']
)

st.sidebar.header('Season')
selected_season = st.sidebar.selectbox(
    'Season', ['2025/2024', '2024/2023', '2023/2022']
)


# Web Scraping Football Data

# Função para carregar os dados
def load_data(league, season): 

# Condicionais para definir a liga com base na seleção do usuário
    if selected_league == 'England': 
        league = 'E0'
    elif selected_league == 'Spain': 
        league = 'SP1'
    elif selected_league == 'Germany': 
        league = 'D1'
    elif selected_league == 'France': 
        league = 'F1'

# Condicionais para definir a temporada com base na seleção do usuário
    if selected_league == '2024/2025':
        season = '2425' 
    elif selected_league == '2023/2024':
        season = '2324'
    elif selected_league == '2022/2023':
        season = '2223'    

    url = f"https://www.football-data.co.uk/mmz4281/{season}/{league}.csv" 
    data = pd.read_csv(url)
    return data



df = load_data(selected_league, selected_season)

st.subheader('Dataframe: '+selected_league)
st.dataframe(df)