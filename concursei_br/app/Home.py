import streamlit as st
import pandas as pd
import requests
from io import StringIO

# Configuração da página
st.set_page_config(
    page_title="Concursei Br",
    layout="wide",
    page_icon="assets/logo_concursei.png"
)

# Função para carregar dados do CSV
@st.cache_data
def load_data():
    """Carrega e processa os dados do CSV."""
    file_url = 'https://raw.githubusercontent.com/unb-mds/2024-2-Concursei_Br/front/concursei_br/data/contests_info.csv'

    try:
        response = requests.get(file_url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        st.error(f"Erro ao acessar o arquivo: {e}")
        return pd.DataFrame()

    df = pd.read_csv(StringIO(response.text), sep=';')
    df["Vagas"] = pd.to_numeric(df["Vagas"], errors="coerce").fillna(0).astype(int)
    return df

# Função para aplicar estilos CSS personalizados
def get_custom_css():
    return """
    <style>
        /* Estilos gerais */
        body {
            font-family: Arial, sans-serif;
            background-color: #f9f9f9;
            margin: 0;
            padding: 0;
        }
        
        .block-container{
            padding: 0;
        }

        /* Cabeçalho */
        .header {
            background-color: #ffffff;
            padding: 20px 50px;
            border-bottom: 3px solid #1e7a34;
            display: flex;
            justify-content: space-between;
            align-items: center;
            position: sticky;
            z-index: 1000;
            margin-top: 45px;
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
        /* Seção principal */
        .main-section {
            background-color: #dcdcdc;
            text-align: left;
            padding: 50px 7%;
            border-radius: 0px;
        }
        .main-section h1 {
            font-size: 36px;
            color: #333333;
        }
        .main-section p {
            font-size: 18px;
            color: #666666;
            margin: 20px 0;
        }
        .main-section .btn {
            display: inline-block;
            background-color: #32a852;
            color: white;
            padding: 10px 20px;
            border-radius: 0px;
            text-decoration: none;
            font-size: 16px;
            margin-top: 10px;
        }
        /* Estatísticas */
        .statistics {
            background-color: #dcdcdc;
            padding: 20px;
            text-align: center;
            border-radius: 0px;
        }
        .statistics-box {
            background: #ffffff;
            border-radius: 0px;
            padding: 35px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            border: 2px solid #1e7a34;
        }
        .stat-number {
            color: #32a852;
            font-size: 48px;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .stat-label {
            color: #666666;
            font-size: 18px;
            line-height: 1.4;
        }
        /* Rodapé */
        .footer {
            border-top: 3px solid green;
            background-color: #ffffff;
            padding: 20px;
            text-align: center;
            font-size: 14px;
            color: #000000;
        }
    </style>
    """

# Função para renderizar o cabeçalho
def get_header():
    return """
    <div class="header">
        <a href="home" class="logo">Concursei Br</a>
        <div class="nav">
            <a href="Dashboards">Dashboards</a>
        </div>
    </div>
    """

# Função para renderizar a seção principal
def get_main_section():
    return """
    <div class="main-section">
        <h1>Acompanhe as<br>publicações no<br><span style="color:green">Concursei Br</span></h1>
        <p>Promovendo a participação pública em concursos do Brasil: acompanhe de forma simples e clara as publicações de concursos.</p>
        <a href="Exportar" class="btn">Exportar Dados</a>
    </div>
    """

# Função para renderizar as estatísticas
def get_statistics(df):
    total_concursos = len(df)
    total_vagas = df['Vagas'].sum()

    return f"""
    <div class="statistics">
        <div class="statistics-box">
            <div>
                <div class="stat-label">Concursos com inscrições abertas HOJE</div>
                <div class="stat-number">{total_concursos}</div>
            </div>
            <div>
                <div class="stat-label">Total de vagas HOJE</div>
                <div class="stat-number">{total_vagas}</div>
            </div>
        </div>
    </div>
    """

# Função para renderizar o rodapé
def get_footer():
    return """
    <div class="footer">
        © 2025 Concursei Br. Todos os direitos reservados.
    </div>
    """

# Função principal
def main():
    """Função principal para rodar o Streamlit."""
    df = load_data()
    
    if df.empty:
        st.warning("Nenhum dado carregado. Verifique a origem dos dados.")
        return

    df = df[df['Status'] == 'Aberto']

    # Aplicando o CSS
    st.markdown(get_custom_css(), unsafe_allow_html=True)
    
    # Renderizando elementos visuais
    st.markdown(get_header(), unsafe_allow_html=True)
    st.markdown(get_main_section(), unsafe_allow_html=True)
    st.markdown(get_statistics(df), unsafe_allow_html=True)
    st.markdown(get_footer(), unsafe_allow_html=True)

# Executa o app
if __name__ == "__main__":
    main()