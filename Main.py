from laceRSV23 import dataScraped
import streamlit as st
import pandas as pd
from streamlit_chat import message
from time import *
from ioBot import io
from urllib.request import urlopen
import matplotlib.pyplot as plt

import streamlit as st
import webbrowser
from io import BytesIO
import requests

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

from PIL import Image
#image01 = Image.open('background.JPG')

def SendMAIL(conteudo):
    # create message object instance 
    msg = MIMEMultipart()     
    # setup the parameters of the message 
    password = "efoqfcwiorncteas"
    msg['From'] = "prof.massaki@gmail.com"  
    msg['To'] =   "prof.massaki@gmail.com"
    msg['Subject'] = "Assunto"
    #file = "Python.pdf"
    # attach image to message body 
    #msg.attach(MIMEText(open(file).read()))     
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
with open('style.css') as s:
        st.markdown(f'<style>{s.read()}</style>', unsafe_allow_html=True)


st.title('Mackenzie ChatBot')
#st.image(image01, width=800, caption='RSV2023') 

def user():
        # Transforma as letras em minúscalas e retira o espaço sobrando
        user = st.text_input('Diga um "Oi" para iniciar conversa.').lower().strip()
        return user

user_ = user()

if user_  == "":
        pass
elif user_ in io.bot_answer:
        message(user_, is_user=True)
        message(io.bot_answer[user_])
elif user_ == 'sim':
        try:
                select_city = dataScraped.selectCity()
                message('Selecione algumas cidades para análisar:')
                search_city = st.multiselect(
                '', select_city) # Lista de multipla escolha que usúario escolher 
                yearCity = st.selectbox('',('2023','2022','2021','2020','2019'))  # Lista de escolha única
                frames= []
                a = [
                        frames.append(
                        dataScraped.getAPI(
                        search_city[i], yearCity)) for i in range(len(search_city))]

                result = pd.concat(frames) # Juntando os dados selecionados em uma tabela                
                result['Cidade'] = search_city # Adicionando uma coluna das cidades para ser o index
                st.table(result)      
                x = result['Cidade']
                # Modificando o tipo de valor das colunas
             
                result['recursosTransferidosAoGovernoEstadual'] = pd.to_numeric(result['recursosTransferidosAoGovernoEstadual'])
                result['recursosTransferidosAoMunicipio'] = pd.to_numeric(result['recursosTransferidosAoMunicipio'])
                result['gastosDiretosGovernoFederalNaLocalidade'] = pd.to_numeric(result['gastosDiretosGovernoFederalNaLocalidade'])
                result['beneficiosNaLocalidade'] = pd.to_numeric(result['beneficiosNaLocalidade'])
                
                x = result['Cidade']
                y1 = result['recursosTransferidosAoGovernoEstadual']
                y2 = result['recursosTransferidosAoMunicipio']
                y3 = result['gastosDiretosGovernoFederalNaLocalidade']
                y4 = result['beneficiosNaLocalidade']
                                 
                plt.title('recursosTransferidosAoMunicipio')
                plt.bar(x,y2)
                plt.show()
                st.pyplot(plt)                
                
                url= 'https://docs.google.com/forms/d/e/1FAIpQLSe3k4qby8XCLb4ABrZ972PW_VK4PS3aJo_qCEX-nfDsYiaMeg/formResponse?&submit=Submit?usp=pp_url&entry.705323696=' + yearCity

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

