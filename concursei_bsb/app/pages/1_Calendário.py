import streamlit as st

st.set_page_config(page_title="Calendário", page_icon="📅", layout="wide")

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
st.title("Calendário de Concursos")
st.write("### Confira os próximos concursos públicos!")
st.write("Esta seção contém uma lista atualizada dos principais concursos com prazos importantes.")
st.warning("Exemplo: Concurso IBGE 2025 - Inscrições até 31/01/2025.")
