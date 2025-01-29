import requests
import re
import time
from bs4 import BeautifulSoup
import pandas as pd

class Run_scrappers():
    def __init__(self):

        self.months_map = {
            'janeiro': '01', 'fevereiro': '02', 'março': '03', 'abril': '04',
            'maio': '05', 'junho': '06', 'julho': '07', 'agosto': '08',
            'setembro': '09', 'outubro': '10', 'novembro': '11', 'dezembro': '12'
        }
    
    def page_request(self, url: str):

        """Essa função é dedicada a fazer a requisição HTTP para a url especificada."""

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


    def init_web_scrapper(self, url: str, parser: str = 'html.parser'):

        """Essa função retorna um objeto BeautifulSoup, para que assim seja
        possível manipular o texto de alguma página e realizar o scraping."""

        webResponse = self.page_request(url)
    
        if(webResponse == None):
            print("Canceling scrapping")
            return None
    
        return BeautifulSoup(webResponse.text, parser)


    def feed_dict(self, contests_dict: dict, contest_name: str = "", vacancies: str = "",
                  forecast: str = "", url: str = "", register_initial_data: str = "",
                  register_final_data: str = ""):
        
        """Essa função alimenta o dicionário que armazena os dados dos concursos."""
        
        # Inicializando o item no dicionário caso ele não exista
        if len(contests_dict) == 0:
            contests_dict['name'] = []
            contests_dict['vacancies'] = []
            contests_dict['forecast'] = []
            contests_dict['url'] = []
            contests_dict['register_initial_data'] = []
            contests_dict['register_final_data'] = []

        # Adição dos valores no dicionário
        if contest_name:
            contests_dict['name'].append(contest_name)

        if vacancies:
            contests_dict['vacancies'].append(vacancies)

        if forecast:
            contests_dict['forecast'].append(forecast)

        if url:
            contests_dict['url'].append(url)
        
        if register_initial_data:
            contests_dict['register_initial_data'].append(register_initial_data)
        
        if register_final_data:
            contests_dict['register_final_data'].append(register_final_data)


    def translate_forecast(self, forecast: object|None):

        if forecast != None:
            return "Previsto"
        
        return "Aberto"


    def get_contests_entire_info(self, contests_dict: dict, soup):

        """Essa é a função principal para o scraping de algum concurso.
        Ele faz o scraping na página geral onde são exibidos os concursos, e chama uma
        outra função para acessar a página específica do concurso, para também realizar
        o scraping."""
        
        info = soup.select('tr:not(:first-child)')

        for index, tr in enumerate(info):
            
            name = tr.find("a").text.strip()
            vacancies = tr.find("td", class_="center").text.strip()
            forecast = self.translate_forecast(tr.find("div", class_='label-previsto'))
            url = tr.find("a")['href']

            register_intial_data, register_final_data = scrap.get_especific_page_info(url)

            self.feed_dict(contests_dict, name, vacancies, forecast, url,
                           register_intial_data, register_final_data)


    def format_data(self, day: str, month: str, year: str):

        """Essa função formata a data do formato d/mês_por_extenso/yyy para
        dd/mm/yyyy."""

        day = day.zfill(2)
        month = self.months_map[month]
        year = "20" + year if len(year) == 2 else year

        return f"{day}/{month}/{year}".replace(" ", "")
        

    def get_extreme_months(self, months_to_compare: list):

        """Essa função identifica qual é o 'menor' mês, e qual o 'maior' mês.
        Por exemplo, janeiro é menor que dezembro."""
        
        months_list = list(self.months_map.keys())
        smaller_month = months_list[-1]
        bigger_month = months_list[0]

        for month in months_to_compare:
            if months_list.index(month) > months_list.index(bigger_month):
                bigger_month = month

            if months_list.index(month) < months_list.index(smaller_month):
                smaller_month = month

        return smaller_month, bigger_month

    
    def get_registrations_data(self, paragraph: str):

        """A função busca a data de início e a data final de inscrição para o concurso."""

        key_words = ("inscrições", "inscrição", "participação", "candidatar", "data")

        # Verifica se no parágrafo é citado algum mês e as palavras-chave
        has_key_word = any(key_word in paragraph for key_word in key_words)
        has_month = any(month in paragraph for month in self.months_map)
        has_digit = any(char.isdigit() for char in paragraph)

        if not (has_key_word and has_month and has_digit):
            return "Unavailable", "Unavailable"
        
        try:
            days = re.findall(r" [0-9]{1,2} ", paragraph)
            starting_day = days[0]
            finishing_day = days[-1]

            months = re.findall("(" + "|".join(self.months_map) + ")", paragraph)
            starting_month = months[0]
            finishing_month = months[-1]

            years = re.findall(r" [0-9]{4}", paragraph)
            starting_year = years[0]
            finishing_year = years[-1]
        except:
            return "Unavailable", "Unavailable"
        
        # Formantando no formato de data
        initial_data = self.format_data(starting_day, starting_month, starting_year)
        finishing_data = self.format_data(finishing_day, finishing_month, finishing_year)

        return initial_data, finishing_data


    def get_especific_page_info(self, url: str):

        """Esta função é dedicada a fazer o scraping de cada página específica de cada concurso.
        Ao rodar o scraping da página, ela pode ser editada para pegar diferentes informações, 
        como inscrição, remuneração, cargos, etc..."""

        soup = self.init_web_scrapper(url)
        paragraphs = soup.select("p:not(.related-post-grid), li")
        
        # Inscrições
        for paragraph in paragraphs:
            paragraph = paragraph.text.lower()
            register_initial_data, register_finishing_data = self.get_registrations_data(paragraph)
            
            if register_initial_data != "Unavailable" and register_finishing_data != "Unavailable":
                break
            
        return register_initial_data, register_finishing_data


    def parse_to_csv(self, contests_dict: dict):

        """Essa função pega o dicionário com os dados dos concursos e 
        o exporta para o formato csv."""

        df = pd.DataFrame(contests_dict)
        df.to_csv("../data/contests_info.csv", index=False, sep=';')

if __name__ == "__main__":

    scrap = Run_scrappers()
    soup = scrap.init_web_scrapper('https://concursosnobrasil.com/concursos/df')

    contests = {}
    scrap.get_contests_entire_info(contests, soup)
    scrap.parse_to_csv(contests)