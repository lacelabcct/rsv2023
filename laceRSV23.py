# Bibilotecas importadas 
from bs4 import BeautifulSoup
from urllib.request import urlopen
import json
import requests
import pandas as pd


class scraping:
    
    # Função para pegar todos nomes do banco de dados
    def linkList(url,tag,classdiv,name):
        # Procurando o elemento do HTML
        page = requests.get(url)
        soup = BeautifulSoup(page.content,'html.parser')
        link_list = []
        for link in soup.find_all(tag,{classdiv:name}):
            link_list.append(f"{link.get('href')}")
        return link_list
    
    # Função para importa e mostrar os dados num dataframe
    def showData(link, answer):
        url = f'{link}{answer}'
        response = urlopen(url)
        data_json = json.loads(response.read())
        df = pd.DataFrame(data_json)
        return df
