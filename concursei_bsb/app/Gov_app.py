import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Configuração da página
st.set_page_config(page_title="Concursei BSB", layout="wide")

class GovWebApp:
    def __init__(self):
        self.pages = {
            "inicio": self.show_inicio,
            "relatorios": self.show_relatorios
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
                cursor: pointer; /* Adiciona o cursor de clique */
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
                cursor: pointer;
            }

            .header .nav a:hover {
                color: #236e1a; /* Efeito de hover no Início */
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
                margin-top: 100px;
            }
            </style>

            <div class="header">
                <div class="logo" onClick="window.location.href='/?page=inicio'" target="_self">CONCURSEI BSB</div>
                <div class="nav">
                    <a href="/?page=inicio" target="_self">Início</a>
                    <a href="/?page=relatorios" target="_self" class="btn">Ver Relatórios →</a>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    def main_content(self):
        st.markdown('<div class="main-content">', unsafe_allow_html=True)

    def subheader(self, text):
        st.markdown(f"<div class='main-header'>{text}</div>", unsafe_allow_html=True)

    def show_inicio(self):
        self.header()
        self.main_content()
        self.subheader("Monitore Concursos de Brasília")
        st.write("Explore dados importantes sobre diversos setores do governo.")
        st.info("Use os botões acima para navegar entre as opções disponíveis.")

        # Exemplo: gráfico de histograma
        data = np.random.randn(1000)
        fig, ax = plt.subplots()
        ax.hist(data, bins=30, color='skyblue', edgecolor='black')
        ax.set_title("Distribuição Exemplo")
        ax.set_xlabel("Valores")
        ax.set_ylabel("Frequência")
        st.pyplot(fig)

    def show_relatorios(self):
        self.header()
        self.main_content()
        self.subheader("Relatórios de Dados")
        st.write("Aqui você encontrará relatórios detalhados sobre concursos e dados relacionados.")

        # Exemplo: tabela de dados de concursos
        df = pd.DataFrame({
            "Concurso": ["Concurso A", "Concurso B", "Concurso C", "Concurso D"],
            "Inscritos": [1200, 950, 1500, 800],
            "Vagas": [50, 30, 70, 40],
            "Taxa de Inscrição (R$)": [100, 120, 80, 90],
            "Estado": ["DF", "SP", "RJ", "MG"],
        })
        st.write("### Detalhes dos Concursos")
        st.table(df)

        # Exemplo: gráfico de barras com dados de inscritos por concurso
        st.write("### Inscritos por Concurso")
        fig, ax = plt.subplots()
        ax.bar(df["Concurso"], df["Inscritos"], color="skyblue", edgecolor="black")
        ax.set_title("Inscritos por Concurso")
        ax.set_xlabel("Concurso")
        ax.set_ylabel("Número de Inscritos")
        st.pyplot(fig)

    def run(self):
        # Verifica a página atual com base no parâmetro na URL
        query_params = st.experimental_get_query_params()
        current_page = query_params.get("page", ["inicio"])[0]

        # Renderiza a página correspondente
        if current_page in self.pages:
            self.pages[current_page]()
        else:
            st.error("Página não encontrada!")


if __name__ == "__main__":
    app = GovWebApp()
    app.run()