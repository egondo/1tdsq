import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("data.csv", sep=";")

st.set_page_config(page_title="CAGED", layout="wide")
df['saldomovimentacao'] = df['saldomovimentacao'].replace({-1 : 'desligado', 1: 'admitido'}, regex=True)

df['sexo'] = df['sexo'].replace({1: 'masculino', 3: 'feminino'})

df['competenciamov'] = df['competenciamov'].replace({202501: '01/25', 202502: '02/25', 202503: '03/25'})


outro_df = df[['competenciamov', 'saldomovimentacao', 'sexo', 'idade', 'salario']]

col1, col2 = st.columns(2)
with col1:
    aux_sexo = st.selectbox("Sexo", ['todos', 'masculino', 'feminino'])
    if aux_sexo != 'todos':
        outro_df = outro_df.query(f"sexo == '{aux_sexo}'")
    st.write(outro_df)

with col2:
    tabela = pd.pivot_table(outro_df, values='sexo', index=['competenciamov'],
                       columns=['saldomovimentacao'], aggfunc="count")
    tabela['saldo'] = tabela['admitido'] - tabela['desligado']
    st.write(tabela)

    #plt.bar(tabela.index, tabela['admitido'])
    #st.pyplot(plt)
    
    tabela.plot(y=['admitido', 'desligado', 'saldo'], kind='bar', title='Trabalhadores')
    st.pyplot(plt)