import unittest
import pandas as pd
import streamlit as st
from io import StringIO
from app.pages.Dashboards import load_data, plot_pie_chart, plot_bar_vagas_estado, plot_bar_vagas_orgao, plot_hist_aberturas

class TestStreamlitApp(unittest.TestCase):
    def setUp(self):
        self.csv_data = """Nome;Status;Início;Fim;Vagas;Região
        Concurso A;Aberto;01/02/2024;10/02/2024;100;SP
        Concurso B;Previsto;15/02/2024;25/02/2024;50;RJ
        Concurso C;Aberto;05/03/2024;15/03/2024;200;MG"""

        self.df = pd.read_csv(StringIO(self.csv_data), sep=';')
        self.df["Início"] = pd.to_datetime(self.df["Início"], errors="coerce", dayfirst=True)
        self.df["Fim"] = pd.to_datetime(self.df["Fim"], errors="coerce", dayfirst=True)
        self.df["Vagas"] = pd.to_numeric(self.df["Vagas"], errors="coerce", downcast="integer")
    
    def test_load_data(self):
        df = load_data()
        self.assertIsInstance(df, pd.DataFrame)
        self.assertIn("Status", df.columns)
    
    def test_plot_pie_chart(self):
        try:
            plot_pie_chart(self.df)
        except Exception as e:
            self.fail(f"plot_pie_chart falhou com erro: {e}")
    
    def test_plot_bar_vagas_estado(self):
        try:
            plot_bar_vagas_estado(self.df)
        except Exception as e:
            self.fail(f"plot_bar_vagas_estado falhou com erro: {e}")
    
    def test_plot_bar_vagas_orgao(self):
        try:
            plot_bar_vagas_orgao(self.df, top_n=5)
        except Exception as e:
            self.fail(f"plot_bar_vagas_orgao falhou com erro: {e}")
    
    def test_plot_hist_aberturas(self):
        try:
            plot_hist_aberturas(self.df)
        except Exception as e:
            self.fail(f"plot_hist_aberturas falhou com erro: {e}")

if __name__ == "__main__":
    unittest.main()
