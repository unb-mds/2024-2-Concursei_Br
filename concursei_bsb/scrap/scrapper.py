import re
import time
import requests
from datetime import datetime
from bs4 import BeautifulSoup
import numpy as np

class Scrapper():
    def __init__(self):
        self.__months_map = {
            "janeiro": "01", "fevereiro": "02", "março": "03", "abril": "04",
            "maio": "05", "junho": "06", "julho": "07", "agosto": "08",
            "setembro": "09", "outubro": "10", "novembro": "11", "dezembro": "12"
        }

        # self.__regions = [
        #     'AC','AL','AM','AP','BA','CE','DF','ES','GO','MA','MG','MS','MT','PA','PB','PE','PI','PR','RJ','RN','RO','RR','RS','SC','SE','SP','TO'
        # ]

        self.__regions = [
            'AC','AL'
        ]

        self.aux = []

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

        if not web_response:
            print("Canceling scrapping")
            return None
    
        return BeautifulSoup(web_response.text, parser)


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

    def __get_registrations_data(self, paragraph: str):
        """A função busca a data de início e a data final de inscrição para o concurso."""

        key_words = ("inscrições", "inscrição", "participação", "candidatar", "data", 'inscrever')

        # Verifica se no parágrafo é citado algum mês e as palavras-chave
        has_key_word = any(key_word in paragraph for key_word in key_words)
        has_month = any(month in paragraph for month in self.__months_map)
        has_digit = any(char.isdigit() for char in paragraph)

        if not (has_key_word and has_month and has_digit):
            return "Unavailable", "Unavailable"

        # Regex para capturar datas em diferentes formatos
        date_pattern = re.compile(
            r"(\d{1,2})\s*(?:de)?\s*(" + "|".join(self.__months_map.keys()) + r")\s*(?:de)?\s*(\d{2,4})?",
            re.IGNORECASE
        )

        # Encontra todas as datas no parágrafo
        dates = date_pattern.findall(paragraph)

        if not dates:
            return "Unavailable", "Unavailable"

        # Processa as datas encontradas
        formatted_dates = []
        for day, month, year in dates:
            month_num = self.__months_map.get(month.lower(), "01")
            year_num = year if year else datetime.now().strftime("%Y")
            formatted_date = f"{day.zfill(2)}/{month_num}/{year_num}"
            formatted_dates.append(formatted_date)

        # Assume que a primeira data é a de início e a última é a de fim
        initial_data = formatted_dates[0]
        finishing_data = formatted_dates[-1]

        return initial_data, finishing_data

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

        np.savetxt("../data/contests_info.csv", contests_array, delimiter=";", 
                   fmt="%s", header="Região;Nome;Vagas;Status;URL;Início;Fim", comments="")
    
    def __list_to_variable(self):
        retorno = ''
        for a in range(len(self.aux)):
            retorno += self.aux[a]
        return retorno
        
    def run_scrapper(self):
        while True:
            #Laço dedicado a verificação do horário para que o scrap seja executado
            time_now = datetime.now()
            if time_now.hour == 22 and time_now.minute == 11:
                contests = np.empty((0, 7), dtype=object)
                for loc in self.__regions:
                    soup =  self.__init_web_scrapper(f'https://concursosnobrasil.com/concursos/{loc}')
                    contests = self.__get_contests_entire_info(loc, contests, soup)
                    self.aux.append(contests)
                self.__parse_to_csv(self.__list_to_variable())
            else:
                pass