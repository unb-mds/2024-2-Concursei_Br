import pandas as pd
import altair as alt
import streamlit as st
import requests
from io import StringIO
from Home import load_data

try:
    st.set_page_config(page_title="Exportar", page_icon="assets/logo_concursei.png", layout="wide")
except:
    pass


def render_header():
    """Renderiza o cabeçalho da página."""
    st.markdown(
        """
        <style>
            .header-container {
                padding: 0px !important;
                margin: 0px !important;
            }
            .block-container {
                padding-top: 45px !important;
                padding: 0px;
            }
            .header {
                background-color: #ffffff;
                padding: 20px 50px;
                border-bottom: 3px solid #1e7a34;
                display: flex;
                justify-content: space-between;
                align-items: center;
                position: sticky;
                z-index: 1000;
                margin-top: 0px;
            }
            .header .logo {
                font-size: 24px;
                font-weight: bold;
                color: #32a852;
                text-decoration: none;
            }
            .header .nav a {
                text-decoration: none;
                color: white;
                font-weight: bold;
                margin-left: 20px;
                background-color: green;
                padding: 10px 25px;
                border-radius: 0px;
            }
        </style>
        <div class="header">
            <a href="home" class="logo">Concursei Br</a>
            <div class="nav">
                <a href="Home">Home</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

def render_footer():
    """Renderiza o rodapé da página."""
    st.markdown(
        """
        <style>
            .footer { 
                border-top: 3px solid #1e7a34;
                background-color: rgb(255, 255, 255);
                padding: 20px;
                text-align: center;
                font-size: 14px;
                color: rgb(0, 0, 0);
            }
        </style>
        <div class="footer">
            © 2025 Concursei Br. Todos os direitos reservados.
        </div>
        """,
        unsafe_allow_html=True
    )

# Streamlit app

# Header estilizado
render_header()

# Criando um layout com espaçamento lateral (igual ao Dashboard)
espaco_esquerda, conteudo_principal, espaco_direita = st.columns([0.03, 0.94, 0.03])  # 3% - 94% - 3%

with conteudo_principal:
    # Conteúdo principal
    st.title("Exportar dados")
    st.write("Nesta página você poderá exportar os dados personalizados.")

    df = load_data()

    df["Vagas"] = df["Vagas"].astype(str).str.replace(".", "", regex=False)  # Remove separadores de milhares
    df["Vagas"] = df["Vagas"].replace("Várias", "0")  # Substitui "Várias" por "0"
    df["Vagas"] = pd.to_numeric(df["Vagas"], errors="coerce").fillna(0).astype(int)
    df_ordenado = df.dropna(subset=["Vagas"]).sort_values(by="Vagas",ascending=False)


    def filtros():
        col1, col2 = st.columns(2)

        # 1. Filtro de Região
        with col1:
            regioes = df_ordenado['Região'].unique()
            regiao_selecionada = st.multiselect(
                "Selecione a(s) Região(ões):", 
                options=regioes
            )

        # 2. Filtro de Status
        with col2:
            status_opcoes = df_ordenado['Status'].unique()   
            status_selecionado = st.multiselect(
                "Selecione o(s) Status:", 
                options=status_opcoes,
                default=["Aberto"]  # Definir "EM ABERTO" como padrão
            )

        # 3. Aplicar filtros simultâneos
        df_filtrado = df_ordenado.copy()

        if regiao_selecionada:
            df_filtrado = df_filtrado[df_filtrado['Região'].isin(regiao_selecionada)]

        if status_selecionado:
            df_filtrado = df_filtrado[df_filtrado['Status'].isin(status_selecionado)]

        
        
        return df_filtrado

    def criar_visualizacoes(df_filtrado):
        """
        Recebe o df_filtrado e exibe "cards" resumindo:
        - Número total de concursos filtrados
        - Soma da coluna 'Vagas'
        Além disso, exibe a tabela e permite exportá-la para CSV.
        """
        if df_filtrado.empty:
            st.info("Não há dados para exibir nos gráficos com os filtros selecionados.")
            return

        total_vagas = df_filtrado['Vagas'].sum()

        col1, col2 = st.columns(2)

        with col1:
            st.metric(label="Concursos Filtrados", value=len(df_filtrado))
        with col2:
            st.metric(label="Total de Vagas", value=int(total_vagas))
        
        # Exibe a tabela
        st.table(df_filtrado)
        
        # Converte o dataframe para CSV (opcionalmente, você pode ajustar o separador e a codificação)
        csv = df_filtrado.to_csv(index=False, encoding="utf-8")
        
        # Botão de download para exportar a tabela em CSV
        st.download_button(
            label="Exportar tabela em CSV",
            data=csv,
            file_name="concursos_filtrados.csv",
            mime="text/csv"
        )


    df_filtrado = filtros()

    criar_visualizacoes(df_filtrado)
render_footer()