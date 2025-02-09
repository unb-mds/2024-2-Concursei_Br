# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 19:12:31 2025

@author: Marqu
"""
import pandas as pd
import streamlit as st
from utils.data_loader import load_contests_data

st.set_page_config(page_title="Editais e Provas", page_icon="📄", layout="wide")

# Header estilizado
st.markdown(
    """
    <div class="header">
        <div class="logo">CONCURSOS BRASIL</div>
        <div class="nav">
            <a href="#inicio">Início</a>
            <a href="#calendario">Calendário</a>
            <a href="#editais" class="btn">Ver Editais →</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Conteúdo principal
st.title("Editais e Provas")
st.write("### Links para Editais e Provas Anteriores")
st.write("Nesta página você terá acesso direto aos editais e provas anteriores para download e consulta.")

df = pd.read_csv("../data/contests_info.csv", sep=';')

def filtro_uf():
    regioes = df['Região'].unique()
    regiao_selecionada = st.multiselect("Selecione a Região:", options=regioes)
    if regiao_selecionada:
        # Filtrar o DataFrame com base na seleção do usuário
        df_filtrado = df[df['Região'].isin(regiao_selecionada)]
        
        # Exibir o DataFrame filtrado
        st.write(df_filtrado)
    else:
        # Mensagem quando nenhuma região for selecionada
        st.write("Selecione uma ou mais regiões para visualizar os dados.")


filtro_uf()