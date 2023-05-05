from laceRSV23 import dataScraped
import streamlit as st
import pandas as pd
from streamlit_chat import message
from time import *
from ioBot import io
from urllib.request import urlopen

st.title('Mackenzie ChatBot')


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
elif user_ == 'sim':
        try:
                select_city = dataScraped.selectCity()
                message('Selecione as cidades que você deseja analisar:')
                search_city = st.multiselect(
                '', select_city)
                frames= []
                a = [
                        frames.append(dataScraped.getAPI(
                        search_city[i], '2022')) for i in range(len(search_city))]

                result = pd.concat(frames)
                st.table(result)
        except:
                pass
        
else:
        message('Desculpa, ainda não fui programado pra compreender o que você escreveu')

try:
        if user_ == "":
                pass
        else:
                response = urlopen(
                f'https://docs.google.com/forms/d/e/1FAIpQLScRqU6yRw2Ykln-42Dj2_NfORcwbsUc_pfadE7p3KPMZtY5AQ/formResponse?&submit=Submit?usp=pp_url&entry.2034641448=x&entry.2146359889={user_}'
                        )
                html = response.read()

        if search_city[0] == '':
                pass
        else:
                response = urlopen(
                f'https://docs.google.com/forms/d/e/1FAIpQLScRqU6yRw2Ykln-42Dj2_NfORcwbsUc_pfadE7p3KPMZtY5AQ/formResponse?&submit=Submit?usp=pp_url&entry.2034641448=x&entry.2146359889={search_city[0]}'
                        )
                html = response.read()

        if search_city[1] == '':
                pass
        else:
                response = urlopen(
                f'https://docs.google.com/forms/d/e/1FAIpQLScRqU6yRw2Ykln-42Dj2_NfORcwbsUc_pfadE7p3KPMZtY5AQ/formResponse?&submit=Submit?usp=pp_url&entry.2034641448=x&entry.2146359889={search_city[1]}'
                        )
                html = response.read()

except:
        pass
