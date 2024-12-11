import streamlit as st
import plotly.express as px
import pandas as pd

def configure_page():
    st.set_page_config(page_title="DATA GOV", layout="wide", initial_sidebar_state="collapsed")

def header():
    st.markdown(
        """
        <style>
        .navbar {
            background-color: #0FFEF9;
            padding: 10px;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            z-index: 10;
            text-align:center;
        }
        .navbar h1 {
            color: white;
            font-family: 'Arial', sans-serif;
            margin: 0;
            display: inline-block;
        }
        .navbar-icons {
            float: right;
            margin-top: -35px;
        }
        .navbar-icons img {
            width: 30px;
            margin-left: 10px;
            cursor: pointer;
        }
        /* Adiciona espaçamento extra ao conteúdo principal */
        .main-content {
            margin-top: 100px; /* Ajusta o espaço para evitar sobreposição */
        }
        .main-header {
            font-family: 'Arial', sans-serif;
            color: #0FFEF9;
            text-align: left;
            margin-top: 20px;
            font-size: 28px;
            font-weight: bold;
        }
        .sub-header {
            font-family: 'Arial', sans-serif;
            color: #0FFEF9;
            text-align: left;
            font-size: 18px;
            margin-bottom: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Barra de navegação
    st.markdown(
        """
        <style>
        .navbar {
            background-color: #0FFEF9;
            padding: 10px;
            position: fixed;
            top: 40px; /* Ajusta a posição vertical da barra de navegação */
            left: 40;
            width: 100%;
            z-index: 10;
        }
        .navbar h1 {
            color: black;
            font-family: 'Arial', sans-serif;
            margin: 0;
            display: inline-block;
        }
        .navbar-icons {
            float: right;
            margin-top: -35px;
        }
        .navbar-icons img {
            width: 30px;
            margin-left: 10px;
            cursor: pointer;
        }
        </style>
        <div class="navbar">
            <h1>DATA GOV</h1>
            <div class="navbar-icons">
                <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="GitHub">
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

def subheader():
    st.markdown("<div class='main-header'>Monitore Licitações do GOV", unsafe_allow_html=True)
    st.markdown("<div class='sub-header'>Dados Provenientes do Diário Oficial!", unsafe_allow_html=True)

def layout():
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        city = st.selectbox("Município", ["São Paulo", "Campinas", "Santos", "Ribeirão Preto", 
        "Sorocaba", "São José dos Campos", "Bauru", "Jundiaí", "Piracicaba", "São Vicente"], key="city", help="Selecione o município desejado")
    with col2:
        year = st.selectbox("Ano", ["Todos os anos", "2021", "2022", "2023"], key="year", help="Selecione o período desejado")
    with col3:
        data_type = st.selectbox("Tipo", ["Quantidade de Licitações", "Valor Total Gasto"], key="data_type", help="Escolha o tipo de dado")

    # Simular dados para gráfico
    data = {
        "Ano": [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
        "Quantidade de Licitações": [0, 0, 0, 0, 0, 0, 0, 5, 10, 20],
        "Valor Total Gasto": [0, 0, 0, 0, 0, 0, 0, 10000, 25000, 50000],
    }
    df = pd.DataFrame(data)

    # Filtrar os dados com base nas seleções
    if year != "Todos os anos":
        df = df[df["Ano"] == int(year)]

    # Criar gráfico com Plotly
    fig = px.bar(df, x="Ano", y=data_type, title=f"{data_type} no período", text=data_type, labels={"Ano": "Ano", data_type: "Quantidade"})
    fig.update_traces(marker_color="#0FFEF9", textposition="outside")

    # Mostrar gráfico
    st.plotly_chart(fig, use_container_width=True)


def main():
    configure_page()
    header()
    subheader()
    layout()    


if __name__ == "__main__":
    main()