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

        # 1. Criar dados fictícios com mês, trimestre, semestre e número de licitações.
        # Neste exemplo, temos 12 linhas (Janeiro a Dezembro de 2025).
        data = {
            "Mes": [
                "Janeiro", "Fevereiro", "Março", 
                "Abril", "Maio", "Junho", 
                "Julho", "Agosto", "Setembro", 
                "Outubro", "Novembro", "Dezembro"
            ],
            "Trimestre": [
                "Q1", "Q1", "Q1", 
                "Q2", "Q2", "Q2", 
                "Q3", "Q3", "Q3", 
                "Q4", "Q4", "Q4"
            ],
            "Semestre": [
                "S1", "S1", "S1", 
                "S1", "S1", "S1", 
                "S2", "S2", "S2", 
                "S2", "S2", "S2"
            ],
            # Número de licitações fictício
            "NumeroLic": [10, 12, 9, 15, 18, 13, 17, 14, 20, 22, 19, 25]
        }
        df_saude = pd.DataFrame(data)

        # Exibir a tabela completa se desejar
        st.write("#### Licitações Mensais (Tabela Completa)")
        st.dataframe(df_saude)

        # 2. Criar um filtro para o usuário selecionar o tipo de visualização
        filtro_periodo = st.radio(
            "Selecione o período para visualização:",
            ("Mensal", "Trimestral", "Semestral")
        )

        # 3. Agrupar ou não os dados dependendo do filtro selecionado
        if filtro_periodo == "Mensal":
            # Não precisamos agrupar, pois já temos dados mensais
            df_plot = df_saude[["Mes", "NumeroLic"]].copy()
            df_plot.rename(columns={"Mes": "Periodo", "NumeroLic": "TotalLic"}, inplace=True)

        elif filtro_periodo == "Trimestral":
            # Agrupa por trimestre somando o número de licitações
            df_plot = df_saude.groupby("Trimestre", as_index=False)["NumeroLic"].sum()
            df_plot.rename(columns={"Trimestre": "Periodo", "NumeroLic": "TotalLic"}, inplace=True)

        else:  # "Semestral"
            df_plot = df_saude.groupby("Semestre", as_index=False)["NumeroLic"].sum()
            df_plot.rename(columns={"Semestre": "Periodo", "NumeroLic": "TotalLic"}, inplace=True)

        # 4. Exibir a tabela resultante do agrupamento
        st.write(f"### Tabela - Agrupamento {filtro_periodo}")
        st.dataframe(df_plot)

        # 5. Plotar o gráfico de barras
        fig, ax = plt.subplots()
        ax.bar(df_plot["Periodo"], df_plot["TotalLic"], color="skyblue", edgecolor="black")
        ax.set_title(f"Número de Licitações por Período ({filtro_periodo}) - Saúde")
        ax.set_xlabel("Período")
        ax.set_ylabel("Nº de Licitações")
        plt.xticks(rotation=0)  # ajuste de rotação nos rótulos do eixo X (se necessário)

        # Exibir no Streamlit
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