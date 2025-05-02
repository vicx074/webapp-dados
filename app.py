import streamlit as st
import pandas as pd
import numpy as np


st.title('Football Data App')

st.sidebar.header('Leagues')
# Select para cada liga
selected_league = st.sidebar.selectbox(
    'League',
    ['England', 'Spain', 'Germany', 'France']
)

st.sidebar.header('Season')
selected_seaso = st.sidebar.selectbox(
    'Season', ['2025/2024', '2024/2023', '2023/2022']
)

# Web Scraping Football Data

def load_data(league, season):
    url = f"https://www.football-data.co.uk/mmz4281/{season}/{league}.csv" 
    data = pd.read_csv(url)
    return data



df = load_data(selected_league, selected_season)