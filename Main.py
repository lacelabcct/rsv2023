from WebSCR import scraping
import streamlit as st
import pandas as pd



st.title('Projeto Mackenzie')

link_list = scraping.linkList()

btn = [] # lista dos botões

# 
for i in range(len(link_list)):
        btn.append(
                st.sidebar.button(link_list[i][3:])
                )
        if btn[i]:
                st.table(
                        scraping.showData(
                        link_list[i]
                        )
                )


amountLink = len(link_list) - 1

# enumerando os links
enumerateList = {}
for x,y in enumerate(link_list):
        z = []
        z.append(y)
        enumerateList[x] = z

option = pd.DataFrame(data=enumerateList)

st.table(option)

# comando de pesquisa via texto
search = st.number_input(
        'Escolha um número',max_value=amountLink, min_value=0
        )
 
st.table(
        scraping.showData(
                        link_list[search]
                        )
)
                


