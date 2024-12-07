import requests
from bs4 import BeautifulSoup
from unidecode import unidecode
import json
from collections import defaultdict



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



# Procura por determinado conteúdo em publicações
# Use a query_string para filtrar por palavras-chave como "abertura de licitação", "contrato", etc...
def scrap_by_gazettes(territory_ids, published_since="2000-01-01", query_string="", excerpt_size=30, number_of_excerpts=1, size=2000):

    # API
    BASE_API_URL = "https://queridodiario.ok.org.br/api/"
    ENDPOINT = "gazettes"
    PARAMS = {
        "territory_ids": territory_ids,
        "published_since": published_since,
        "querystring": query_string,
        "excerpt_size": excerpt_size,
        "number_of_excertps": number_of_excerpts,
        "pre_tags": "",
        "post_tags": "",
        "size": size,
        "sort_by": "relevance"
    }

    res = requests.get(f"{BASE_API_URL}{ENDPOINT}", params=PARAMS)
    return res.json()


# Teste
if __name__ == "__main__":

    acronym = "RJ"
    query_string = "licitação"
    published_since = "2020-01-01"

    municipalities_dict = get_estate_municipalities(acronym)

    
    # Todo novo valor do dicionário será inicializado como uma lista
    txt_urls = defaultdict(list)

    # Fazendo o scraping pra cada munincípio
    for id in municipalities_dict.values():
        
        try:
            res_json = scrap_by_gazettes(id, published_since, query_string)
        except:
            continue

        print(f"Processando: {id}")
        for gazette in res_json.get("gazettes"):
            txt_urls[gazette.get("territory_id")].append(gazette.get("txt_url"))
    
    
    # Salvando tudo num arquivo json
    with open(f"data/gazettes_{acronym}.json", "w") as file:
        json.dump(dict(txt_urls), file, indent=4)