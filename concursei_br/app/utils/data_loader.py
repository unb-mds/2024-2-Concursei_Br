import pandas as pd
import streamlit as st
from pathlib import Path

@st.cache_data
def load_contests_data():
    """Carrega os dados de concursos do CSV com tratamento de erros."""
    try:
        # Caminho absoluto considerando a estrutura de pastas
        base_dir = Path(__file__).resolve().parent.parent.parent  # Sobe dois níveis a partir do arquivo atual
        csv_path = base_dir / "data" / "contests_info.csv"
        
        # Carrega dados com verificação de encoding
        df = pd.read_csv(csv_path, sep=";", encoding='utf-8')
        
        # Verificação básica de dados
        if df.empty:
            st.error("O arquivo CSV está vazio!")
            return pd.DataFrame()
            
        return df
        
    except FileNotFoundError:
        st.error(f"Arquivo não encontrado em: {csv_path}")
        return pd.DataFrame()
    except Exception as e:
        st.error(f"Erro ao carregar dados: {str(e)}")
        return pd.DataFrame()
    
if __name__ == "__main__":
    test_df = load_contests_data()
    if not test_df.empty:
        print("Dados carregados com sucesso!")
        print(test_df.head())
    else:
        print("Falha no carregamento dos dados")