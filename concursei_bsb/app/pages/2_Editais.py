# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 19:12:31 2025

@author: Marqu
"""

import streamlit as st

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
