import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import plotly.express as px
import plotly.graph_objects as go

import folium
from streamlit_folium import folium_static
from folium.plugins import HeatMap
from datetime import datetime
import requests
from io import StringIO

try:
    st.set_page_config(page_title="Dashboards", page_icon="../assets/logo_concursei.png", layout="wide")
except:
    pass

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

def render_footer():
    """Renderiza o rodapé da página."""
    st.markdown(
        """
        <style>
            .footer { 
                border-top: 3px solid #1e7a34;
                background-color: rgb(255, 255, 255);
                padding: 20px;
                text-align: center;
                font-size: 14px;
                color: rgb(0, 0, 0);
            }
        </style>
        <div class="footer">
            © 2025 Concursei Br. Todos os direitos reservados.
        </div>
        """,
        unsafe_allow_html=True
    )

@st.cache_data
def load_data():

    """Carrega e processa os dados do CSV."""
    file_path = 'https://raw.githubusercontent.com/unb-mds/2024-2-Concursei_Br/front/concursei_br/data/contests_info.csv'

    try:
        response = requests.get(file_path)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        st.error(f"Erro ao acessar o arquivo: {e}")
        return None

    df = pd.read_csv(StringIO(response.text), sep=';')

    # Carrega e trata os dados do CSV.
    #df = pd.read_csv("../data/contests_info.csv", sep=';')

    # Remover espaços extras e valores inconsistentes na coluna STATUS
    df['Status'] = df['Status'].astype(str).str.strip()

    # Tratamento da coluna início
    df["Início"] = df["Início"].astype(str).str.strip()  # Remove espaços extras
    df["Início"] = df["Início"].replace("Previsto", None)  # Substitui "Previsto" por None manualmente
    df["Início"] = pd.to_datetime(df["Início"], errors="coerce") # Converte para datetime (os erros viram NaN)
    df["Vagas"] = pd.to_numeric(df["Vagas"], errors="coerce").fillna(0).astype(int)
    
    # Tratamento DATAS
    # Converter datas para formato datetime
    df["Início"] = pd.to_datetime(df["Início"], errors="coerce", dayfirst=True)
    df["Fim"] = pd.to_datetime(df["Fim"], errors="coerce", dayfirst=True)

    # Criar uma nova coluna de mês referência
    df["Mês_Referência"] = df["Início"].dt.strftime("%m/%Y")
    df["Mês_Referência"] = df["Mês_Referência"].fillna("Previsto")

    # Excluir linhas onde a coluna "Status" contém "Previsto"
    df = df[df["Status"].notna()]

    return df

def plot_pie_chart(df):
    status_counts = df["Status"].value_counts()

    if "Aberto" not in status_counts:
        status_counts["Aberto"] = 0
    if "Previsto" not in status_counts:
        status_counts["Previsto"] = 0

    custom_color_map = {
        "Aberto": "#2ecc71",
        "Previsto": "#FFD700"
    }

    fig = px.pie(
        names=status_counts.index,
        values=status_counts.values,
        title="Proporção de Concursos Abertos/Previstos",
        color=status_counts.index,
        color_discrete_map=custom_color_map
    )

    # Ajustes do rótulo
    fig.update_traces(
        textinfo="none",
        texttemplate=(
            "<span style='font-size:16px; font-weight:bold; "
            "background-color: rgba(0,0,0,0.8); color:#fff; "
            "padding:4px; border-radius:4px;'>"
            # Exibe "Status", depois a porcentagem e o valor bruto
            "%{label}<br>%{percent} (%{value:,d})</span>"
        ),
        textfont=dict(size=16, color="white"),
        hovertemplate="<b>%{label}</b><br>Quantidade: %{value}<br>Proporção: %{percent}"
    )

    # Remove a anotação central (excluir ou deixar vazio)
    fig.update_layout(
        height=600,
        annotations=[],
        title_x = 0.25
    )

    # Borda ao redor das fatias
    fig.update_traces(
        marker=dict(line=dict(color='#808080', width=2))
    )

    st.plotly_chart(fig, use_container_width=True)




