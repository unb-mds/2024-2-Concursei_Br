import streamlit as st
import pandas as pd
from datetime import datetime
import calendar

#nome da página e configurações gerais da página
st.set_page_config(
    page_title="Calendário de Concursos",
    layout="wide",
    page_icon="assets/logo_concursei.png"
)

#css da página
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
    
    [data-testid="stVerticalBlock"] > div:nth-child(2) > div {
        border-radius: 8px !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1) !important;
    }
    
    hr {
        border-color: var(--primary-color) !important;
    }
    
    [data-testid="stNotificationContent"] {
        background-color: #f8fff9 !important;
    }
    
    .dia-evento {
        background: white !important;
        padding: 10px !important;
        margin: 4px !important;
    }
</style>
""", unsafe_allow_html=True)

#lendo o csv e filtrando os dados que queremos
df = pd.read_csv("../data/contests_info.csv", sep=";")
df['Início'] = pd.to_datetime(df['Início'], dayfirst=True, errors='coerce')
df['Fim'] = pd.to_datetime(df['Fim'], dayfirst=True, errors='coerce')
df = df.dropna(subset=['Início', 'Fim'])

st.title("📅 Calendário de Concursos Públicos")

#filtro de meses e anos
st.subheader("Selecione o período")
col1, col2 = st.columns(2)
with col1:
    available_years = sorted(df['Início'].dt.year.unique().tolist() + df['Fim'].dt.year.unique().tolist())
    selected_year = st.selectbox("Ano", options=available_years)

with col2:
    selected_month = st.selectbox("Mês", options=range(1, 13), format_func=lambda x: calendar.month_name[x])

#criação do calendário
def create_calendar(year, month):
    cal = calendar.monthcalendar(year, month)
    
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
            contests = df[(df['Início'].dt.date == current_date.date()) | 
                         (df['Fim'].dt.date == current_date.date())]
            
            with col:
                if contests.empty:
                    st.markdown(f"<div class='dia-evento' style='text-align: center;'>{day}</div>", unsafe_allow_html=True)
                else:
                    with st.container():
                        st.markdown(f"<div class='dia-evento'>", unsafe_allow_html=True)
                        st.markdown(f"**{day}**")
                        for _, contest in contests.iterrows():
                            event_type = "🔵 Início" if contest['Início'].date() == current_date.date() else "🔴 Fim"
                            st.markdown(f"""
                            **{contest['Nome']}**  
                            {event_type}  
                            Vagas: {contest['Vagas']}  
                            """)
                        st.markdown("</div>", unsafe_allow_html=True)

st.divider()
st.header(f"Calendário para {calendar.month_name[selected_month]} {selected_year}")
create_calendar(selected_year, selected_month)

#legenda do calendário
st.info("""
**Legenda:**  
🔵 = Data de Início do Concurso  
🔴 = Data de Término do Concurso  
Clique nos cards para expandir detalhes
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
    © 2025 Concursei BSB. Todos os direitos reservados.
</div>
""", unsafe_allow_html=True)