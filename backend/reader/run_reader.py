
import json
from txt_reader import *

if __name__ == "__main__":

    with open(GAZZETE_PATHS, "r") as file:
        gazette_links = json.load(file)

    # Loop que passa por todos os munincípios e todas suas publicações
    for i in range(len(gazette_links)):
        for j in range(len(gazette_links[list(gazette_links.keys())[i]])):

            gazette_text = request_gazzete_url(gazette_links, i, j)
            if gazette_text:
                print("Sucesso")