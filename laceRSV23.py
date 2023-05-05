import requests
import pandas as pd
import unicodedata
from bs4 import BeautifulSoup 

def remove_normalized(string: str) -> str:
        normalized = unicodedata.normalize('NFC', string)
        return normalized.enconde('ascii', 'ignore').decode('utf8').casefold()

class dataScraped:

    def selectCity():
        select_city = [
            'Americana', 'Artur Nogueira', 'Campinas', 'Cosmópolis', 'Engenheiro Coelho',
            'Holambra', 'Hortolândi', 'Indaiatuba', 'Itatiba', 'Jaguariúna', 'Monte Mor', 
            'Morungaba', 'Nova Odessa', 'Paulínia','Pedreira', "Santa Bárbara d'Oeste",
            'Santo Antônio de Posse', 'Sumaré', 'Valinhos', 'Vinhedo']
        
        return pd.DataFrame(select_city)
    
    
    def getAPI(city_search, year):
        urll = f'https://servicodados.ibge.gov.br/api/v1/localidades/estados/35/municipios'
        
        r = requests.get(urll).json()
        
        cidades_sp = [municipios['nome'] for municipios in r]
        cidades_id = [municipios['id'] for municipios in r]
        
        df = pd.DataFrame.from_dict({'ID':cidades_id, 'MUNICIPIOS':cidades_sp})
        
        city_code = ''
        for i in range(len(df['MUNICIPIOS'])):
            if df['MUNICIPIOS'][i] == city_search:
                city_code = df['ID'][i]
        
        url = f'https://portaldatransparencia.gov.br/localidades/{city_code}-#?ano={year}'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        link1 = soup.find("span", {"id": "recursosTransferidosAoGovernoEstadual"})
        html1 = link1.get('data-original-title')

        link2 = soup.find("span", {"id": "recursosTransferidosAoMunicipio"})
        html2 = link2.get('data-original-title')

        link3 = soup.find("span", {"id": "gastosDiretosGovernoFederalNaLocalidade"})
        html3 = link3.get('data-original-title')

        link4 = soup.find("span", {"id": "beneficiosNaLocalidade"})
        html4 = link4.get('data-original-title')


        df_value = pd.DataFrame(
            {
                link1.get('id'):[html1],
                link2.get('id'):[html2],
                link3.get('id'):[html3],
                link4.get('id'):[html4]
            })
        return df_value


