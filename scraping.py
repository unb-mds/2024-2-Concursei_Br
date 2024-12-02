import requests
from datetime import date
from io import BytesIO
from PyPDF2 import PdfReader

# Link das edições: https://dodf.df.gov.br/dodf/jornal/pastas
# Esse é o caminho padrão das edições do diário oficial do DODF.
# Abaixo tem o padrão do link de cada pdf do diário oficial.
#
# "pasta=ANO":      pasta=ANO_DESEJADO
# "MES_MES":        MÊS_EM_NÚMERO/MÊS_POR_EXTENSO
# "ID":             ID_DA_PUBLICAÇÃO (O nº da publicação do ano. A primeira publicação do ano é sempre 001, a segunda, 002, terceira, 003...)
# "DIA-MES-ANO":    DIA-MES-ANO em número

PDF_PATH = "https://dodf.df.gov.br/dodf/jornal/visualizar-pdf?pasta=ANO|MES_MES|DODF%20ID%20DIA-MES-ANO|&arquivo=DODF%20ID%20DIA-MES-ANO%20INTEGRA.pdf"
STANDARD_PDF_CLASS = "link-materia"
MONTHS = {
    "1": "janeiro",
    "2": "fevereiro",
    "3": "março",
    "4": "abril",
    "5": "maio",
    "6": "junho",
    "7": "julho",
    "8": "agosto",
    "9": "setembro",
    "10": "outubro",
    "11": "novembro",
    "12": "dezembro"
}

def fetch_daily_pdf():

    current_year, current_month, current_day = str(date.today()).split("-")
    
    # Corrigindo o link para a data atual
    pdf_link = PDF_PATH.replace("pasta=ANO", f"pasta={current_year}")
    pdf_link = pdf_link.replace("MES_MES", f"{current_month}_{MONTHS[current_month].capitalize()}")
    pdf_link = pdf_link.replace("DIA-MES-ANO", f"{current_day}-{current_month}-{current_year}")

    # Link de teste
    # pdf_link = "https://dodf.df.gov.br/dodf/jornal/visualizar-pdf?pasta=2024|01_Janeiro|DODF%20ID%2031-01-2024|&arquivo=DODF%20ID%2031-01-2024%20INTEGRA.pdf"

    # O ID da publicação é sempre incerto, pois depende de feriados, fins de semana, e publicações de emergência
    # Então vamos loopar por todos os ids possíveis até encontrar o da data atual
    for i in range(20001, 20002):

        updated_link = pdf_link.replace("20ID", str(i))

        # Buscando o link
        res = requests.get(updated_link)

        if res.headers.get("content-type") == "application/pdf":
            continue
        else:
            # Gerando objeto para manipular pdf
            pdf_content = BytesIO(res.content)
            pdfreader = PdfReader(pdf_content)
            return pdfreader
    
    return None