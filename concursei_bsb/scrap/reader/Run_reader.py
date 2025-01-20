import json
from Txt_reader import Txt_reader
import re

class Run_reader():
    def __init__(self):
        self.__SAIDA = open('../../data/saida.txt', 'w')

    def initialize(self):
        reader = Txt_reader()
        with open(reader.get_GAZZETE_PATHS(), "r") as file:
            gazette_links = json.load(file)

        # Loop que passa por todos os munincípios e todas suas publicações
        for i in range(len(gazette_links)):
            for j in range(len(gazette_links[list(gazette_links.keys())[i]])):
                #Retorna o texto caso passe gazette_text no print
                gazette_text = reader.request_gazzete_url(gazette_links, i, j)
                if gazette_text:
                    #Em desenvolvimento: leitura de linhas com regex
                    for z in gazette_text.split('\n'):
                        if re.search(r"^(\w+)\s+(da|de)\s+(\w+)", z) != None:
                            self.__SAIDA.write(f'{re.search(r"^(\w+)\s+(da|de)\s+(\w+)", z).group()}\n')
        self.__SAIDA.close()

    #Teste de leitura de regex
    # def extrair_informacoes_importantes(self):
    #     """
    #     Função para extrair informações importantes do texto do edital.
    #     """
    #     # Definindo as expressões regulares para buscar as informações chave
    #     informacoes = {
    #         "cargo": re.findall(r"Cargo[s]?:\s*([A-Za-z\s]+)", self.__SAIDA),
    #         "remuneracao": re.findall(r"Remuneração?:\s*([R\$0-9,.]+)", self.__SAIDA),
    #         "requisitos": re.findall(r"Requisitos?:\s*([^\n]+)", self.__SAIDA),
    #         "data_limite": re.findall(r"Data de Inscrição Final?:\s*([0-9]{2}/[0-9]{2}/[0-9]{4})", self.__SAIDA),
    #         "data_prova": re.findall(r"Data da Prova?:\s*([0-9]{2}/[0-9]{2}/[0-9]{4})", self.__SAIDA)
    #     }
    #     return informacoes

#Temporário para teste
if __name__ == "__main__":
    teste = Run_reader()
    teste.initialize()
    # for g in teste.extrair_informacoes_importantes():
        # print(teste.extrair_informacoes_importantes()[g])