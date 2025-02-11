import pandas as pd
import altair as alt
import streamlit as st
from utils.data_loader import load_contests_data

st.set_page_config(page_title="Dashboards", page_icon="../assets/logo_concursei.png", layout="wide")

def render_header():
    """Renderiza o cabeçalho da página."""
    st.markdown(
        """
        <style>
            .header { 
                background-color: rgb(255, 255, 255);
                padding: 20px 50px;
                border-bottom: 3px solid #1e7a34;
                display: flex;
                justify-content: space-between;
                align-items: center;
                position: sticky;
                top: 0;
                text-wrap: nowrap;
            }
            .header .logo {
                font-size: 24px;
                font-weight: bold;
                color: rgb(2, 2, 2);
            }
        </style>
        <div class="header">
            <div class="logo">  
                <a href="home">Concursei Br</a> 
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

# Header estilizado
render_header()

# Conteúdo principal
st.title("Exportar dados")
st.write("Nesta página você poderá exportar os dados personalizados.")

df = pd.read_csv("../data/contests_info.csv", sep=';')

# Tratamento da coluna "Vagas"
df["Vagas"] = df["Vagas"].astype(str).str.replace(".", "", regex=False)  # Remove separadores de milhares
df["Vagas"] = pd.to_numeric(df["Vagas"], errors="coerce")  # Converte números e transforma "Várias" em NaN

# Criar um DataFrame separado para "Várias"
df_varias = df[df["Vagas"].isna()]  # Filtra apenas os concursos com "Várias"

# Substituir NaN por 0 APENAS para cálculos (não modificar os dados)
df["Vagas_Num"] = df["Vagas"].fillna(0).astype(int)  # Criamos uma nova coluna apenas para cálculos

# Ordenar apenas os concursos numéricos
df_ordenado = df.dropna(subset=["Vagas"]).sort_values(by="Vagas")

# Concatenar os concursos numéricos com os de "Várias" no final
df_final = pd.concat([df_ordenado, df_varias], ignore_index=True)

def filtros():
    col1, col2 = st.columns(2)

    # 1. Filtro de Região
    with col1:
        regioes = df_final['Região'].unique()
        regiao_selecionada = st.multiselect(
            "Selecione a(s) Região(ões):", 
            options=regioes
        )

    # 2. Filtro de Status
    with col2:
        status_opcoes = df_final['Status'].unique()   
        status_selecionado = st.multiselect(
            "Selecione o(s) Status:", 
            options=status_opcoes
        )

    # 3. Aplicar filtros simultâneos
    df_filtrado = df_final.copy()

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
        st.metric(label="Total de Vagas", value=int(total_vagas/10))

df_filtrado = filtros()

criar_visualizacoes(df_filtrado)
render_footer()