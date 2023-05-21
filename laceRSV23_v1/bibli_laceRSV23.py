#ioBot
from time import *


class io:
    hour = asctime()
    hour = int(hour[11] + hour[12])

    def hourGreetings(anotherHour=hour):
        result = ''
        if anotherHour <= 11:
            result = 'Bom dia'
        elif anotherHour <= 19:
            result = 'Boa tarde'
        else:
            result = 'Boa noite'
        return result

    bot_answer = {
        'oi': f'{hourGreetings()}, tudo bem? Gostaria de consultar nossa base de dados?',
        'olá': f'{hourGreetings()}, tudo bem? Gostaria de consultar nossa base de dados?',
        'ola': f'{hourGreetings()}, tudo bem? Gostaria de consultar nossa base de dados?',
        'que horas são?': f'São {asctime()[11:16:1]}',
        'que horas sao?': f'São {asctime()[11:16:1]}',
        'que horas são': f'São {asctime()[11:16:1]}',
        'que horas sao': f'São {asctime()[11:16:1]}'
    }

#laceRSV23
import requests
#import pandas as pd
from bs4 import BeautifulSoup


def nonAscii(world):  # Substituindo os caracteres especiais
    if world == 'Artur Nogueira':
        new_world = world.replace('Artur Nogueira', 'artur-nogueira')
    elif world == 'Cosmópolis':
        new_world = world.replace('Cosmópolis', 'cosmopolis')
    elif world == 'Engenheiro Coelho':
        new_world = world.replace('Engenheiro Coelho', 'engenheiro-coelho')
    elif world == 'Hortolândia':
        new_world = world.replace('Hortolândi', 'hortolandia')
    elif world == 'Jaguariúna':
        new_world = world.replace('Jaguariúna', 'jaguariuna')
    elif world == 'Monte Mor':
        new_world = world.replace('Monte Mor', 'monte-mor')
    elif world == 'Nova Odessa':
        new_world = world.replace('Nova Odessa', 'nova-odessa')
    elif world == 'Paulínia':
        new_world = world.replace('Paulínia', 'paulinia')
    elif world == "Santa Bárbara d'Oeste":
        new_world = world.replace("Santa Bárbara d'Oeste", 'santa-barbara-d-oeste')
    elif world == 'Santo Antônio de Posse':
        new_world = world.replace('Santo Antônio de Posse', 'santo-antonio-de-posse')
    elif world == 'Sumaré':
        new_world = world.replace('Sumaré', 'sumare')
    else:
        new_world = world

    return new_world


class dataScraped:

    # Cidades que podem ser selecionadas para consultar
    def selectCity():
        select_city = [
            'Americana', 'Artur Nogueira', 'Campinas', 'Cosmópolis', 'Engenheiro Coelho',
            'Holambra', 'Hortolândia', 'Indaiatuba', 'Itatiba', 'Jaguariúna', 'Monte Mor',
            'Morungaba', 'Nova Odessa', 'Paulínia', 'Pedreira', "Santa Bárbara d'Oeste",
            'Santo Antônio de Posse', 'Sumaré', 'Valinhos', 'Vinhedo']

        return pd.DataFrame(select_city)

    # Função para retornar o DataFrame
    def getAPI(city_search, year):
        API = f'https://servicodados.ibge.gov.br/api/v1/localidades/estados/35/municipios'

        r = requests.get(API).json()  # Requisintando o API do IBGE em JSON

        # Organiza os Id's(Códigos Municipais) por cidades
        cidades_sp = [municipios['nome'] for municipios in r]
        cidades_id = [municipios['id'] for municipios in r]

        df = pd.DataFrame.from_dict({'ID': cidades_id, 'MUNICIPIOS': cidades_sp})

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

        # PARA FORMATAR COMO NOTAÇÃO CIENTÍFICA:
        # "{:,}".format(resp)

        html1 = convertValue(html1)
        html2 = convertValue(html2)
        html3 = convertValue(html3)
        html4 = convertValue(html4)

        # Gera o DataFrame
        df_value = pd.DataFrame(
            {
                link1.get('id'): [html1],
                link2.get('id'): [html2],
                link3.get('id'): [html3],
                link4.get('id'): [html4]
            })

        return df_value

    if __name__ == '__main__':
        pass

#main
#from laceRSV23 import dataScraped
import pandas as pd
from streamlit_chat import message
from time import *
#from ioBot import io
from urllib.request import urlopen
import matplotlib.pyplot as plt

