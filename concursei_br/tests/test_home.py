import pytest
from unittest.mock import patch, MagicMock
import pandas as pd
from io import StringIO
from app.Home import load_data, get_custom_css, get_header, get_main_section, get_statistics, get_footer, main

@pytest.fixture
def mock_csv_data():
    data = """
    Nome;Status;Vagas
    Concurso 1;Aberto;10
    Concurso 2;Previsto;Várias
    Concurso 3;Aberto;5
    """
    return StringIO(data)


@patch('requests.get')
def test_load_data(mock_get, mock_csv_data):

    mock_response = MagicMock()
    mock_response.text = mock_csv_data.getvalue()
    mock_get.return_value = mock_response

    df = load_data()

    assert not df.empty
    assert len(df) == 3
    assert df['Vagas'].sum() == 15


def test_get_statistics(mock_csv_data):
    df = pd.read_csv(mock_csv_data, sep=';')
    df["Vagas"] = pd.to_numeric(df["Vagas"], errors="coerce").fillna(0).astype(int)
    
    stats = get_statistics(df)
    
    assert "3" in stats
    assert "15" in stats


def test_get_custom_css():
    css = get_custom_css()
    assert '<style>' in css

def test_get_header():
    header = get_header()
    assert '<div class="header">' in header

def test_get_main_section():
    main_section = get_main_section()
    assert '<div class="main-section">' in main_section

def test_get_footer():
    footer = get_footer()
    assert '© 2025 Concursei Br. Todos os direitos reservados.' in footer
