import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

def load_data():
    """Carrega e trata os dados do CSV."""
    df = pd.read_csv("../data/contests_info.csv", sep=';')
    df.dropna(inplace=True)
    df['Início'] = pd.to_datetime(df['Início'], errors='coerce')
    df = df.dropna(subset=['Início'])
    return df

def plot_pie_chart(df):
    """Gráfico de pizza mostrando a proporção de concursos abertos/previstos."""
    status_counts = df['Status'].value_counts()
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', colors=['#1e7a34', '#dcdcdc'])
    ax.set_title("Proporção de Concursos Abertos/Previstos")
    st.pyplot(fig)

def plot_bar_vagas_estado(df):
    """Gráfico de barras: quantidade de vagas por estado."""
    df['Vagas'] = pd.to_numeric(df['Vagas'], errors='coerce').fillna(0)
    vagas_estado = df.groupby('Região')['Vagas'].sum().sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x=vagas_estado.index, y=vagas_estado.values, ax=ax, palette=['#1e7a34'])
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    ax.set_title("Quantidade de Vagas por Estado")
    st.pyplot(fig)

def plot_bar_vagas_orgao(df):
    """Gráfico de barras mostrando quais órgãos têm mais vagas."""
    vagas_orgao = df.groupby('Nome')['Vagas'].sum().nlargest(10)
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(y=vagas_orgao.index, x=vagas_orgao.values, ax=ax, palette=['#1e7a34'])
    ax.set_title("Órgãos com Mais Vagas")
    st.pyplot(fig)

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
plot_bar_vagas_orgao(df)
plot_hist_aberturas(df)

render_footer()
