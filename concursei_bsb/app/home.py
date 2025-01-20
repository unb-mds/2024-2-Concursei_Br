import streamlit as st

# Configuração da página
st.set_page_config(page_title="Início", page_icon="🏠", layout="wide")

# Função para renderizar o cabeçalho
def render_header():
    st.markdown(
        """
        <style>
        /* Estilos do cabeçalho */
        .header {
            position: fixed; /* Fixa o cabeçalho no topo */
            top: 0;
            left: 0;
            width: 100%;
            background-color: #90ee90; /* Verde claro */
            padding: 64px 45px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* Sombra elegante */
            z-index: 1000;
        }
        .header .logo {
            font-size: 1.8em;
            font-weight: bold;
            color: #004d00; /* Verde escuro */
        }
        .header .nav {
            display: flex;
        }
        .header .nav a {
            background-color: white;
            color: #004d00; /* Verde escuro */
            text-decoration: none;
            padding: 10px 15px;
            margin: 0 5px;
            border-radius: 5px;
            font-size: 1em;
            font-weight: bold;
            transition: background-color 0.3s ease;
        }
        .header .nav a:hover {
            background-color: #e6ffe6; /* Verde mais claro ao passar o mouse */
        }
        .header .page-title {
            font-size: 1.2em;
            font-weight: bold;
            color: #004d00; /* Verde escuro */
        }
        .spacer {
            height: 80px; /* Espaço para o cabeçalho fixo */
        }
        </style>
        <div class="header">
            <div class="logo">CONCURSOS BRASIL</div>
            <div class="nav">
                <a href="/Home" target="_self">Início</a>
                <a href="/pages/1_Calendário" target="_self">Calendário</a>
                <a href="/pages/2_Dicas_de_Estudo" target="_self">Dicas de Estudo</a>
                <a href="/pages/3_Editais_e_Provas" target="_self">Editais</a>
                <a href="/pages/4_Notícias" target="_self">Notícias</a>
            </div>
            <div class="page-title">Concursei BSB</div>
        </div>
        <div class="spacer"></div>
        """,
        unsafe_allow_html=True,
    )

# Renderizar o cabeçalho
render_header()

# Conteúdo principal
st.title("Bem-vindo ao Concursos Brasil!")
st.write("Descubra informações úteis sobre concursos públicos e prepare-se para as melhores oportunidades.")
st.info("Use o menu acima ou lateral para explorar informações sobre calendários, dicas de estudo, editais e muito mais!")
