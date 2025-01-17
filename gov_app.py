import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Configuração da página (deve ser feita no início)
st.set_page_config(page_title="DATA GOV", layout="wide")

class GovWebApp:
    def __init__(self):
        self.app_title = "Web App de Dados Governamentais"
        self.sidebar_options = {
            "Início": self.show_inicio,
            "Saúde": self.show_saude,
            "Educação": self.show_educacao,
            "Segurança": self.show_seguranca,
            "Economia": self.show_economia,
        }

    def header(self):
        st.markdown(
            """
            <style>
            /* Estilo do header */
            .header {
                background-color: #28a745; /* Verde */
                border: none;
                padding: 20px;
                position: fixed;
                top: 60px;
                left: 0;
                width: 100%;
                z-index: 1000;
                text-align: center;
                display: flex;
                justify-content: space-between;
                align-items: center;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            }

            .header .logo {
                font-size: 30px;
                font-weight: bold;
                color: white;
                margin-left: 20px;
            }
            .header .nav {
                display: flex;
                align-items: center;
            }

            .header .nav a {
                margin: 0 10px;
                text-decoration: none;
                color: white;
                font-weight: bold;
            }

            .header .btn {
                background-color: white;
                border: none;
                color: #28a745 !important; /* Cor do texto do botão */
                padding: 10px 20px;
                border-radius: 5px;
                text-decoration: none;
                font-weight: bold;
                font-size: 18px;
            }

            .header .btn:hover {
                background-color: #236e1a;
                color: white !important;
            }

            /* Espaçamento para evitar sobreposição */
            .main-content {
                margin-top: 80px;
            }
            </style>

            <div class="header">
                <div class="logo">DATA GOV</div>
                <div class="nav">
                    <a href="#inicio">Início</a>
                    <a href="#relatorios">Relatórios</a>
                    <a href="#contato" class="btn">Ver Relatórios →</a>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    def main_content(self):
        st.markdown('<div class="main-content">', unsafe_allow_html=True)

    def subheader(self):
        st.markdown("<div class='main-header'>Monitore Licitações do GOV</div>", unsafe_allow_html=True)
        st.markdown("<div class='sub-header'>Dados Provenientes do Diário Oficial!</div>", unsafe_allow_html=True)

    def display_sidebar(self):
        st.sidebar.title("Dados do Governo")
        return st.sidebar.radio("Selecione uma aba", list(self.sidebar_options.keys()))

    # Métodos para cada aba
    def show_inicio(self):
        self.header()  # Exibe o header
        self.main_content()  # Ajusta o conteúdo principal
        self.subheader()  # Exibe o subheader
        st.write("Explore dados importantes sobre diversos setores do governo.")
        st.info("Use a barra lateral para navegar entre os setores.")

    def show_saude(self):
        self.header()
        self.main_content()
        self.subheader()
        st.write("### Informações sobre Saúde Pública")
        st.write("Aqui você encontrará estatísticas, dados e análises do setor de saúde no Brasil.")
        # Dados de exemplo
        data = np.random.randn(1000)

        st.title("Histograma de licitações por período")

        # Criando o histograma
        fig, ax = plt.subplots()
        ax.hist(data, bins=30, color='skyblue', edgecolor='black')
        ax.set_title("Histograma")
        ax.set_xlabel("Valores")
        ax.set_ylabel("Frequência")

        # Exibindo no Streamlit
        st.pyplot(fig)

    def show_educacao(self):
        self.header()
        self.main_content()
        self.subheader()
        st.write("### Informações sobre Educação")
        st.write("Explore dados sobre escolas, universidades e programas educacionais no Brasil.")

    def show_seguranca(self):
        self.header()
        self.main_content()
        self.subheader()
        st.write("### Informações sobre Segurança Pública")
        st.write("Descubra estatísticas sobre segurança, policiamento e políticas públicas de segurança.")

    def show_economia(self):
        self.header()
        self.main_content()
        self.subheader()
        st.write("### Informações sobre Economia")
        st.write("Analise dados sobre PIB, desemprego, inflação e outros indicadores econômicos.")

    def run(self):
        selected_option = self.display_sidebar()
        # Chama o método correspondente à aba selecionada
        self.sidebar_options[selected_option]()


if __name__ == "__main__":
    app = GovWebApp()
    app.run()
