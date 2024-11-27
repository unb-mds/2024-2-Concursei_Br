import streamlit as st

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
        self.style = """
            <style>
                .main-header {
                    font-family: 'Arial', sans-serif;
                    text-align: center;
                    color: #2E86C1;
                    padding: 10px 0;
                }
                .sidebar {
                    background-color: #F4F6F7;
                    border-right: 2px solid #D5DBDB;
                }
            </style>
        """

    def display_header(self, title):
        st.markdown(self.style, unsafe_allow_html=True)
        st.markdown(f"<h1 class='main-header'>{title}</h1>", unsafe_allow_html=True)

    def display_sidebar(self):
        st.sidebar.markdown(self.style, unsafe_allow_html=True)
        st.sidebar.title("Dados do Governo")
        return st.sidebar.radio("Selecione uma aba", list(self.sidebar_options.keys()))

    # Métodos para cada aba
    def show_inicio(self):
        self.display_header("Bem-vindo ao Web App de Dados Governamentais!")
        st.write("Explore dados importantes sobre diversos setores do governo.")
        st.info("Use a barra lateral para navegar entre os setores.")

    def show_saude(self):
        self.display_header("Dados do Setor de Saúde")
        st.write("### Informações sobre Saúde Pública")
        st.write("Aqui você encontrará estatísticas, dados e análises do setor de saúde no Brasil.")

    def show_educacao(self):
        self.display_header("Dados do Setor de Educação")
        st.write("### Informações sobre Educação")
        st.write("Explore dados sobre escolas, universidades e programas educacionais no Brasil.")

    def show_seguranca(self):
        self.display_header("Dados do Setor de Segurança")
        st.write("### Informações sobre Segurança Pública")
        st.write("Descubra estatísticas sobre segurança, policiamento e políticas públicas de segurança.")

    def show_economia(self):
        self.display_header("Dados do Setor de Economia")
        st.write("### Informações sobre Economia")
        st.write("Analise dados sobre PIB, desemprego, inflação e outros indicadores econômicos.")

    def run(self):
        selected_option = self.display_sidebar()
        # Chama o método correspondente à aba selecionada
        self.sidebar_options[selected_option]()


if __name__ == "__main__":
    app = GovWebApp()
    app.run()
