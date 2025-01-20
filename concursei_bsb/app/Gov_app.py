import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Configuração da página
st.set_page_config(page_title="Concursei BSB", layout="wide")

class GovWebApp:
    def __init__(self):
        self.app_title = "Web App de dados relacionados a concursos"

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
                cursor: pointer;
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
                <div class="logo">CONCURSEI BSB</div>
                <div class="nav">
                    <a onClick="window.location.href='?page=inicio'" target="_self">Início</a>
                    <a onClick="window.location.href='?page=relatorios'" target="_self" class="btn">Ver Relatórios →</a>
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

        # Exemplo: tabela de dados
        df = pd.DataFrame({
            "Concurso": ["Concurso A", "Concurso B", "Concurso C"],
            "Inscritos": [1200, 950, 1500],
            "Vagas": [50, 30, 70],
        })
        st.table(df)

    def run(self):
        # Use o session_state para definir a página atual
        if "page" not in st.session_state:
            st.session_state.page = "inicio"

        # Navegação entre páginas
        if st.session_state.page == "inicio":
            self.show_inicio()
        elif st.session_state.page == "relatorios":
            self.show_relatorios()

        # Adiciona scripts JavaScript para mudar o estado no session_state ao clicar
        st.markdown(
            """
            <script>
            const links = document.querySelectorAll('.nav a');
            links.forEach(link => {
                link.addEventListener('click', (e) => {
                    const href = link.getAttribute('onClick').split("'")[1];
                    e.preventDefault();
                    const queryParam = href.split('=')[1];
                    window.location.href = href; 
                    Streamlit.setComponentValue({"page": queryParam});
                });
            });
            </script>
            """,
            unsafe_allow_html=True,
        )


if __name__ == "__main__":
    app = GovWebApp()
    app.run()