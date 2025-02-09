import streamlit as st
import pandas as pd
from datetime import datetime
import calendar

# Configuração da página
st.set_page_config(
    page_title="Calendário de Concursos",
    layout="wide",
    page_icon="assets/logo_concursei.png"
)

# CSS da página
st.markdown("""
<style>
    :root {
        --primary-color: #32a852;
        --background-color: #ffffff;
    }
    .stApp {
        background-color: var(--background-color);
    }
    h1, h2, h3 {
        color: var(--primary-color) !important;
    }
    .stSelectbox label p {
        color: var(--primary-color) !important;
        font-weight: bold !important;
    }
    hr {
        border-color: var(--primary-color) !important;
    }
    .dia-evento {
        background: white !important;
        padding: 10px !important;
        margin: 4px !important;
    }
</style>
""", unsafe_allow_html=True)

# Carregar e limpar os dados
df = pd.read_csv("../data/contests_info.csv", sep=";")
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

# Legenda do calendário
st.info("""
**Legenda:**  
🔹 = Data de Início do Concurso  
🔴 = Data de Término do Concurso  
""")

# Footer da página
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