import streamlit as st
import webbrowser
#from io import BytesIO
import requests

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText


def SendMAIL(conteudo):
    # create message object instance
    msg = MIMEMultipart()
    # setup the parameters of the message
    password = "efoqfcwiorncteas"
    msg['From'] = "prof.massaki@gmail.com"
    msg['To'] = "prof.massaki@gmail.com"
    msg['Subject'] = "Assunto"
    # file = "Python.pdf"
    # attach image to message body
    # msg.attach(MIMEText(open(file).read()))
    # create server
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    # Login Credentials for sending the mail
    server.login(msg['From'], password)
    # send the message via the server.
    conteudo = "Subject: RSV2023(Mackenzie&Urbe9) \r\n" + conteudo
    server.sendmail(msg['From'], msg['To'], str(conteudo))
    server.quit()


# Abre o arquivo css para que posso modificar as estrura visual do site
#with open('style.css') as s:
#    st.markdown(f'<style>{s.read()}</style>', unsafe_allow_html=True)

st.title('Mackenzie ChatBot')


def user():
    # Transforma as letras em minúscalas e retira o espaço sobrando
    user = st.text_input('Diga um "Oi" para iniciar conversa.').lower().strip()
    return user


user_ = user()

if user_ == "":
    pass
elif user_ in io.bot_answer:
    message(user_, is_user=True)
    message(io.bot_answer[user_])
elif user_ == 'sim':
    try:
        select_city = dataScraped.selectCity()
        message('Selecione algumas cidades para análisar:')
        search_city = st.multiselect(
            '', select_city)  # Lista de multipla escolha que usúario escolher
        yearCity = st.selectbox('', ('2023', '2022', '2021', '2020', '2019'))  # Lista de escolha única
        frames = []
        a = [
            frames.append(
                dataScraped.getAPI(
                    search_city[i], yearCity)) for i in range(len(search_city))]

        result = pd.concat(frames)  # Juntando os dados selecionados em uma tabela
        result['Cidade'] = search_city  # Adicionando uma coluna das cidades para ser o index
        st.table(result)
        x = result['Cidade']
        # Modificando o tipo de valor das colunas

        result['recursosTransferidosAoGovernoEstadual'] = pd.to_numeric(result['recursosTransferidosAoGovernoEstadual'])
        result['recursosTransferidosAoMunicipio'] = pd.to_numeric(result['recursosTransferidosAoMunicipio'])
        result['gastosDiretosGovernoFederalNaLocalidade'] = pd.to_numeric(
            result['gastosDiretosGovernoFederalNaLocalidade'])
        result['beneficiosNaLocalidade'] = pd.to_numeric(result['beneficiosNaLocalidade'])

        x = result['Cidade']
        y1 = result['recursosTransferidosAoGovernoEstadual']
        y2 = result['recursosTransferidosAoMunicipio']
        y3 = result['gastosDiretosGovernoFederalNaLocalidade']
        y4 = result['beneficiosNaLocalidade']

        plt.title('recursosTransferidosAoMunicipio')
        plt.bar(x, y2)
        plt.show()
        st.pyplot(plt)

        url = 'https://docs.google.com/forms/d/e/1FAIpQLSe3k4qby8XCLb4ABrZ972PW_VK4PS3aJo_qCEX-nfDsYiaMeg/formResponse?&submit=Submit?usp=pp_url&entry.705323696=' + yearCity

        if st.button('Enviar Dados para e-mail 👇'):
            DadosToSend = str(y1) + ', ' + str(y2) + ', ' + str(y3) + ', ' + str(y4)
            SendMAIL(str(DadosToSend))
            response = urlopen(f'{url}')
            html = response.read()
    except:
        pass

else:
    # Caso o usuário digite algo que não foi programado, exiba esta mensagem
    message('Desculpa, ainda não fui programado pra compreender o que você escreveu')


# Função agrega o dado inserido para uma planilha
def add_sheets(data):
    response = urlopen(
        f'https://docs.google.com/forms/d/e/1FAIpQLScRqU6yRw2Ykln-42Dj2_NfORcwbsUc_pfadE7p3KPMZtY5AQ/formResponse?&submit=Submit?usp=pp_url&entry.2034641448=x&entry.2146359889={data}')
    html = response.read()
    return html


try:
    # Adicionando as palavras que o usuário digitou no banco de dados
    if user_ == "":
        pass
    else:
        add_sheets(user_)
except:
    pass