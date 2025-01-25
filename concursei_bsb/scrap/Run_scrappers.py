import requests
import re
import time
from bs4 import BeautifulSoup as BSP

class Run_scrappers():
    def __init__(self):
        pass
    
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


    def feed_dict(self, contests_dict: dict, contest_name: str, *args):
        
        # Inicializando o item no dicionário caso ele não exista
        if contest_name not in contests_dict:
            contests_dict[contest_name] = []
        
        for value in args:
            contests_dict[contest_name].append(value)


    def translate_forecast(self, forecast: object|None):

        if forecast != None:
            return "Previsto"
        
        return "Aberto"


    def get_main_page_info(self, contests_dict: dict, soup: BSP):
        
        info = soup.select('tr:not(:first-child)')

        for index, tr in enumerate(info):
            
            name = tr.find("a").text.strip()
            vacancies = tr.find("td", class_="center").text.strip()
            link = tr.find("a")['href']
            forecast = self.translate_forecast(tr.find("div", class_='label-previsto'))

            self.feed_dict(contests_dict, name, vacancies, forecast, link)


    def get_extreme_months(self, months_to_compare: list):

        months_list = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 
                       'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
        
        smaller_month = months_list[-1]
        bigger_month = months_list[0]

        for month in months_to_compare:
            if months_list.index(month) > months_list.index(bigger_month):
                bigger_month = month

            if months_list.index(month) < months_list.index(smaller_month):
                smaller_month = month

        return smaller_month, bigger_month

    
    def get_registrations_data(self, paragraph: str):

        key_words = ("inscrições", "inscrição", "participação", "candidatar", "data")
        months_order = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')

        # Verifica se no parágrafo é citado algum mês e as palavras-chave
        has_key_word = any(key_word in paragraph for key_word in key_words)
        has_month = any(month in paragraph for month in months_order)
        has_digit = any(char.isdigit() for char in paragraph)

        if not (has_key_word and has_month and has_digit):
            return None, None
        
        try:
            days = re.findall(r" [0-9]{1,2} ", paragraph)
            starting_day = days[0]
            finishing_day = days[-1]

            months = re.findall("(" + "|".join(months_order) + ")", paragraph)
            starting_month = months[0]
            finishing_month = months[-1]

            years = re.findall(r" [0-9]{4}", paragraph)
            starting_year = years[0]
            finishing_year = years[-1]
        except:
            return None, None
        
        # Formantando no formato de data
        starting_data = f"{starting_day}/{starting_month}/{starting_year}".replace(" ", "")
        finishing_data = f"{finishing_day}/{finishing_month}/{finishing_year}".replace(" ", "")

        return starting_data, finishing_data


    def get_especific_page_info(self, contests_dict: dict, contest_name: str, soup: BSP):

        paragraphs = soup.select("p:not(.related-post-grid)")
        
        # Inscrições
        if contests_dict[contest_name][1] == 'Previsto':
            self.feed_dict(contests_dict, contest_name, None, None)
            return
        
        for paragraph in paragraphs:
            paragraph = paragraph.text.lower()
            starting_data, finishing_data = self.get_registrations_data(paragraph)
            
            if starting_data and finishing_data:
                break
            
        self.feed_dict(contests_dict, contest_name, starting_data, finishing_data)


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

    contests = {}
    scrap.get_main_page_info(contests, soup)
    
    for key, values in contests.items():

        name = key
        link = values[-1]
        soup = scrap.initWebScraper(link)
        scrap.get_especific_page_info(contests, key, soup)


        print(key, values)