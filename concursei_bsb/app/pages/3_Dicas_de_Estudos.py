import streamlit as st

st.set_page_config(page_title="Dicas de Estudo", page_icon="📝", layout="wide")

# Header estilizado
st.markdown(
    """
    <div class="header">
        <div class="logo">CONCURSOS BRASIL</div>
        <div class="nav">
            <a href="#inicio">Início</a>
            <a href="#calendario">Calendário</a>
            <a href="#editais" class="btn">Ver Editais →</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Conteúdo principal
st.title("Dicas de Estudo")
st.write("### Melhore sua preparação para concursos")
st.write("Nesta página você encontrará métodos de estudo eficazes para aumentar suas chances de aprovação:")
st.markdown(
    """
    - **Técnica Pomodoro**: Estude em blocos de 25 minutos com 5 minutos de pausa.
    - **Resumos**: Faça resumos curtos e diretos de cada matéria.
    - **Provas Anteriores**: Resolva questões de concursos passados para se familiarizar com o estilo.
    """
)
