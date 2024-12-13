import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


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
            .navbar {
                background-color: #0FFEF9;
                padding: 10px;
                position: fixed;
                top: 35px;
                left: 0;
                width: 100%;
                z-index: 10;
                text-align:center;
                height: 10px;
            }
            .navbar h1 {
                color: white;
                font-family: 'Arial', sans-serif;
                margin: 0;
                display: inline-block;
            }
            .navbar-icons {
                float: right;
                margin-top: -35px;
            }
            .navbar-icons img {
                width: 30px;
                margin-left: 10px;
                cursor: pointer;
            }
            /* Adiciona espaçamento extra ao conteúdo principal */
            .main-content {
                margin-top: 100px; /* Ajusta o espaço para evitar sobreposição */
            }
            .main-header {
                font-family: 'Arial', sans-serif;
                color: #0FFEF9;
                text-align: left;
                margin-top: 20px;
                font-size: 28px;
                font-weight: bold;
            }
            .sub-header {
                font-family: 'Arial', sans-serif;
                color: #0FFEF9;
                text-align: left;
                font-size: 18px;
                margin-bottom: 20px;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )
        # Barra de navegação
        st.markdown(
            """
            <div class="navbar">
                <h1>DATA GOV</h1>
                <div class="navbar-icons">
                    <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="GitHub">
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    def subheader(self):
        st.markdown("<div class='main-header'>Monitore Licitações do GOV</div>", unsafe_allow_html=True)
        st.markdown("<div class='sub-header'>Dados Provenientes do Diário Oficial!</div>", unsafe_allow_html=True)

    def display_sidebar(self):
        st.sidebar.title("Dados do Governo")
        return st.sidebar.radio("Selecione uma aba", list(self.sidebar_options.keys()))

    # Métodos para cada aba
    def show_inicio(self):
        self.header()  # Exibe o header
        self.subheader()  # Exibe o subheader
        st.write("Explore dados importantes sobre diversos setores do governo.")
        st.info("Use a barra lateral para navegar entre os setores.")

    def show_saude(self):
        self.header()
        self.subheader()
        st.write("### Informações sobre Saúde Pública")
        st.write("Aqui você encontrará estatísticas, dados e análises do setor de saúde no Brasil.")
        # Dados de exemplo
        data = np.random.randn(1000)

        st.title("Histograma de licitações por período ")

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
        self.subheader()
        st.write("### Informações sobre Educação")
        st.write("Explore dados sobre escolas, universidades e programas educacionais no Brasil.")

    def show_seguranca(self):
        self.header()
        self.subheader()
        st.write("### Informações sobre Segurança Pública")
        st.write("Descubra estatísticas sobre segurança, policiamento e políticas públicas de segurança.")

    def show_economia(self):
        self.header()
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