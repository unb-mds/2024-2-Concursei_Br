import requests
import re
import time
from bs4 import BeautifulSoup as BSP

class Run_scrappers():
    def __init__(self):
        pass
    
    def pageRequest(self, url: str):
        try:
            time.sleep(5)
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
    
        constests = {
            'concurso': [],
            'vagas': [],
            # 'remuneracao': [],
            # 'inscricao': []
        }
    
        for i in range(len(soup.select(".center"))):
            constests['concurso'].append(soup.select(".center")[i].text)
            constests['vagas'].append(soup.select("td > a")[i].text) 

        return constests
    
    # def get_info_json(self, soup: BSP):

    #     for indice in range(1,7):
    #         print(soup.find_all(f'h{indice}'))
        
        #Bloco de peqsuisa usando a regex passada dentro dos requests
        #regex = re.compile(r'\b(\d+\s+cargos|cargos\s+\d+)\b|\b(\d+\s+vagas|vagas\s+\d+)\b', re.IGNORECASE)
        # # Buscar todas as tags
        # tags = soup.find_all()

        # # Aplicar a regex diretamente no texto das tags e capturar as correspondências
        # resultados = []
        # for tag in tags:
        #     if tag.string:  # Verifica se a tag possui conteúdo de texto
        #         matches = regex.findall(tag.string)
        #         resultados.extend(matches)

        # for resultado in resultados:
        #     print(resultado)
 
if __name__ == "__main__":
    scrap = Run_scrappers()
    soup = scrap.initWebScraper('https://concursosnobrasil.com/concursos/df')
    scrap.get_contests_links(soup)
    # for contest in scrap.get_contests_links(soup):
    #     scrap.get_info_json(scrap.initWebScraper(f'{contest}'))