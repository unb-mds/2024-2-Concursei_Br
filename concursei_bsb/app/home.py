import streamlit as st
import pandas as pd

def set_page_config():
    st.set_page_config(
        page_title="Concursei Br",
        layout="wide",
        page_icon="assets/logo_concursei.png"
    )

def load_data():
    """Carrega e processa os dados do CSV."""
    file_path = "../data/contests_info.csv"
    df = pd.read_csv(file_path, sep=';')
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
            background-color: #32a852;
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
            color: #ffffff;
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
            background-color: #32a852;
            padding: 20px;
            border-top: 2px solid #eaeaea;
            text-align: center;
            font-size: 14px;
            color: #ffffff;
        }
    </style>
    """

def render_body():
    """Renderiza o corpo principal da página."""
    template = """
    <div class="header">
        <div class="logo">  
            Concursei Br
        </div>
        <div>
            <a href="#">Início</a>
            <a href="#"><span class="relatorios">Relatórios</span></a>
        </div>
    </div>

    <div class="main-section">
        <h1>Acompanhe as <br>publicações no <br> <div style="color:green">Concursei Br</div></h1>
        <p>Promovendo a participação pública em concursos do Brasil: <br>acompanhe de forma simples e clara as publicações de concursos.</p>
        <a href="#" class="btn">Ver Relatórios</a>
    </div>
    """
    return template

def render_statistics(df):
    """
    Renderiza o bloco estatístico com duas informações na mesma caixa:
    - Número de concursos com inscrições abertas (considerando apenas concursos em que 'Vagas' é numérico)
    - Soma total de vagas dos concursos com valor numérico na coluna 'Vagas'
    """
    # Filtra os concursos onde a coluna 'Vagas' contém um valor numérico
    df_numeric = df[pd.to_numeric(df['Vagas'], errors='coerce').notnull()].copy()
    df_numeric['Vagas'] = pd.to_numeric(df_numeric['Vagas'])
    
    # Calcula a quantidade de concursos abertos dentre os concursos com vagas numéricas
    abertos = df_numeric[df_numeric['Status'] == 'Aberto'].shape[0]
    # Calcula a soma total de vagas
    total_vagas = df_numeric['Vagas'].sum()
    
    return f"""
    <div class="statistics" style="display: flex; justify-content: center;">
        <div class="statistics-box">
            <div style="margin-bottom: 20px;">
                <div class="stat-label">Concursos com inscrições abertas HOJE</div>
                <div class="stat-number">{abertos}</div>
            </div>
            <div>
                <div class="stat-label">Total de vagas</div>
                <div class="stat-number">{int(total_vagas)}</div>
            </div>
        </div>
    </div>
    """

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

    st.markdown(get_css(), unsafe_allow_html=True)
    st.markdown(render_body(), unsafe_allow_html=True)
    
    st.markdown(render_statistics(df), unsafe_allow_html=True)
    st.markdown(render_footer(), unsafe_allow_html=True)

if __name__ == "__main__":
    main()