import requests
import re
import time
from bs4 import BeautifulSoup as BSP

class Run_scrappers():
    def __init__(self):

        self.__constests = {
            'concursos': [],
            'vagas': [],
            'links': []
            # 'remuneracao': [],
            # 'inscricao': []
        }
    
    def pageRequest(self, url: str):
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
            time.sleep(5)
            return requests.get(url, headers=headers)
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


    def get_links(self, soup : BSP):

        links = []

        constest_names = soup.select(".center")
        vagas = soup.select("td > a")

        for i in range(len(soup.select(".center"))):
            self.__constests['concursos'].append(constest_names[i])
            self.__constests['vagas'].append(vagas[i].text) 
            links.append(vagas[i]['href'])

        return links
    
    def search_web_info(self, links_array : list):
        
        for link in links_array:
            soup = self.initWebScraper(link)

            # Tratamento aqui
            print(soup)



    #     for indice in range(1,7):
    #         print(soup.find_all(f'h{indice}'))
        
    #     Bloco de peqsuisa usando a regex passada dentro dos requests
    #     regex = re.compile(r'\b(\d+\s+cargos|cargos\s+\d+)\b|\b(\d+\s+vagas|vagas\s+\d+)\b', re.IGNORECASE)
    #     # Buscar todas as tags
    #     tags = soup.find_all()

    #     # Aplicar a regex diretamente no texto das tags e capturar as correspondências
    #     resultados = []
    #     for tag in tags:
    #         if tag.string:  # Verifica se a tag possui conteúdo de texto
    #             matches = regex.findall(tag.string)
    #             resultados.extend(matches)

    #     for resultado in resultados:
    #         print(resultado)
 
if __name__ == "__main__":
    scrap = Run_scrappers()
    soup = scrap.initWebScraper('https://concursosnobrasil.com/concursos/df')
    links = scrap.get_links(soup)
    scrap.search_web_info(links)

        