def plot_bar_vagas_estado(df):
    # Gráfico de barras: quantidade de vagas por estado.
    # Agrupar por Estado (Região) e somar as vagas
    vagas_por_estado = df.groupby("Região")["Vagas"].sum().reset_index()

    # Ordenar por número de vagas
    vagas_por_estado = vagas_por_estado.sort_values(by="Vagas", ascending=False)

    # Criar o gráfico de barras interativo
    fig = px.bar(
        vagas_por_estado,
        x="Região",
        y="Vagas",
        title="Quantidade de Vagas por Estado",
        text="Vagas",  # Exibir os valores sobre as barras
        color="Vagas",  # Cores diferenciadas por estado
        color_continuous_scale="Greens"  # Paleta de cores
    )
    
    # Ajustar a exibição dos rótulos
    fig.update_traces(texttemplate="%{text:.0f}", textposition="outside")
    fig.update_layout(
        xaxis_title="Estado",
        yaxis_title="Quantidade de Vagas",
        xaxis_tickangle=-45,
        height=700,
        title_x = 0.3
    )

    # Exibir no Streamlit
    st.plotly_chart(fig, use_container_width=True)

def plot_bar_vagas_orgao(df, top_n):
    # Gráfico de barras mostrando quais órgãos têm mais vagas.
    # Agrupar por órgão e somar as vagas
    vagas_por_orgao = df.groupby("Nome")["Vagas"].sum().reset_index()

    # Ordenar por número de vagas (maior para menor)
    vagas_por_orgao = vagas_por_orgao.sort_values(by="Vagas", ascending=False)

    # Filtrar os Top N órgãos com mais vagas
    vagas_por_orgao = vagas_por_orgao.head(top_n)

    # Criar o gráfico interativo
    fig = px.bar(
        vagas_por_orgao,
        y="Nome",
        x="Vagas",
        title=f"Top {top_n} Órgãos com Mais Vagas",
        text="Vagas",  # Exibir os valores nas barras
        orientation="h",  # Barras horizontais para facilitar a leitura
        color="Vagas",  # Cores diferentes por órgão
        color_continuous_scale="Greens"  # Paleta de cores
    )

    # Ajustes visuais
    fig.update_traces(
        texttemplate="%{text:.0f}",  # Exibir apenas inteiros
        textposition="outside",
        hovertemplate="<b>%{y}</b><br>Vagas: %{x:,d}"  # Formatar hover com separador de milhar
    )

    fig.update_layout(
        xaxis_title="Quantidade de Vagas",
        yaxis_title="Órgão",
        yaxis=dict(automargin=True),  
        height=600,
        title_x = 0.3
        
    )
    fig.update_yaxes(autorange="reversed")

    # Exibir no Streamlit
    st.plotly_chart(fig, use_container_width=True)

