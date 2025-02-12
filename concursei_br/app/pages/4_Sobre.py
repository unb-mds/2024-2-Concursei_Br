import streamlit as st
from utils.data_loader import load_contests_data

st.set_page_config(page_title="Sobre o Concursei BR", page_icon="assets/logo_concursei.png", layout="wide")

# Header estilizado
st.markdown(
    """
    <style>
        body {
            width: 100%;
            font-family: Arial, sans-serif;
            background-color: #f9f9f9;
            margin: 0;
            padding: 0;
        }
        .header {
            background-color: #ffffff;
            padding: 20px 50px;
            border-bottom: 3px solid #eaeaea;
            display: flex;
            align-items: center;
            position: sticky;
            top: 0;
        }
        .header .logo {
            margin-left: 5%;
            font-size: 24px;
            font-weight: bold;
            color: #32a852;
            text-decoration: none;
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
        .footer {
            background-color: #ffffff;
            padding: 20px;
            border-top: 2px solid #eaeaea;
            text-align: center;
            font-size: 14px;
            color: #666666;
        }
    </style>

    <div class="header">
        <div class="logo">Concursei BR</div>
    </div>

    <!-- Seção principal com informações sobre o site -->
    <div class="main-section">
        <h1>Sobre o Concursei BR</h1>
        <p>
            O objetivo do concursei BR é criar um painel de concursos com inscrição em aberto e previstos que seja intuitivo e que permita aos cidadãos monitorar e se programar facilmente 
            para concursos de seu interresse. A ideia é que os dados sejam 
            atualizados periodicamente e que todos tenham a oportunidade de saber e participar.
        </p>
        <p>
            Acreditamos que a informação de qualidade é a chave para a cidadania ativa. Aqui você encontrará visões facilitadas de concursos para que você possa se organizar da melhor forma possível. 
        </p>
        <p>
            Esse projeto foi feito para a disciplina de Métodos de Desenvolvimento de Software - Engenharia de Software UnB
    </div>

    <!-- Footer -->
    <div class="footer">
        © 2025 Concursei BR. Todos os direitos reservados.
    </div>
    """,
    unsafe_allow_html=True,
)


