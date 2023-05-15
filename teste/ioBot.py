from time import *
from laceRSV23V01 import scraping


class io:
        link_list = scraping.linkList(url='https://transparencia.campinas.sp.gov.br/index.php?action=dadosabertos',
                              tag='a',
                              classdiv='class',
                              name='btn btn-default btn-coresAlteradas btn-bordasMaiores btn-metodo')
        
        extend_base = []
        for i in link_list:
              letter = []
              letter.extend(i[4:])
              letter_cut = []
              for x in letter:
                      if x.isupper():
                                letter_cut.append(' ')
                                letter_cut.append(x)
                      else:
                              letter_cut.append(x)
              letter_cut = ''.join(letter_cut).strip().lower()

              extend_base.append(letter_cut)


        hour = asctime()
        hour = int(hour[11]+hour[12])
        def hourGreetings(anotherHour = hour):
                result = ''
                if anotherHour <= 11:
                        result = 'Bom dia'
                elif anotherHour <= 19:
                        result = 'Boa tarde'
                else:
                        result = 'Boa noite' 
                return result
        
        bot_function = {}
        bot_function2 = {}

        for key in extend_base:
                for value in link_list:
                        bot_function[key] = value[1:]
        
        for key in link_list:
                key = key[4:].lower()
                for value in link_list:
                        bot_function2[key] = value[1:]
        

        bot_answer = {
                'oi':f'{hourGreetings()}, tudo bem? Gostaria de consultar qual base de dados? Digite o nome.',
                'olá':f'{hourGreetings()}, tudo bem? Gostaria de consultar qual base de dados? Digite o nome.',
                'ola':f'{hourGreetings()}, tudo bem? Gostaria de consultar qual base abaixo? Digite o nome.',
                'que horas são?':f'São {asctime()[11:16:1]}',
                'que horas sao?':f'São {asctime()[11:16:1]}',
                'que horas são':f'São {asctime()[11:16:1]}',
                'que horas sao':f'São {asctime()[11:16:1]}'
        }

        
