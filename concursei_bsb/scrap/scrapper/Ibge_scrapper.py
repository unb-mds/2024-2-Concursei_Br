import requests
from bs4 import BeautifulSoup
from unidecode import unidecode

class Ibge_scrapper():
    def __init__(self):
        # Site do IBGE com o código dos munincípios
        self.__IBGE_URL = "https://www.ibge.gov.br/explica/codigos-dos-municipios.php"
        self.__municipalities = {}

    def get_estate_municipalities(self, acronym : str):
        response = requests.get(self.__IBGE_URL)
        if response.status_code != 200:
            print(f"Erro ao acessar a página. Status code: {response.status_code}")
            return None
        
        soup = BeautifulSoup(response.text, 'html.parser')
        thead = soup.find("thead", id=acronym)
        tbody = thead.find_next_sibling("tbody")

        # Iterando todos os munincípios listados (linhas)
        for row in tbody.find_all("tr"):  
            columns = row.find_all("td")
            name = unidecode(columns[0].a.text)
            id = columns[1].text
            self.__municipalities[name] = id

        return self.__municipalities