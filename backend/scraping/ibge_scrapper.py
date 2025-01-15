import requests
from bs4 import BeautifulSoup
from unidecode import unidecode

# Use as siglas dos estados quando quiser recuperar os munincípios de 
# determinado estado:
#
#    "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", 
#    "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", 
#    "RR", "SC", "SP", "SE", "TO"
#

def get_estate_municipalities(acronym : str):

    # Site do IBGE com o código dos munincípios
    IBGE_URL = "https://www.ibge.gov.br/explica/codigos-dos-municipios.php"
    response = requests.get(IBGE_URL)

    if response.status_code != 200:
        print(f"Erro ao acessar a página. Status code: {response.status_code}")
        return None


    soup = BeautifulSoup(response.text, 'html.parser')
    thead = soup.find("thead", id=acronym)
    tbody = thead.find_next_sibling("tbody")

    municipalities = {}

    # Iterando todos os munincípios listados (linhas)
    for row in tbody.find_all("tr"):  
        columns = row.find_all("td")

        # Recuperando o nome do munincícpio e o ID
        name = unidecode(columns[0].a.text) # Substitui acentos, cedilha, etc...
        id = columns[1].text
        municipalities[name] = id

    return municipalities