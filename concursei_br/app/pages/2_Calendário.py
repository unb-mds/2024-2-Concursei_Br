from datetime import datetime
import calendar
from Home import load_data
import pandas as pd
import streamlit as st

try:
    st.set_page_config(
        page_title="Calendário de Concursos",
        layout="wide",
        page_icon="assets/logo_concursei.png"
    )
except:
    pass  # Evita erro se `set_page_config()` já foi chamado antes

# Função para renderizar o Header igual ao Dashboard
def render_header():
    """Renderiza o cabeçalho da página, mantendo o estilo da home."""
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


#css da página
st.markdown("""
<style>
:root {
    --primary-color: #32a852;
}

/* Títulos e selectbox em verde */
h1, h2, h3 {
    color: var(--primary-color) !important;
}
.stSelectbox label p {
    color: var(--primary-color) !important;
    font-weight: bold !important;
}

/* No modo light */
html[data-theme="light"] .dia-evento {
    background: #ffffff !important;
    color: #000000 !important;
    border: 1px solid rgba(0,0,0,0.1);
}

/* No modo dark */
html[data-theme="dark"] .dia-evento {
    background: #333333 !important;
    color: #ffffff !important;
    border: 1px solid #555555;
}
</style>
""", unsafe_allow_html=True)



# Streamlit app
render_header()

# Criando um layout com espaçamento lateral (igual ao Dashboard)
espaco_esquerda, conteudo_principal, espaco_direita = st.columns([0.03, 0.94, 0.03])  # 3% - 94% - 3%

# Espaço principal com bordas
with conteudo_principal:
    #lendo o csv e filtrando os dados que queremos
    df = load_data()
    invalid_values = ["Não encontrado", "Previsto"]
    df = df[~df["Início"].isin(invalid_values) & ~df["Fim"].isin(invalid_values)].copy()
    df["Início"] = pd.to_datetime(df["Início"], dayfirst=True, errors="coerce")
    df["Fim"] = pd.to_datetime(df["Fim"], dayfirst=True, errors="coerce")
    df = df.dropna(subset=["Início", "Fim"])

    # Filtrar anos válidos (a partir de 2000)
    available_years = sorted(set(df["Início"].dt.year.dropna().tolist() + 
                                df["Fim"].dt.year.dropna().tolist()))
    available_years = [year for year in available_years if year >= 2000]

    # Filtrar regiões disponíveis
    available_regions = sorted(df["Região"].dropna().unique().tolist())

    # Adicionando a opção "Todos" no filtro de região
    available_regions.insert(0, "Todos")

    st.title("📅 Calendário de Concursos Públicos")

    # Filtros de seleção
    st.subheader("Selecione o período e a região")
    col1, col2, col3 = st.columns(3)

    with col1:
        selected_year = st.selectbox("Ano", options=available_years)
    with col2:
        selected_month = st.selectbox("Mês", options=range(1, 13), format_func=lambda x: calendar.month_name[x])
    with col3:
        selected_region = st.selectbox("Região", options=available_regions)

        
    # Criar calendário
    def create_calendar(year, month, region):
        cal = calendar.monthcalendar(year, month)

        if region == "Todos":
            filtered_df = df
        else:    
            filtered_df = df[df["Região"] == region]
        
        cols = st.columns(7)
        days = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"]
        for col, day in zip(cols, days):
            col.markdown(
                f"<div style='text-align: center; padding: 10px; background: #32a852; color: white; border-radius: 5px;'><strong>{day}</strong></div>", 
                unsafe_allow_html=True
            )

        for week in cal:
            cols = st.columns(7)
            for day, col in zip(week, cols):
                if day == 0:
                    col.write("")
                    continue
                
                current_date = datetime(year, month, day)
                contests = filtered_df[(filtered_df['Início'].dt.date == current_date.date()) | 
                                    (filtered_df['Fim'].dt.date == current_date.date())]
                
                with col:
                    if contests.empty:
                        st.markdown(f"<div class='dia-evento' style='text-align: center;'>{day}</div>", unsafe_allow_html=True)
                    else:
                        with st.container():
                            st.markdown(f"<div class='dia-evento'>", unsafe_allow_html=True)
                            st.markdown(f"**{day}**")
                            for _, contest in contests.iterrows():
                                event_type = "🔹 Início" if contest['Início'].date() == current_date.date() else "🔴 Fim"
                                st.markdown(f"""
                                **{contest['Nome']}**  
                                {event_type}  
                                Vagas: {contest['Vagas']}  
                                """)
                            st.markdown("</div>", unsafe_allow_html=True)

    st.divider()
    st.header(f"Calendário para {calendar.month_name[selected_month]} {selected_year} - {selected_region}")
    create_calendar(selected_year, selected_month, selected_region)

    #legenda do calendário
    st.info("""
    **Legenda:**  
    🔹 = Data de Início das Inscrições do Concurso  
    🔴 = Data de Término das Inscrições do Concurso  
    """)

#footer da página
st.markdown("""
<style>   
    .footer {
        background-color: #ffffff;
        padding: 20px;
        border-top: 2px solid #eaeaea;
        text-align: center;
        font-size: 14px;
        color: #666666;
    }
</style>
<div class="footer">
    © 2025 Concursei Br. Todos os direitos reservados.
</div>
""", unsafe_allow_html=True)