def plot_hist_aberturas(df):
    # Remover valores "Previsto" e substituir por NaN
    df["Início"] = df["Início"].replace("Previsto", None)
    df["Fim"] = df["Fim"].replace("Previsto", None)

    # Converter colunas para datetime (NaN será criado automaticamente onde não for possível converter)
    df["Início"] = pd.to_datetime(df["Início"], errors="coerce", dayfirst=True)
    df["Fim"] = pd.to_datetime(df["Fim"], errors="coerce", dayfirst=True)

    # Se ainda houver valores NaT, substituímos por datas padrão
    data_inicio = df["Início"].min()
    data_fim = df["Fim"].max()

    if pd.isna(data_inicio):
        data_inicio = datetime.today().replace(day=1)  # Definindo um valor padrão

    if pd.isna(data_fim):
        data_fim = datetime.today()  # Define a data máxima como a data atual

    # Criar um intervalo de meses entre o primeiro e o último concurso registrado
    meses = pd.date_range(start=data_inicio, end=data_fim, freq="MS")  # MS = primeiro dia do mês
    
    concursos_por_mes = []
    for mes in meses:
        abertos_no_mes = df[(df["Início"] <= mes) & (df["Fim"] >= mes)]
        
        num_max_hover = 12
        concursos_nomes = abertos_no_mes["Nome"].tolist()
        hover_text = "<br>".join(concursos_nomes[:num_max_hover])
        
        if len(concursos_nomes) > num_max_hover:
            hover_text += f"<br>... e mais {len(concursos_nomes) - num_max_hover} concursos"

        concursos_por_mes.append({
            "Mês": mes.strftime("%Y-%m"), 
            "Concursos Abertos": len(abertos_no_mes),
            "Concursos": hover_text
        })

    df_concursos_mensal = pd.DataFrame(concursos_por_mes)

    if df_concursos_mensal.empty:
        st.warning("⚠️ Nenhum dado disponível para exibir no gráfico.")
        return go.Figure()  # Retorna um gráfico vazio

    fig = px.area(
        df_concursos_mensal,
        x="Mês",
        y="Concursos Abertos",
        title="📆 Concursos com Inscrições Abertas por Mês",
        markers=True,
        line_shape="linear",
        color_discrete_sequence=["#1e7a34"]
    )

    fig.update_traces(
        hovertemplate="<b>%{x}</b><br>Concursos Abertos: %{y}<br><br><b>Concursos:</b><br>%{customdata}",
        mode="lines+markers",
        customdata=df_concursos_mensal["Concursos"]
    )

    fig.update_layout(
        xaxis=dict(
            tickmode="array",
            tickvals=df_concursos_mensal["Mês"],
            tickformat="%b %Y",
        ),
        xaxis_title="Mês",
        yaxis_title="Concursos Abertos",
        xaxis_tickangle=-45,
        height=600,
        title_x=0.3
    )

    return fig

def concursos_por_mes(df):
    """Exibe a lista de concursos do mês já filtrado."""
    st.subheader("🔎 Ver Lista Completa de Concursos")

    # Formatar datas corretamente
    df["Início"] = df["Início"].dt.strftime('%d/%m/%y').fillna("Previsto")
    df["Fim"] = df["Fim"].dt.strftime('%d/%m/%y').fillna("Previsto")

    if not df.empty:
        st.write(f"📋 **Concursos disponíveis:**")
        st.write(df[["Nome","Status", "Início", "Fim", "Vagas", "Região"]])
    else:
        st.warning("⚠️ Nenhum concurso encontrado para este mês.")

def plot_map_concursos(df):
    """
    Gera um mapa interativo mostrando a distribuição dos concursos por estado.
    """
    # Criar dicionário para converter siglas em coordenadas (lat, lon)
    estados_coordenadas = {
        "AC": (-9.0238, -70.8110), "AL": (-9.5713, -36.7819), "AP": (0.9020, -52.0030),
        "AM": (-3.4653, -62.2159), "BA": (-12.5797, -41.7007), "CE": (-5.4984, -39.3206),
        "DF": (-15.8267, -47.9218), "ES": (-19.1834, -40.3089), "GO": (-15.8270, -49.8362),
        "MA": (-4.9609, -45.2744), "MT": (-12.6819, -56.9211), "MS": (-20.7722, -54.7852),
        "MG": (-18.5122, -44.5550), "PA": (-3.4168, -52.3500), "PB": (-7.2399, -36.7819),
        "PR": (-25.2521, -52.0215), "PE": (-8.8137, -36.9541), "PI": (-7.7183, -42.7289),
        "RJ": (-22.9083, -43.1964), "RN": (-5.4026, -36.9541), "RS": (-30.0346, -51.2177),
        "RO": (-10.8306, -63.3180), "RR": (2.7376, -61.3013), "SC": (-27.2423, -50.2189),
        "SP": (-23.5505, -46.6333), "SE": (-10.5741, -37.3857), "TO": (-10.1753, -48.2982)
    }

    # Contar o número de concursos por estado
    concursos_por_estado = df["Região"].value_counts()

    # Criar um mapa centralizado no Brasil
    mapa = folium.Map(location=[-14.2350, -51.9253], zoom_start=4, tiles="cartodb positron")

    # Adicionar os marcadores no mapa
    for estado, coordenadas in estados_coordenadas.items():
        if estado in concursos_por_estado:
            quantidade = concursos_por_estado[estado]

            folium.CircleMarker(
                location=coordenadas,
                radius=5 + (quantidade * 0.3),  # Ajusta tamanho com base no número de concursos
                color="green",
                fill=True,
                fill_color="green",
                fill_opacity=0.7,
                popup=f"{estado}: {quantidade} concursos",
            ).add_to(mapa)

    # Exibir o mapa no Streamlit
    folium_static(mapa, width=600, height=500)


