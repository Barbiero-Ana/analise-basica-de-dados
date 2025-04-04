# arquivo: app.py

import streamlit as st

st.title("Testando o Streamlit 🚀")

nome = st.text_input("Digite seu nome:")

if st.button("Dizer Olá"):
    st.success(f"Olá, {nome}! Seja bem-vindo(a) ao Streamlit! 😄")
