import re
import time
import requests
from bs4 import BeautifulSoup
import numpy as np

class Run_scrappers():
    def __init__(self):

        self.months_map = {
            'janeiro': '01', 'fevereiro': '02', 'março': '03', 'abril': '04',
            'maio': '05', 'junho': '06', 'julho': '07', 'agosto': '08',
            'setembro': '09', 'outubro': '10', 'novembro': '11', 'dezembro': '12'
        }
    
    def page_request(self, url: str):

        """Faz requisição HTTP e retorna a resposta."""

        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
            time.sleep(3)
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

        web_response = self.page_request(url)

        if not web_response:
            print("Canceling scrapping")
            return None
    
        return BeautifulSoup(web_response.text, parser)


    def feed_dict(self, contests_array: np.ndarray, *args):
        
        """Essa função alimenta o dicionário que armazena os dados dos concursos."""
        
        new_row = np.array(args, object).reshape(1, -1)
        return np.vstack([contests_array, new_row])

    def translate_forecast(self, forecast: object|None):

        """Função que identifica o valor de forecast e o renomeia
        de acordo com um padrão amigável para colocar no csv."""

        return "Previsto" if forecast else "Aberto"


    def get_contests_entire_info(self, contests_array: np.ndarray, soup):

        """Faz scraping da página principal de concursos."""
        
        info = soup.select('tr:not(:first-child)')

        for index, tr in enumerate(info):
            
            a_tag = tr.find("a")
            name = a_tag.text.strip()
            url = a_tag['href']
            vacancies = tr.find("td", class_="center").text.strip()
            forecast = self.translate_forecast(tr.find("div", class_='label-previsto'))

            register_intial_data, final_register_data = self.get_especific_page_info(url)

            contests_array = self.feed_dict(contests_array, name, vacancies, forecast, url,
                           register_intial_data, final_register_data)
        
        return contests_array


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
            starting_day, finishing_day = days[0], days[-1]

            months = re.findall("(" + "|".join(self.months_map) + ")", paragraph)
            starting_month, finishing_month = months[0], months[-1]

            years = re.findall(r" [0-9]{4}", paragraph)
            starting_year, finishing_year = years[0], years[-1]
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
            initial_register_data, register_finishing_data = self.get_registrations_data(paragraph)
            
            if initial_register_data != "Unavailable" and register_finishing_data != "Unavailable":
                break
            
        return initial_register_data, register_finishing_data


    def parse_to_csv(self, contests_array: np.ndarray):

        """Essa função pega o dicionário com os dados dos concursos e 
        o exporta para o formato csv."""

        np.savetxt("../data/contests_info.csv", contests_array, delimiter=";", 
                   fmt="%s", header="Nome;Vagas;Status;URL;Início;Fim", comments="")

if __name__ == "__main__":

    scrap = Run_scrappers()
    soup = scrap.init_web_scrapper('https://concursosnobrasil.com/concursos/df')

    contests = np.empty((0, 6), dtype=object)
    contests = scrap.get_contests_entire_info(contests, soup)
    scrap.parse_to_csv(contests)