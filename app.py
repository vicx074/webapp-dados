import streamlit as st
import pandas as pd
import numpy as np

st.title('Football Data App')

# Sidebar
st.sidebar.header('Leagues')
selected_league = st.sidebar.selectbox(
    'League',
    ['England', 'Spain', 'Germany', 'France']
)

st.sidebar.header('Season')
selected_season = st.sidebar.selectbox(
    'Season', ['2024/2025', '2023/2024', '2022/2023']
)

# Função para carregar os dados
def load_data(league, season): 
    # Mapear nomes para códigos de liga
    league_codes = {
        'England': 'E0',
        'Spain': 'SP1',
        'Germany': 'D1',
        'France': 'F1'
    }
    
    # Mapear temporadas para códigos de temporada
    season_codes = {
        '2024/2025': '2425',
        '2023/2024': '2324',
        '2022/2023': '2223'
    }
    
    league_code = league_codes.get(league)
    season_code = season_codes.get(season)

    url = f"https://www.football-data.co.uk/mmz4281/{season_code}/{league_code}.csv"
    st.write("CSV:", url)  # Para debug

    data = pd.read_csv(url)
    return data

df = load_data(selected_league, selected_season)

st.subheader('Dataframe: ' + selected_league)
st.dataframe(df)
