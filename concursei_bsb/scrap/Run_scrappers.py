from Gazzetes_scrapper import scrap_by_gazettes
from Ibge_scrapper import get_estate_municipalities

import json
from collections import defaultdict

if __name__ == "__main__":

    acronym = "DF"
    query_strings = ["concurso", "concurso público", "edital", "inscrição", "provas"]
    published_since = "2020-01-01"

    municipalities_dict = get_estate_municipalities(acronym)

    
    # Todo novo valor do dicionário será inicializado como uma lista
    txt_urls = defaultdict(list)

    # Fazendo o scraping pra cada munincípio
    for q_string in query_strings:
        for id in municipalities_dict.values():
            
            try:
                res_json = scrap_by_gazettes(id, published_since, q_string)
            except:
                continue

            print(f"Processando: {id}")
            for gazette in res_json.get("gazettes"):
                txt_urls[gazette.get("territory_id")].append(gazette.get("txt_url"))
        
    
    # Salvando tudo num arquivo json
    with open(f"../../database/gazettes_{acronym}.json", "w") as file:
        json.dump(dict(txt_urls), file, indent=4)