from concursei_bsb.scrap.scrapper.gazettes_scrapper import Gazzetes_scrapper
from Ibge_scrapper import Ibge_scrapper

import json
from collections import defaultdict

class Run_scrappers():
    def __init__(self):
        self.__acronym = "DF"
        self.__query_strings = ["concurso"]
        self.__published_since = "2024-01-01"
    
    def initialize(self):
        API = Gazzetes_scrapper()
        ID = Ibge_scrapper()
        municipalities_dict = ID.get_estate_municipalities(self.__acronym)

        # Todo novo valor do dicionário será inicializado como uma lista
        txt_urls = defaultdict(list)

        # Fazendo o scraping pra cada munincípio
        for q_string in self.__query_strings:
            for id in municipalities_dict.values():
                try:
                    res_json = API.scrap_by_gazettes(id, self.__published_since, q_string)
                except:
                    continue
                print(f"Processando: {id}")
                for gazette in res_json.get("gazettes"):
                    txt_urls[gazette.get("territory_id")].append(gazette.get("txt_url"))

        # Salvando tudo num arquivo json
        with open(f"../../data/gazettes_{self.__acronym}.json", "w") as file:
            json.dump(dict(txt_urls), file, indent=4)

#Temporário para teste
if __name__ == '__main__':
    teste = Run_scrappers()
    teste.initialize()
