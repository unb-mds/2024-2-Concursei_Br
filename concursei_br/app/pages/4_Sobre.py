import streamlit as st

try:
    st.set_page_config(page_title="Sobre o Concursei BR", page_icon="assets/logo_concursei.png", layout="wide")
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

render_header()

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
        .team-section {
            width: 100%;
            background-color: #ffffff;
            text-align: center;
            padding: 50px 20px;
        }
        .team-section h2 {
            font-size: 30px;
            color: #333333;
            margin-bottom: 40px;
        }
        .team-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 50px;
        }
        .team-row {
            display: flex;
            justify-content: center;
            gap: 50px;
            flex-wrap: wrap;
        }
        .team-member {
            width: 220px;
            text-align: center;
        }
        .team-member img {
            width: 150px;
            height: 150px;
            border-radius: 50%;
            object-fit: cover;
            border: 3px solid #32a852;
        }
        .team-member h3 {
            font-size: 20px;
            color: #333333;
            margin-top: 10px;
            text-align: center;
        }
        .team-member a {
            text-decoration: none;
            color: #32a852;
            font-weight: bold;
            display: inline-block;
            margin-top: 5px;
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

    <div class="main-section">
        <h1>Sobre o Concursei BR</h1>
        <p>
            O objetivo do Concursei BR é criar um painel de concursos com inscrições em aberto e previstos que seja intuitivo e que permita aos cidadãos monitorar e se programar facilmente 
            para concursos de seu interesse. A ideia é que os dados sejam 
            atualizados periodicamente e que todos tenham a oportunidade de saber e participar.
        </p>
        <p>
            Acreditamos que a informação de qualidade é a chave para a cidadania ativa. Aqui você encontrará visões facilitadas de concursos para que você possa se organizar da melhor forma possível. 
        </p>
        <p>
            Esse projeto foi feito para a disciplina de Métodos de Desenvolvimento de Software - Engenharia de Software UnB.
        </p>
        <p>
            🔗 <a href="https://unb-mds.github.io/2024-2-Concursei_Br/" target="_blank">Gitpages do Projeto</a>
        </p>
        <p>
            📂 <a href="https://github.com/unb-mds/2024-2-Concursei_Br" target="_blank">Repositório no GitHub</a>
        </p>
    </div>

    <div class="team-section">
        <h2>Nosso Time</h2>
        <div class="team-container">
            <div class="team-row">
                <div class="team-member">
                    <img src="https://avatars.githubusercontent.com/u/133173588?v=4" alt="Participante 1">
                    <h3>Luiz Bessa</h3>
                    <a href="https://github.com/lfelipebessa" target="_blank">GitHub</a>
                </div>
                <div class="team-member">
                    <img src="https://avatars.githubusercontent.com/u/135292465?v=4" alt="Participante 2">
                    <h3>José Victor</h3>
                    <a href="https://github.com/RR2M4A" target="_blank">GitHub</a>
                </div>
                <div class="team-member">
                    <img src="https://avatars.githubusercontent.com/u/144077153?v=4" alt="Participante 3">
                    <h3>Eduardo Waski</h3>
                    <a href="https://github.com/EduardoWaski" target="_blank">GitHub</a>
                </div>
            </div>
            <div class="team-row">
                <div class="team-member">
                    <img src="https://avatars.githubusercontent.com/u/144404621?v=4" alt="Participante 4">
                    <h3>André Meyer</h3>
                    <a href="https://github.com/AndreMeyerr" target="_blank">GitHub</a>
                </div>
                <div class="team-member">
                    <img src="https://avatars.githubusercontent.com/u/110571317?v=4" alt="Participante 5">
                    <h3>Artur de Camargos</h3>
                    <a href="https://github.com/ArturDCR" target="_blank">GitHub</a>
                </div>
                <div class="team-member">
                    <img src="https://avatars.githubusercontent.com/u/108733538?v=4" alt="Participante 6">
                    <h3>Marco Marques</h3>
                    <a href="https://github.com/marcomarquesdc" target="_blank">GitHub</a>
                </div>
            </div>
        </div>
    </div>

    <div class="footer">
        © 2025 Concursei BR. Todos os direitos reservados.
    </div>
    """,
    unsafe_allow_html=True,
)