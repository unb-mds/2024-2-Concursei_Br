import re
import time
import requests
from datetime import datetime
from bs4 import BeautifulSoup
import numpy as np
import time

class Scrapper():
    def __init__(self):
        self.__months_map = {
            "janeiro": "01", "fevereiro": "02", "março": "03", "abril": "04",
            "maio": "05", "junho": "06", "julho": "07", "agosto": "08",
            "setembro": "09", "outubro": "10", "novembro": "11", "dezembro": "12"
        }

        self.__regions = [
            'AC','AL','AM','AP','BA','CE','DF','ES','GO','MA','MG','MS','MT','PA','PB','PE','PI','PR','RJ','RN','RO','RR','RS','SC','SE','SP','TO'
        ]

        self.__months_regex = re.compile("|".join(self.__months_map))
        self.__key_words_regex = re.compile(r'inscrições|inscrição|participação|candidatar|data|inscrever')
        self.__digit_regex = re.compile(r'\d')

    def __page_request(self, url: str):

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


    def __init_web_scrapper(self, url: str, parser: str = 'html.parser'):

        """Essa função retorna um objeto BeautifulSoup, para que assim seja
        possível manipular o texto de alguma página e realizar o scraping."""

        web_response = self.__page_request(url)
        return BeautifulSoup(web_response.content, parser)


    def __feed_dict(self, contests_array: np.ndarray, *args):
        
        """Essa função alimenta o dicionário que armazena os dados dos concursos."""
        
        new_row = np.array(args, object).reshape(1, -1)
        return np.vstack([contests_array, new_row])

    def __translate_forecast(self, forecast: object|None):

        """Função que identifica o valor de forecast e o renomeia
        de acordo com um padrão amigável para colocar no csv."""

        return "Previsto" if forecast else "Aberto"


    def __get_contests_entire_info(self, region, contests_array: np.ndarray, soup):

        """Faz scraping da página principal de concursos."""
        
        info = soup.select('tr:not(:first-child)')

        for index, tr in enumerate(info):
            
            a_tag = tr.find("a")
            name = a_tag.text.strip()
            url = a_tag['href']
            vacancies = tr.find("td", class_="center").text.strip()
            forecast = self.__translate_forecast(tr.find("div", class_='label-previsto'))

            if forecast == "Previsto":
                contests_array = self.__feed_dict(contests_array, region, name, vacancies, forecast, url,
                'Unavailable', 'Unavailable')
            else:
                register_intial_data, final_register_data = self.__get_especific_page_info(url)

                contests_array = self.__feed_dict(contests_array, region, name, vacancies, forecast, url,
                            register_intial_data, final_register_data)
        
        return contests_array
    
    def __verify_key_words(self, paragraph: str):

        if not self.__months_regex.search(paragraph):
            return False

        if not self.__key_words_regex.search(paragraph):
            return False

        if not self.__digit_regex.search(paragraph):
            return False
        
        return True


    def __get_registrations_data(self, paragraph: str):
        """A função busca a data de início e a data final de inscrição para o concurso."""

        has_key_words = self.__verify_key_words(paragraph)

        if not has_key_words:
            return "Unavailable", "Unavailable"

        try:
            days = re.findall(r" [0-9]{1,2} ", paragraph)
            starting_day = days[0]
            finishing_day = days[-1]

            months = re.findall("(" + "|".join(self.__months_map) + ")", paragraph)
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

    def __get_especific_page_info(self, url: str):

        """Esta função é dedicada a fazer o scraping de cada página específica de cada concurso.
        Ao rodar o scraping da página, ela pode ser editada para pegar diferentes informações, 
        como inscrição, remuneração, cargos, etc..."""

        soup = self.__init_web_scrapper(url)
        paragraphs = soup.select("p:not(.related-post-grid), li")
        
        # Inscrições
        for paragraph in paragraphs:
            paragraph = paragraph.text.lower()
            initial_register_data, register_finishing_data = self.__get_registrations_data(paragraph)
            
            if initial_register_data != "Unavailable" and register_finishing_data != "Unavailable":
                break
            
        return initial_register_data, register_finishing_data


    def __parse_to_csv(self, contests_array: np.ndarray):

        """Essa função pega o dicionário com os dados dos concursos e 
        o exporta para o formato csv."""

        file_path = "../data/contests_info.csv"

        np.savetxt(file_path, contests_array, delimiter=";", 
                fmt="%s", header="Região;Nome;Vagas;Status;URL;Início;Fim", comments="")

        
    def run_scrapper(self):
        #Laço dedicado a verificação do horário para que o scrap seja executado

        now = time.time()

        while True:

            # if time_now.hour == 0 and time_now.minute == 0:
            contests = np.empty((0, 7), dtype=object)
            
            for loc in self.__regions:

                print(loc)
                soup =  self.__init_web_scrapper(f'https://concursosnobrasil.com/concursos/{loc}')
                contests = self.__get_contests_entire_info(loc, contests, soup)
                
            self.__parse_to_csv(contests)
            break

        after = time.time()

        
        print("Tempo: " + after - now)