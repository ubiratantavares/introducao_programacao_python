from datetime import date, time, datetime, timedelta

def trabalhando_com_date():
    # cria a data do sistema
    data_atual = date.today()
    print(data_atual, type(data_atual))
    print(data_atual.strftime('%A, %B, %Y'))

    # transforma a data para formato de string
    data_atual_str = data_atual.strftime('%d/%m/%Y')
    print(data_atual_str, type(data_atual_str))


def trabalhando_com_time():
    # cria uma hora em formato hora:minuto:segundo
    horario = time(15, 18, 30)
    print(horario, type(horario))

    # transforma a hora para formato de string
    horario_str = horario.strftime('%H:%M:%S')
    print(horario_str, type(horario_str))


def trabalhando_com_datetime():
    # cria a data e hora do sistema
    data_hora_atual = datetime.now()
    print(data_hora_atual, type(data_hora_atual))

    # transforma a data e hora para formato de string
    data_hora_atual_str = data_hora_atual.strftime('%d/%m/%Y %H:%M:%S')
    print(data_hora_atual_str, type(data_hora_atual_str))
    
    data_hora_atual_str = data_hora_atual.strftime('c')
    print(data_hora_atual_str, type(data_hora_atual_str))
    
    print('Dia: ', data_hora_atual.day)
    print('Mês: ', data_hora_atual.month)
    print('Ano: ', data_hora_atual.year)
    print('Data: ', data_hora_atual.date())
    print('Dia da semana: ', data_hora_atual.weekday())
    
    tupla = ('SEG', 'TER', 'QUA', 'QUI', 'SEX', 'SAB', 'DOM')
    
    print('Dia da semana:', tupla[data_hora_atual.weekday()])
    
    data_criada = datetime(2018, 6, 20, 15, 30, 20)
    print(data_criada, type(data_criada))
    print(data_criada.strftime('%c'), type(data_criada))
    
    data_string = '01/01/2019 12:20:22'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S')
    print(data_convertida, type(data_convertida))

    # timedelta(qtd_dias, qtd_horas, qtd_minutos)
    nova_data = data_convertida - timedelta(365, 2, 15)
    print(nova_data, type(nova_data))


if __name__ == '__main__':
    #trabalhando_com_date()
    #trabalhando_com_time()
    trabalhando_com_datetime()

    data_atual = datetime.now()
    resultado = data_atual.strftime('%d/%m/%Y %H:%M:%S')
    print(resultado, type(resultado))

    data= datetime(1815, 12, 10, 00, 00, 00).strftime('%d/%m/%Y')
    hora = time(13, 14, 00)
    print('{} às {}'.format(data, hora))

    data_viagem = datetime.now() - timedelta(days=1)
    print(datetime.now().weekday()) #retornou 0
    print(data_viagem, type(data_viagem))