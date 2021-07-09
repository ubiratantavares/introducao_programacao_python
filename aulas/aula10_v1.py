# -*- coding: utf-8 -*-

from datetime import date, time, datetime, timedelta

def trabalhando_com_date():    
    data_atual = date.today()
    print(type(data_atual))
    print(data_atual)
    
    data_atual_str = data_atual.strftime('%d/%m/%Y')
    print(type(data_atual_str))
    print(data_atual_str)    
    print(data_atual.strftime('%A %B %Y'))   

def trabalhando_com_time():
    horario = time(hour = 15, minute = 18, second = 30)
    print(type(horario))
    print(horario)
    horario_str = horario.strftime('%H:%M:%S')
    print(type(horario_str))
    print(horario_str)
    
def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(type(data_atual))
    print(data_atual)
    
    data_atual_str = data_atual.strftime('%d/%m/%Y %H:%M:%S')
    print(type(data_atual_str))
    print(data_atual_str)     
    
    data_atual_str = data_atual.strftime('c')
    print(type(data_atual_str))
    print(data_atual_str)  
    
    print(data_atual.day)
    print(data_atual.month)
    print(data_atual.year)   
    print(data_atual.date())
    print(data_atual.weekday())
    
    tupla = ('Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab', 'Dom')
    
    print(tupla[data_atual.weekday()])
    
    data_criada = datetime(2018, 6, 20, 15, 30, 20)
    print(data_criada)
    print(data_criada.strftime('%c'))
    
    data_string = '01/01/2019 12:20:22'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S')
    print(data_convertida)
    
    nova_data = data_convertida - timedelta(days = 365, hours = 2, minutes = 15)
    print(nova_data)    
    
if __name__ == '__main__':
    trabalhando_com_date()
    trabalhando_com_time()
    trabalhando_com_datetime()