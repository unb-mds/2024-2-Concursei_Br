import pytest
import numpy as np
import sys
import os
import requests_mock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scrap.scrapper import Scrapper

@pytest.fixture
def scrapper():
    return Scrapper()


def test_scrapper_instantiation(scrapper):
    assert scrapper is not None


def test_init_web_scrapper(scrapper):
    url = "https://concursosnobrasil.com/concursos/DF"

    web_response = self.__page_request(url)
    return BeautifulSoup(web_response.content, parser)


def test_format_data(scrapper):
    formatted = scrapper._Scrapper__format_data("1", "janeiro", "2023")
    assert formatted == "01/01/2023"

    formatted = scrapper._Scrapper__format_data("10", "dezembro", "2025")
    assert formatted == "10/12/2025"


def test_get_registrations_data(scrapper):

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


def test_verify_key_words(scrapper):
    # Teste com parágrafo que contém as palavras-chave e meses
    paragraph_valid = "As inscrições começam dia 18 de janeiro e vão até 14 de fevereiro, conforme edital."
    assert scrapper._Scrapper__verify_key_words(paragraph_valid)

    # Teste com parágrafo sem as palavras-chave
    paragraph_no_keywords = "O concurso será realizado em janeiro de 2023."
    assert not scrapper._Scrapper__verify_key_words(paragraph_no_keywords)

    # Teste com parágrafo sem meses e palavras-chave
    paragraph_invalid = "As inscrições começam no dia 15."
    assert not scrapper._Scrapper__verify_key_words(paragraph_invalid)


def test_translate_forecast(scrapper):
    # Teste com forecast válido
    assert scrapper._Scrapper__translate_forecast(True) == "Previsto"

    # Teste com forecast None
    assert scrapper._Scrapper__translate_forecast(None) == "Aberto"


def test_get_especific_page_info(scrapper, requests_mock):
    url = "https://www.exemplo.com.br"
    
    # Mocking the response to simulate the page content
    requests_mock.get(url, text="""
        <html>
            <body>
                <p>Inscrições de 10 de janeiro de 2023 até 20 de fevereiro de 2023.</p>
            </body>
        </html>
    """)
    
    # Chamar o método para pegar as informações de inscrição
    initial_date, final_date = scrapper._Scrapper__get_especific_page_info(url)
    
    # Verificar se as datas foram extraídas corretamente
    assert initial_date == "10/01/2023"
    assert final_date == "20/02/2023"


def test_feed_dict(scrapper):
    contests_array = np.empty((0, 6), dtype=object)
    contests_array = scrapper._Scrapper__feed_dict(contests_array, 'SP', 'Concurso 1', '10', 'Aberto', '01/01/2023', '31/01/2023')
    
    # Verificar se a linha foi adicionada corretamente
    assert contests_array.shape[0] == 1
    assert contests_array[0, 1] == 'Concurso 1'
    assert contests_array[0, 5] == '31/01/2023'


def test_parse_to_csv(scrapper, tmpdir):
    contests_array = np.array([
        ['SP', 'Concurso 1', '10', 'Aberto', '01/01/2023', '31/01/2023']
    ], dtype=object)
    
    # Modificar o caminho do arquivo CSV para usar um diretório temporário
    scrapper._Scrapper__csv_path = tmpdir.join("contests_info.csv")
    
    # Chamar o método para salvar os dados no CSV
    scrapper._Scrapper__parse_to_csv(contests_array)
    
    # Verificar se o arquivo foi criado e contém os dados
    assert scrapper._Scrapper__csv_path.exists()
    with open(scrapper._Scrapper__csv_path, 'r') as f:
        content = f.read()
        assert 'Concurso 1' in content
        assert '10' in content


def test_remove_duplicated_contests(scrapper, tmpdir):
    # Criar um arquivo CSV de exemplo com dados duplicados
    contests_array = np.array([
        ['SP', 'Concurso 1', '10', 'Aberto', '01/01/2023', '31/01/2023'],
        ['SP', 'Concurso 1', '10', 'Aberto', '01/01/2023', '31/01/2023'],  # Duplicado
        ['RJ', 'Concurso 2', '5', 'Aberto', '10/02/2023', '20/02/2023']
    ], dtype=object)
    
    scrapper._Scrapper__csv_path = tmpdir.join("contests_info.csv")
    scrapper._Scrapper__parse_to_csv(contests_array)
    
    # Chamar o método para remover duplicatas
    scrapper._Scrapper__remove_duplicated_contests()
    
    # Verificar se as duplicatas foram removidas
    with open(scrapper._Scrapper__csv_path, 'r') as f:
        content = f.read()
        assert content.count('Concurso 1') == 1  # Deve haver apenas uma ocorrência de "Concurso 1"


def test_page_request(scrapper, requests_mock):
    url = "https://www.exemplo.com.br"
    
    # Mocking the response to simulate the page content
    requests_mock.get(url, text="Conteúdo da página de exemplo.")
    
    # Verificar se o conteúdo da página foi retornado corretamente
    response = scrapper._Scrapper__page_request(url)
    assert response is not None
    assert "Conteúdo da página de exemplo." in response.text


def test_init_web_scrapper(scrapper, requests_mock):
    url = "https://www.exemplo.com.br"
    
    # Mocking the response to simulate the page content
    requests_mock.get(url, text="<html><body>Exemplo de conteúdo</body></html>")
    
    # Verificar se o BeautifulSoup foi inicializado corretamente
    soup = scrapper._Scrapper__init_web_scrapper(url)
    assert soup is not None
    assert "<body>Exemplo de conteúdo</body>" in str(soup)


def test_run_scrapper(scrapper, requests_mock):
    url = "https://concursosnobrasil.com/concursos/SP"
    
    # Mocking the response to simulate the page content
    requests_mock.get(url, text="<html><body><tr><td><a href='/concurso1'>Concurso 1</a></td></tr></body></html>")
    
    # Checar se o concurso foi adicionado corretamente ao array
    contests_array = np.empty((0, 6), dtype=object)
    soup = scrapper._Scrapper__init_web_scrapper(url)
                             
    contests_array = scrapper._Scrapper__get_contests_entire_info('SP', contests_array, scrapper._Scrapper__init_web_scrapper(url))
    assert contests_array.shape[0] == 1
    assert contests_array[0, 1] == "Concurso 1"