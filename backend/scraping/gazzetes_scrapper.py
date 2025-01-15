import requests

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