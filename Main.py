from laceRSV23 import scraping
import streamlit as st
import pandas as pd
from streamlit_chat import message
from time import *
from ioBot import io


st.title('Projeto Mackenzie')

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


user = st.text_input('Diga um "Oi" para iniciar conversa.')
user = user.lower().strip()

if user  == "":
        pass
elif user in io.bot_answer:
        message(user, is_user=True)
        message(io.bot_answer[user])
        st.table(option)

elif user in io.bot_function:
        message(user, is_user=True)
        message(f'Tabela de {user}:')
        st.table(
                scraping.showData(
                        link='https://transparencia.campinas.sp.gov.br/index.php?action=ws&mode=',
                        answer=io.bot_function[user]
                        )
                        )
        
elif user in io.bot_function2:
        message(user, is_user=True)
        message(f'Tabela {user}:')
        st.table(
                scraping.showData(
                        link='https://transparencia.campinas.sp.gov.br/index.php?action=ws&mode=',
                        answer=io.bot_function2[user]
                        )
                        )
        
else:
        message('Desculpa, ainda não fui programado pra compreender o que você escreveu')

     
btn = [] # lista dos botões

for i in range(len(link_list)):
        btn.append(
                st.sidebar.button(link_list[i][4:])
                )
        if btn[i]:
                st.table(
                        scraping.showData(
                        link='https://transparencia.campinas.sp.gov.br/index.php?action=ws&mode=',
                        answer=link_list[i][1:]
                        )
                )
           
