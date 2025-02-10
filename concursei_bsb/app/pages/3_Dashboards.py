import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import plotly.express as px
import plotly.graph_objects as go

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
                <a href="#">Concursei Br</a> 
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

@st.cache_data
def load_data():
    # Carrega e trata os dados do CSV.
    df = pd.read_csv("../data/contests_info.csv", sep=';')

    # Remover espaços extras e valores inconsistentes na coluna STATUS
    df['Status'] = df['Status'].astype(str).str.strip()

    # Tratamento da coluna início
    df["Início"] = df["Início"].astype(str).str.strip()  # Remove espaços extras
    df["Início"] = df["Início"].replace("Previsto", None)  # Substitui "Previsto" por None manualmente
    df["Início"] = pd.to_datetime(df["Início"], errors="coerce") # Converte para datetime (os erros viram NaN)

    df["Vagas"] = pd.to_numeric(df["Vagas"], errors="coerce").fillna(0).astype(int)

    # Tratamendo coluna VAGAS e REGIÃO
    # Converter a coluna "Vagas" para numérico (ignorar valores inválidos)
    #df["Vagas"] = pd.to_numeric(df["Vagas"], errors="coerce")
    # Remover linhas onde "Região" ou "Vagas" são NaN
    #df = df.dropna(subset=["Região", "Vagas"])
    
    return df

def plot_pie_chart(df):
    # Gráfico de pizza mostrando a proporção de concursos abertos/previstos.
    status_counts = df['Status'].value_counts()

    # Verifica se há ambos os valores antes de gerar o gráfico
    if "Aberto" not in status_counts:
        status_counts["Aberto"] = 0
    if "Previsto" not in status_counts:
        status_counts["Previsto"] = 0

    fig = px.pie(
        names=status_counts.index, 
        values=status_counts.values, 
        title="Proporção de Concursos Abertos/Previstos",
        color=status_counts.index,
        color_discrete_map={"Aberto": "#1e7a34", "Previsto": "#dcdcdc"},  # Cores específicas
    )

    # Exibir valores absolutos no gráfico
    fig.update_traces(
        textinfo="label+percent",
        hovertemplate="<b>%{label}</b><br>Quantidade: %{value}"
    )

    # Renderizar no Streamlit
    st.plotly_chart(fig, use_container_width=True)


def plot_bar_vagas_estado(df):
    # Gráfico de barras: quantidade de vagas por estado.
    # Agrupar por Estado (Região) e somar as vagas
    vagas_por_estado = df.groupby("Região")["Vagas"].sum().reset_index()

    # Ordenar por número de vagas
    vagas_por_estado = vagas_por_estado.sort_values(by="Vagas", ascending=False)

    # Criar o gráfico de barras interativo
    fig = px.bar(
        vagas_por_estado,
        x="Região",
        y="Vagas",
        title="Quantidade de Vagas por Estado",
        text="Vagas",  # Exibir os valores sobre as barras
        color="Região",  # Cores diferenciadas por estado
        color_discrete_sequence=px.colors.sequential.Greens,  # Paleta de cores
    )

    # Ajustar a exibição dos rótulos
    fig.update_traces(texttemplate="%{text:.0f}", textposition="outside")
    fig.update_layout(
        xaxis_title="Estado",
        yaxis_title="Quantidade de Vagas",
        xaxis_tickangle=-45
    )

    # Exibir no Streamlit
    st.plotly_chart(fig, use_container_width=True)

def plot_bar_vagas_orgao(df, top_n):
    # Gráfico de barras mostrando quais órgãos têm mais vagas.
    # Agrupar por órgão e somar as vagas
    vagas_por_orgao = df.groupby("Nome")["Vagas"].sum().reset_index()

    # Ordenar por número de vagas (maior para menor)
    vagas_por_orgao = vagas_por_orgao.sort_values(by="Vagas", ascending=False)

    # Filtrar os Top N órgãos com mais vagas
    vagas_por_orgao = vagas_por_orgao.head(top_n)

    # Criar o gráfico interativo
    fig = px.bar(
        vagas_por_orgao,
        y="Nome",
        x="Vagas",
        title=f"Top {top_n} Órgãos com Mais Vagas",
        text="Vagas",  # Exibir os valores nas barras
        orientation="h",  # Barras horizontais para facilitar a leitura
        color="Nome",  # Cores diferentes por órgão
        color_discrete_sequence=px.colors.sequential.Greens  # Paleta de cores
    )

    # 🔹 Ajustes visuais
    fig.update_traces(
        texttemplate="%{text:.0f}",  # Exibir apenas inteiros
        textposition="outside",
        hovertemplate="<b>%{y}</b><br>Vagas: %{x:,d}"  # Formatar hover com separador de milhar
    )

    fig.update_layout(
        xaxis_title="Quantidade de Vagas",
        yaxis_title="Órgão",
        yaxis=dict(automargin=True),  # Ajusta a margem automaticamente
        height=600  # Define a altura do gráfico para facilitar a rolagem
    )

    # Exibir no Streamlit
    st.plotly_chart(fig, use_container_width=True)

def plot_hist_aberturas(df):
    """Gráfico histograma mostrando a quantidade de aberturas por mês."""
    df['Mês'] = df['Início'].dt.to_period('M')
    aberturas_por_mes = df['Mês'].value_counts().sort_index()
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x=aberturas_por_mes.index.astype(str), y=aberturas_por_mes.values, ax=ax, palette=['#1e7a34'])
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    ax.set_title("Quantidade de Aberturas por Mês")
    st.pyplot(fig)

# Streamlit App
render_header()
st.title("Dashboard de Concursos")

df = load_data()
plot_pie_chart(df)
plot_bar_vagas_estado(df)

# Seletor para número de órgãos a exibir
top_n = st.slider("Quantidade de órgãos a exibir:", min_value=5, max_value=50, value=10, step=5)
plot_bar_vagas_orgao(df, top_n)
plot_hist_aberturas(df)

render_footer()
