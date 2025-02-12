# tests/test_scrapper.py

import pytest
from scrapper import Scrapper  # import da sua classe

def test_scrapper_instantiation():
    scrapper = Scrapper()
    assert scrapper is not None


def test_format_data():
    scrapper = Scrapper()
    formatted = scrapper._Scrapper__format_data("1", "janeiro", "2023")
    assert formatted == "01/01/2023"

    # Teste com outra data
    formatted = scrapper._Scrapper__format_data("10", "dezembro", "2025")
    assert formatted == "10/12/2025"


def test_get_registrations_data():
    scrapper = Scrapper()

    # Exemplo de parágrafo válido
    paragraph_valid = (
        "As inscrições para o concurso estarão abertas do dia 15 de janeiro de 2023 "
        "até o dia 30 de janeiro de 2023, conforme edital."
    )

    initial_date, final_date = scrapper._Scrapper__get_registrations_data(paragraph_valid)
    assert initial_date == "15/01/2023"
    assert final_date == "30/01/2023"

    # Exemplo de parágrafo sem mês
    paragraph_no_month = "As inscrições começam dia 10 até dia 20, conforme edital."
    initial_date, final_date = scrapper._Scrapper__get_registrations_data(paragraph_no_month)
    assert initial_date == "Indisponível"
    assert final_date == "Indisponível"

    # Exemplo de parágrafo sem datas
    paragraph_no_dates = "Conforme o edital, está publicado no Diário Oficial."
    initial_date, final_date = scrapper._Scrapper__get_registrations_data(paragraph_no_dates)
    assert initial_date == "Indisponível"
    assert final_date == "Indisponível"