# Streamlit App
render_header()

df = load_data()

# Criando um layout com espaçamento lateral
espaco_esquerda, conteudo_principal, espaco_direita = st.columns([0.03, 0.94, 0.03])  # 2% espaço vazio, 98% conteúdo

with conteudo_principal:
    st.title("Dashboard de Concursos")
    
    def filtros():
        col1, col2, col3 = st.columns(3)

        # 1. Filtro de Região
        with col1:
            regioes = df['Região'].unique()
            regiao_selecionada = st.multiselect(
                "Selecione a(s) Região(ões):", 
                options=regioes
            )

        # 2. Filtro de Status
        with col2:
            status_opcoes = df['Status'].unique()   
            status_selecionado = st.multiselect(
                "Selecione o(s) Status:", 
                options=status_opcoes
            )

        # 3. Filtro de Data
        with col3:
            # Criar lista de meses disponíveis, adicionando "Todos" como opção inicial
            meses_disponiveis = sorted(df["Mês_Referência"].unique(), key=lambda x: (x != "Previsto", x))
            meses_disponiveis.insert(0, "Todos")  # Adicionar a opção "Todos" no início

            # Selecionar "Todos" por padrão
            mes_selecionado = st.selectbox("Selecione um mês:", meses_disponiveis, index=0)

        # 4. Aplicar filtros simultâneos
        df_filtrado = df.copy()

        if regiao_selecionada:
            df_filtrado = df_filtrado[df_filtrado['Região'].isin(regiao_selecionada)]

        if status_selecionado:
            df_filtrado = df_filtrado[df_filtrado['Status'].isin(status_selecionado)]

        if mes_selecionado != "Todos":
            df_filtrado = df_filtrado[df_filtrado["Mês_Referência"] == mes_selecionado]

        return df_filtrado

    df_filtrado = filtros()

    col1, col2 = st.columns(2)

    # Coluna 1
    with col1:
        # Slider e gráfico de vagas por órgão
        top_n = st.slider("Quantidade de órgãos a exibir:", 
                          min_value=5, max_value=50, 
                          value=10, step=5)
        plot_bar_vagas_orgao(df_filtrado, top_n)

    # Coluna 2
    with col2:
        plot_bar_vagas_estado(df_filtrado)

    # -------------------------------------------------------
    # EXEMPLO: OUTROS GRÁFICOS LADO A LADO
    # -------------------------------------------------------
    col3, col4 = st.columns(2)

    with col3:
        st.plotly_chart(plot_hist_aberturas(df_filtrado), 
                        use_container_width=True)

    with col4:
        plot_pie_chart(df_filtrado)

    col5, col6 = st.columns(2)

    with col5:
        concursos_por_mes(df_filtrado)

    with col6:
        st.subheader("🌎 Mapa Interativo de Concursos por Estado")
        plot_map_concursos(df_filtrado)

render_footer()