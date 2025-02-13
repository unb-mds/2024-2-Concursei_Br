import pytest
import pandas as pd
import streamlit as st
from unittest.mock import MagicMock, patch
from io import StringIO
from app.Home import load_data
from app.Exportar import filtros, criar_visualizacoes

data_csv = """Nome;Região;Status;Vagas;Início;Fim
Concurso 1;Sudeste;Aberto;10;01/01/2025;10/02/2025
Concurso 2;Sul;Fechado;5;05/01/2025;15/02/2025
Concurso 3;Nordeste;Aberto;20;10/01/2025;20/02/2025
"""

@pytest.fixture
def mock_csv_data():
    return StringIO(data_csv)

@pytest.fixture
def mock_df(mock_csv_data):
    df = pd.read_csv(mock_csv_data, sep=';')
    df["Vagas"] = pd.to_numeric(df["Vagas"], errors="coerce").fillna(0).astype(int)
    return df

@patch("Home.load_data")
def test_filtros(mock_load_data, mock_df):
    mock_load_data.return_value = mock_df
    st.experimental_rerun = MagicMock()
    
    with patch("streamlit.multiselect", side_effect=[["Sudeste"], ["Aberto"]]):
        df_filtrado = filtros()
    
    assert not df_filtrado.empty
    assert len(df_filtrado) == 1
    assert df_filtrado.iloc[0]['Nome'] == "Concurso 1"
    assert df_filtrado.iloc[0]['Vagas'] == 10

@patch("streamlit.metric")
@patch("streamlit.table")
def test_criar_visualizacoes(mock_table, mock_metric, mock_df):
    criar_visualizacoes(mock_df)
    
    mock_metric.assert_any_call(label="Concursos Filtrados", value=3)
    mock_metric.assert_any_call(label="Total de Vagas", value=35)
    mock_table.assert_called_once()
