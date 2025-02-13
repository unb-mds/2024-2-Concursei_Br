import pytest
import pandas as pd
import calendar
from datetime import datetime
from app.Home import load_data
from io import StringIO
from unittest.mock import patch

data = """Nome;Início;Fim;Região;Vagas
Concurso A;01/02/2025;15/02/2025;BH;10
Concurso B;05/02/2025;20/02/2025;SP;5
"""

@pytest.fixture
def mock_csv_data():
    return StringIO(data)


def test_date_conversion(mock_csv_data):
    df = pd.read_csv(mock_csv_data, sep=';')
    df["Início"] = pd.to_datetime(df["Início"], dayfirst=True, errors="coerce")
    df["Fim"] = pd.to_datetime(df["Fim"], dayfirst=True, errors="coerce")
    
    assert df["Início"].dtype == 'datetime64[ns]'
    assert df["Fim"].dtype == 'datetime64[ns]'
    assert df["Início"].iloc[0] == datetime(2025, 2, 1)
    assert df["Fim"].iloc[1] == datetime(2025, 2, 20)


def test_available_years(mock_csv_data):
    df = pd.read_csv(mock_csv_data, sep=';')
    df["Início"] = pd.to_datetime(df["Início"], dayfirst=True, errors="coerce")
    df["Fim"] = pd.to_datetime(df["Fim"], dayfirst=True, errors="coerce")
    
    available_years = sorted(set(df["Início"].dt.year.dropna().tolist() + df["Fim"].dt.year.dropna().tolist()))
    available_years = [year for year in available_years if year >= 2000]
    
    assert available_years == [2025]


def test_available_regions(mock_csv_data):
    df = pd.read_csv(mock_csv_data, sep=';')
    available_regions = sorted(df["Região"].dropna().unique().tolist())
    available_regions.insert(0, "Todos")
    
    assert available_regions == ["Todos", "BH", "SP"]


def test_create_calendar(mock_csv_data):
    df = pd.read_csv(mock_csv_data, sep=';')
    df["Início"] = pd.to_datetime(df["Início"], dayfirst=True, errors="coerce")
    df["Fim"] = pd.to_datetime(df["Fim"], dayfirst=True, errors="coerce")
    
    year, month, region = 2025, 2, "BH"
    cal = calendar.monthcalendar(year, month)
    
    if region == "Todos":
        filtered_df = df
    else:    
        filtered_df = df[df["Região"] == region]
    
    assert isinstance(cal, list)
    assert len(cal) > 0
    assert not filtered_df.empty
    assert filtered_df.iloc[0]["Nome"] == "Concurso A"