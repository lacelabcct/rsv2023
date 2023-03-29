# Bibilotecas importadas 
from bs4 import BeautifulSoup
from urllib.request import urlopen
import json
import requests
import pandas as pd

# Searching the element of data HTML
page = requests.get(
    'https://transparencia.campinas.sp.gov.br/index.php?action=dadosabertos' # interligando
    )
soup = BeautifulSoup(page.content,'html.parser')

class scraping:
    # Function to get all elements database names
    def linkList():
        link_list = []
        for link in soup.find_all('a',{'class':'btn btn-default btn-coresAlteradas btn-bordasMaiores btn-metodo'}):
            link_list.append(f"{link.get('href')[1:]}")
        return link_list
    
    # Function to import the database selected and show the table
    def showData(answer):
        url = f"https://transparencia.campinas.sp.gov.br/index.php?action=ws&mode={answer}"
        response = urlopen(url)
        data_json = json.loads(response.read())
        df = pd.DataFrame(data_json)
        return df

