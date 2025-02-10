import pandas as pd
import altair as alt
import streamlit as st
from utils.data_loader import load_contests_data

st.set_page_config(page_title="Dashboards", page_icon="../assets/logo_concursei.png", layout="wide")

# Header estilizado
st.markdown(
    """
    <div class="header">
        <div class="logo">Concursei BR</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Conteúdo principal
st.title("Exportar dados")
st.write("Nesta página você poderá exportar os dados personalizados.")

df = pd.read_csv("../data/contests_info.csv", sep=';')

def filtros():
    col1, col2 = st.columns(2)

    # 1. Filtro de Região
    with col1:
        regioes = df['Região'].unique()
        regiao_selecionada = st.multiselect(
            "Selecione a(s) Região(ões):", 
            options=regioes
        )

    # 2. Filtro de Status
    with col2:
        status_opcoes = df['Status'].unique()   
        status_selecionado = st.multiselect(
            "Selecione o(s) Status:", 
            options=status_opcoes
        )

    # 3. Aplicar filtros simultâneos
    df_filtrado = df.copy()

    if regiao_selecionada:
        df_filtrado = df_filtrado[df_filtrado['Região'].isin(regiao_selecionada)]

    if status_selecionado:
        df_filtrado = df_filtrado[df_filtrado['Status'].isin(status_selecionado)]

    
    st.write(df_filtrado)
    return df_filtrado

def criar_visualizacoes(df_filtrado):
    """
    Recebe o df_filtrado e exibe "cards" resumindo:
    - Número total de concursos filtrados
    - Soma da coluna 'Vagas', interpretando '.' como separador de milhares
    """
    if df_filtrado.empty:
        st.info("Não há dados para exibir nos gráficos com os filtros selecionados.")
        return

    df_filtrado['Vagas_limpo'] = (df_filtrado['Vagas']
                                  .astype(str)
                                  .str.replace('.', '', regex=False))
    df_filtrado['Vagas_limpo'] = pd.to_numeric(df_filtrado['Vagas_limpo'], errors='coerce')

    
    df_filtrado['Vagas_limpo'] = df_filtrado['Vagas_limpo'].fillna(0)

    total_vagas = df_filtrado['Vagas_limpo'].sum()

    col1, col2 = st.columns(2)

    with col1:
        st.metric(label="Concursos Filtrados", value=len(df_filtrado))

    with col2:
        st.metric(label="Total de Vagas", value=int(total_vagas))

df_filtrado = filtros()
criar_visualizacoes(df_filtrado)