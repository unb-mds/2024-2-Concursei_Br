import requests
from bs4 import BeautifulSoup
 
BASEURL = 'https://concursosnobrasil.com/concursos/df'
errorMessage = ''
 
def pageRequest(url: str):
    try:
        return requests.get(url)
    except requests.HTTPError:
        print("An http error has ocurred, process has exited")
        return None
    except:
        print("An error has ocurred, process has exited")
        return None

def initWebScraper(url: str, parser: str = 'html.parser'):
    webResponse = pageRequest(url)
 
    if(webResponse == None):
        print("Canceling scrapping")
        return None
 
    return BeautifulSoup(webResponse.text, parser)

def get_contests_links(soup : BeautifulSoup):
 
    constests = {
        'title': [],
        'links': []
    }
 
    links = soup.select("td > a")
    
    for link in links:
        constests['title'].append(link.text)
        constests['links'].append(link['href'])
 
    for key in constests:
        print(constests[key])
 
if __name__ == "__main__":
    soup = initWebScraper(BASEURL)
    get_contests_links(soup)