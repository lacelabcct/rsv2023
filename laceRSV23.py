import requests
import pandas as pd
from bs4 import BeautifulSoup 

def nonAscii(world): # Substituindo os caracteres especiais
    if world == 'Artur Nogueira':
        new_world = world.replace('Artur Nogueira','artur-nogueira')
    elif world == 'Cosmópolis':
        new_world = world.replace('Cosmópolis','cosmopolis')
    elif world == 'Engenheiro Coelho':
        new_world = world.replace('Engenheiro Coelho','engenheiro-coelho')
    elif world == 'Hortolândia':
        new_world = world.replace('Hortolândi','hortolandia')
    elif world == 'Jaguariúna':
        new_world = world.replace('Jaguariúna','jaguariuna')
    elif world == 'Monte Mor':
        new_world = world.replace('Monte Mor','monte-mor')
    elif world == 'Nova Odessa':
        new_world = world.replace('Nova Odessa','nova-odessa')
    elif world == 'Paulínia':
        new_world = world.replace('Paulínia','paulinia')
    elif world == "Santa Bárbara d'Oeste":
        new_world = world.replace("Santa Bárbara d'Oeste",'santa-barbara-d-oeste')
    elif world == 'Santo Antônio de Posse':
        new_world = world.replace('Santo Antônio de Posse','santo-antonio-de-posse')
    elif world == 'Sumaré':
        new_world = world.replace('Sumaré','sumare')
    else:
        new_world = world
    
    return new_world
    
    


class dataScraped:
    
    # Cidades que podem ser selecionadas para consultar
    def selectCity(): 
        select_city = [
            'Americana', 'Artur Nogueira', 'Campinas', 'Cosmópolis', 'Engenheiro Coelho',
            'Holambra', 'Hortolândia', 'Indaiatuba', 'Itatiba', 'Jaguariúna', 'Monte Mor', 
            'Morungaba', 'Nova Odessa', 'Paulínia','Pedreira', "Santa Bárbara d'Oeste",
            'Santo Antônio de Posse', 'Sumaré', 'Valinhos', 'Vinhedo']
        
        return pd.DataFrame(select_city)
    
    # Função para retornar o DataFrame
    def getAPI(city_search, year):
        API = f'https://servicodados.ibge.gov.br/api/v1/localidades/estados/35/municipios'
        
        r = requests.get(API).json() # Requisintando o API do IBGE em JSON
        
        # Organiza os Id's(Códigos Municipais) por cidades
        cidades_sp = [municipios['nome'] for municipios in r]
        cidades_id = [municipios['id'] for municipios in r]
        
        df = pd.DataFrame.from_dict({'ID':cidades_id, 'MUNICIPIOS':cidades_sp})
        
        # Busca o ID pelo index
        city_code = ''
        for i in range(len(df['MUNICIPIOS'])):
            if df['MUNICIPIOS'][i] == city_search:
                city_code = df['ID'][i]

        # Faz a raspagem de dados do portal
        url = f'https://portaldatransparencia.gov.br/localidades/{city_code}-{nonAscii(city_search)}?ano={year}'
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
        
        # Função para retirar e substituir os caracteres especiais($ e ,) por " . "
        def convertValue(value):
            value = value.split('.')
            value = ''.join(value)
            value = value.split(',')
            value = '.'.join(value)
            value = value[3:]
            return value
        
        #PARA FORMATAR COMO NOTAÇÃO CIENTÍFICA:
        # "{:,}".format(resp)
                
        html1 = convertValue(html1)
        html2 = convertValue(html2)
        html3 = convertValue(html3)
        html4 = convertValue(html4)


        # Gera o DataFrame
        df_value = pd.DataFrame(
            {
                link1.get('id'):[html1],
                link2.get('id'):[html2],
                link3.get('id'):[html3],
                link4.get('id'):[html4]
            })
        
        return df_value
    

    if __name__ == '__main__':
        pass
