from time import *


class io:

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
        
       
        bot_answer = {
                'oi':f'{hourGreetings()}, tudo bem? Gostaria de consultar nossa base de dados?',
                'olá':f'{hourGreetings()}, tudo bem? Gostaria de consultar nossa base de dados?',
                'ola':f'{hourGreetings()}, tudo bem? Gostaria de consultar nossa base de dados?',
                'que horas são?':f'São {asctime()[11:16:1]}',
                'que horas sao?':f'São {asctime()[11:16:1]}',
                'que horas são':f'São {asctime()[11:16:1]}',
                'que horas sao':f'São {asctime()[11:16:1]}'
        }

        
