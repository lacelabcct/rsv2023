from laceRSV23 import scraping
import streamlit as st
import pandas as pd
from streamlit_chat import message
from time import *
from ioBot import io
from urllib.request import urlopen

st.title('Mackenzie ChaBot')

link_list = scraping.linkList(url='https://transparencia.campinas.sp.gov.br/index.php?action=dadosabertos',
                              tag='a',
                              classdiv='class',
                              name='btn btn-default btn-coresAlteradas btn-bordasMaiores btn-metodo')



# enumerando os links
enumerateList = {}
for x,y in enumerate(link_list):
        z = []
        z.append(y[4:])
        enumerateList[x] = z

option = pd.DataFrame(data=enumerateList)


def user():
        user = st.text_input('Diga um "Oi" para iniciar conversa.').lower().strip()
        user = user.lower().strip()
        return user

user_ = user()
if user_  == "":
        pass
elif user_ in io.bot_answer:
        message(user_, is_user=True)
        message(io.bot_answer[user_])
        btn = [] # lista dos botões

        for i in range(len(link_list)):
                btn.append(
                        st.button(link_list[i][4:],use_container_width=True)
                        )
                if btn[i]:
                        st.table(
                                scraping.showData(
                                link='https://transparencia.campinas.sp.gov.br/index.php?action=ws&mode=',
                                answer=link_list[i][1:]
                                )
                        )

elif user_ in io.bot_function:
        message(user_, is_user=True)
        message(f'Tabela de {user_}:')
        st.table(
                scraping.showData(
                        link='https://transparencia.campinas.sp.gov.br/index.php?action=ws&mode=',
                        answer=io.bot_function[user_]
                        )
                        )
        
elif user_ in io.bot_function2:
        message(user_, is_user=True)
        message(f'Tabela {user_}:')
        st.table(
                scraping.showData(
                        link='https://transparencia.campinas.sp.gov.br/index.php?action=ws&mode=',
                        answer=io.bot_function2[user_]
                        )
                        )
        
else:
        message('Desculpa, ainda não fui programado pra compreender o que você escreveu')

if user_ == "":
        pass
else:
        response = urlopen(
        f'https://docs.google.com/forms/d/e/1FAIpQLScRqU6yRw2Ykln-42Dj2_NfORcwbsUc_pfadE7p3KPMZtY5AQ/formResponse?&submit=Submit?usp=pp_url&entry.2034641448=x&entry.2146359889={user_}'
                )
        html = response.read()

           
