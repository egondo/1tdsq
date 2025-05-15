import streamlit as st 
import pandas as pd

st.set_page_config(page_title="Exemplo Form", page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)

df = pd.read_csv("filmes.csv", sep=';')
#st.write(df)
atores = df['ator'].unique()
ator_selected = st.selectbox("Ator", atores)

df_filtrado = df.query(f'ator == "{ator_selected}"')


st.write(df_filtrado)


