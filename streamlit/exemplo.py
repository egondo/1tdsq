import streamlit as st 

st.set_page_config(page_title="Exemplo Form", page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)

col1, col2 = st.columns(2)
with col1:
    nome = st.text_input("Informe o seu nome: ")
    idade = st.number_input ("Digite sua idade: ", min_value=0, max_value=150, value =25)
    genero = st.selectbox("Gênero", ["masculino", "feminino", "NDA"])

    disciplina = st.radio("Qual a disciplina mais legal?", ["CTP", "DDD", "IA"], 
                captions=["Computational Thinking", "Domain Driven Design", "Chatbox and AI"])



with col2:
    st.write(nome + " " + str(idade) + " " + genero + " " + disciplina)