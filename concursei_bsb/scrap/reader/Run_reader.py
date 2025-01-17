import json
from Txt_reader import Txt_reader

class Run_reader():
    def __init__(self):
        pass

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
                    print("Sucesso")

#Temporário para teste
if __name__ == "__main__":
    teste = Run_reader()
    teste.initialize()