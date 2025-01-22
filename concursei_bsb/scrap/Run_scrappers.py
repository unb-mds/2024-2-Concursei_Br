import requests
import re
from bs4 import BeautifulSoup as BSP

class Run_scrappers():
    def __init__(self):
        pass
    
    def pageRequest(self, url: str):
        try:
            return requests.get(url)
        except requests.HTTPError:
            print("An http error has ocurred, process has exited")
            return None
        except:
            print("An error has ocurred, process has exited")
            return None

    def initWebScraper(self, url: str, parser: str = 'html.parser'):
        webResponse = self.pageRequest(url)
    
        if(webResponse == None):
            print("Canceling scrapping")
            return None
    
        return BSP(webResponse.text, parser)

    def get_contests_links(self, soup : BSP):
    
        constests = []
    
        links = soup.select("td > a")
        
        for link in links:
            constests.append(link['href'])
    
        return constests
    
    def get_info_json(self, soup: BSP):

        for indice in range(1,7):
            print(soup.find_all(f'h{indice}'))
 
if __name__ == "__main__":
    scrap = Run_scrappers()
    soup = scrap.initWebScraper('https://concursosnobrasil.com/concursos/df')
    for contest in scrap.get_contests_links(soup):
        scrap.get_info_json(scrap.initWebScraper(f'{contest}'))