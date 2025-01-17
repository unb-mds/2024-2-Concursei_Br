import requests

# Procura por determinado conteúdo em publicações
# Use a query_string para filtrar por palavras-chave como "abertura de licitação", "contrato", etc...

class Gazzetes_scrapper():
    def __init__(self):
        self.__excerpt_size=30, 
        self.__number_of_excerpts=1, 
        self.__size=2000
    
    def scrap_by_gazettes(self, territory_ids, published_since, query_string):
        # API
        BASE_API_URL = "https://queridodiario.ok.org.br/api/"
        ENDPOINT = "gazettes"
        PARAMS = {
            "territory_ids": territory_ids,
            "published_since": published_since,
            "querystring": query_string,
            "excerpt_size": self.__excerpt_size,
            "number_of_excertps": self.__number_of_excerpts,
            "pre_tags": "",
            "post_tags": "",
            "size": self.__size,
            "sort_by": "relevance"
        }
        
        res = requests.get(f"{BASE_API_URL}{ENDPOINT}", params=PARAMS)
        return res.json()