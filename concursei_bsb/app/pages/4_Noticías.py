# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 19:12:51 2025

@author: Marqu
"""

import streamlit as st

st.set_page_config(page_title="Notícias", page_icon="📰", layout="wide")

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
st.title("Notícias de Concursos")
st.write("### Atualizações importantes sobre concursos públicos")
st.write("Aqui você encontrará notícias recentes e anúncios sobre concursos em todo o Brasil.")
