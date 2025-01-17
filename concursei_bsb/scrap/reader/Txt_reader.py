import os
import requests

class Txt_reader():
    def __init__(self):
        self.__GAZZETE_PATHS = "../../data/gazettes_DF.json"
        # assert os.path.exists(GAZZETE_PATHS), "File not Found!"
    
    def get_GAZZETE_PATHS(self):
        return self.__GAZZETE_PATHS

    def request_gazzete_url(self, gazette_links : dict, key_index: int, gazzete_index: int):
        id_key = list(gazette_links.keys())[key_index]
        link = gazette_links[id_key][gazzete_index]

        res = requests.get(link)

        if res.status_code != 200:
            return
        
        return res.text