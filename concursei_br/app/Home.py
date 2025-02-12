import streamlit as st
import pandas as pd
import os
import requests
from io import StringIO

def set_page_config():
    st.set_page_config(
        page_title="Concursei Br",
        layout="wide",
        page_icon="assets/logo_concursei.png"
    )

def load_data():
    """Carrega e processa os dados do CSV."""
    file_path = 'https://raw.githubusercontent.com/unb-mds/2024-2-Concursei_Br/front/concursei_br/data/contests_info.csv'

    try:
        response = requests.get(file_path)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        st.error(f"Erro ao acessar o arquivo: {e}")
        return None

    df = pd.read_csv(StringIO(response.text), sep=';')
    
    # 🔹 Garantir que "Início" e "Fim" estejam no formato datetime
    df["Início"] = pd.to_datetime(df["Início"], errors="coerce", dayfirst=True)
    df["Fim"] = pd.to_datetime(df["Fim"], errors="coerce", dayfirst=True)

    # 🔹 Remover linhas onde "Início" ou "Fim" não puderam ser convertidas
    df = df.dropna(subset=["Início", "Fim"])

    # 🔹 Corrigir valores da coluna "Vagas"
    df["Vagas"] = df["Vagas"].replace("Várias", None)
    df["Vagas"] = pd.to_numeric(df["Vagas"], errors="coerce").fillna(0).astype(int)

    df["Vagas"] = pd.to_numeric(df["Vagas"], errors="coerce").fillna(0).astype(int)
    return df

def get_css():
    """Retorna o CSS para estilização da página."""
    return """
    <style>
        * {
            padding: 0;
            margin: 0;
            max-width: 100% !important;
        }

        .block-container {
            padding: 0;
        }
        
        body {
            width: 100%;
            height: 100vh;
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            background-color: #f9f9f9;
        }
        .header {
            background-color:rgb(255, 255, 255);
            padding: 20px 50px;
            border-bottom: 3px solid #1e7a34;
            display: flex;
            justify-content: space-between;
            align-items: center;
            position: sticky;
            top: 50px;
            text-wrap: nowrap;
        }
        .header .logo {
            margin-left: 5%;
            font-size: 24px;
            font-weight: bold;
            color:rgb(2, 2, 2);
        }
        .header a {
            text-decoration: none;
            color: #ffffff;
            font-weight: bold;
            margin-left: 20px;
        }
        .relatorios {
            color: #ffffff;
            background-color: green;
            margin-left: 30px;
            padding: 10px 25px;
            border-radius: 8%;
        }
        .main-section {
            width: 100%;
            background-color: #dcdcdc;
            text-align: left;
            padding: 50px 20px;
        }
        .main-section h1 {
            margin-left: 7%;
            font-size: 36px;
            color: #333333;
        }
        .main-section p {
            font-size: 18px;
            color: #666666;
            margin: 20px 0 20px 7%;
        }
        .main-section .btn {
            display: inline-block;
            background-color: #32a852;
            color: white;
            padding: 10px 20px;
            border-radius: 5px;
            text-decoration: none;
            font-size: 16px;
            margin: 10px 10px 10px 7%;
        }
        .statistics-box {
            background: #ffffff;
            border-radius: 10px;
            padding: 35px;
            margin: 0px 7%;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            text-align: center;
            border: 2px solid #1e7a34;
        }
        .statistics {
            background-color: #dcdcdc;
            padding: 10px 20% 70px 20%;
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
        .footer {
            border-top: 3px solid green;
            background-color:rgb(255, 255, 255);
            padding: 20px;
            border-top: 2px solid #eaeaea;
            text-align: center;
            font-size: 14px;
            color:rgb(0, 0, 0);
        }
    </style>
    """

def render_body():
    """Renderiza o corpo principal da página."""
    template = """
    <div class="header">
        <div class="logo" style="color: #32a852;">  
            Concursei Br
        </div>
        <div>
            <a href="Dashboards"><span class="relatorios">Dashboards</span></a>
        </div>
    </div>

    <div class="main-section">
        <h1>Acompanhe as <br>publicações no <br> <div style="color:green">Concursei Br</div></h1>
        <p>Promovendo a participação pública em concursos do Brasil: <br>acompanhe de forma simples e clara as publicações de concursos.</p>
        <a href="Exportar" class="btn">Exportar Dados</a>
    </div>
    """
    return template

def render_statistics(df):
    """
    Renderiza o bloco estatístico com duas informações na mesma caixa:
    - Número de concursos com inscrições abertas (considerando apenas concursos únicos)
    - Soma total de vagas dos concursos com valor numérico na coluna 'Vagas'
    """
    # Remover ponto (separador de milhar) e converter para numérico
    df['Vagas_limpo'] = (df['Vagas']
                                  .astype(str)
                                  .str.replace('.', '', regex=False))
    df['Vagas_limpo'] = pd.to_numeric(df['Vagas_limpo'], errors='coerce')

    
    df['Vagas_limpo'] = df['Vagas_limpo'].fillna(0)

    total_vagas = df['Vagas_limpo'].sum()

    # Exibição das métricas no Streamlit
    st.markdown(f"""
        <div class="statistics" style="display: flex; justify-content: center;">
            <div class="statistics-box">
                <div style="margin-bottom: 20px;">
                    <div class="stat-label">Concursos com inscrições abertas HOJE</div>
                    <div class="stat-number">{len(df)}</div>
                </div>
                <div>
                    <div class="stat-label">Total de vagas HOJE</div>
                    <div class="stat-number">{int(total_vagas)}</div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

def render_footer():
    """Função que retorna o footer"""
    return """
    <div class="footer">
        © 2025 Concursei Br. Todos os direitos reservados.
    </div>
    """

def main():
    """Função principal para rodar o Streamlit."""
    set_page_config()
    df = load_data()
    df = df[df['Status'] == 'Aberto']

    st.markdown(get_css(), unsafe_allow_html=True)
    st.markdown(render_body(), unsafe_allow_html=True)
    
    render_statistics(df)
    st.markdown(render_footer(), unsafe_allow_html=True)

if __name__ == "__main__":
    main()