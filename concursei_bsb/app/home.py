import streamlit as st

def set_page_config():
    st.set_page_config(
        page_title="Concursei Br",
        layout="wide",
        page_icon="assets/logo_concursei.png"
    )

def get_css():
    """Retorna o CSS para estilização da página."""
    return """
    <style>
        body {
            width: 100%;
            font-family: Arial, sans-serif;
            background-color: #f9f9f9;
            margin: 0;
            padding: 0;
        }
        .header {
            background-color: #32a852;
            padding: 20px 50px;
            border-bottom: 3px solid #1e7a34;
            display: flex;
            justify-content: space-between;
            align-items: center;
            position: sticky;
            top: 50px;
            text-wrap: nowrap;
        }
        .header .logo {
            margin-left: 5%;
            font-size: 24px;
            font-weight: bold;
            color: #ffffff;
        }
        .header a {
            text-decoration: none;
            color: #32a852;
            font-weight: bold;
            margin-left: 20px;
        }
        .relatorios {
            color: #ffffff;
            background-color: green;
            margin-left: 30px;
            padding: 10px 25px;
            border-radius: 8%;
        }
        .main-section {
            width: 100%;
            background-color: #dcdcdc;
            text-align: left;
            padding: 50px 20px;
        }
        .main-section h1 {
            margin-left: 7%;
            font-size: 36px;
            color: #333333;
        }
        .main-section p {
            font-size: 18px;
            color: #666666;
            margin: 20px 0 20px 7%;
        }
        .main-section .btn {
            display: inline-block;
            background-color: #32a852;
            color: white;
            padding: 10px 20px;
            border-radius: 5px;
            text-decoration: none;
            font-size: 16px;
            margin: 10px 10px 10px 7%;
        }
        .statistics {
            text-align: center;
            margin: 50px 0;
        }
        .statistics .circle {
            display: inline-block;
            width: 150px;
            height: 150px;
            line-height: 150px;
            border-radius: 50%;
            background-color: #32a852;
            color: white;
            font-size: 48px;
            font-weight: bold;
            margin-top: 20px;
            margin-bottom: 30px;
        }
        .footer {
            background-color: #ffffff;
            padding: 20px;
            border-top: 2px solid #eaeaea;
            text-align: center;
            font-size: 14px;
            color: #666666;
        }
    </style>
    """

def render_html():
    """Renderiza a estrutura HTML da página."""
    template = """
    <div class="header">
        <div class="logo">  
            Concursei Br
        </div>
        <div>
            <a href="#">Início</a>
            <a href="#"><span class="relatorios">Relatórios</span></a>
        </div>
    </div>

    <div class="main-section">
        <h1>Acompanhe as <br>publicações no <br> <div style="color:green">Concursei Br</div></h1>
        <p>Promovendo a participação pública em concursos do Brasil: acompanhe de forma simples e clara <br> as publicações de concursos.</p>
        <a href="#" class="btn">Ver Relatórios</a>
    </div>

    <div class="statistics">
        <h2>Publicações Concursos</h2>
        <div class="circle">39</div>
        <p>Quantidade de publicações no Concursos Brasil hoje</p>
    </div>

    <div class="footer">
        © 2025 Concursei Br. Todos os direitos reservados.
    </div>
    """
    return template

def main():
    """Função principal para rodar o Streamlit."""
    set_page_config()
    st.markdown(get_css(), unsafe_allow_html=True)
    st.markdown(render_html(), unsafe_allow_html=True)



if __name__ == "__main__":
    main()