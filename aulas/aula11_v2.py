class Error(Exception):
    pass


class InputError(Error):
    def __init__(self, msg):
        self.msg = msg

while True:
    try:
        nota = int(input('Digite o valor da nota de 0 a 10: '))
        if nota > 10:
            # lança a exceção
            raise(InputError('Valor não pode ser maior que 10.'))
        elif nota < 0:
            raise(InputError('Valor não pode ser menor que 0.'))
        print('Valor da nota informada: ', nota)
        break
    # trata o erro da exceção
    except ValueError:
        print('Entrada inválida.')
    except InputError as ex:
        print(ex)


try:
  x = 1
  elementos = ['terra', 'ar', 'fogo', 'agua']
  elementos.pop(x)
except:
  print('Elemento não encontrado')
else:
  print('Elemento {} removido.'.format(x))
finally:
  print('Busca completa')


try:
    lista = [1, 2]
    print(lista[2])
except Exception:
    print('Ocorreu um erro desconhecido')
except IndexError:
    print('Não foi possível acessar o index pois ele não existe na lista')

nome = 'Adda'
while True:
    try:
        x = input('Digite um nome: ')
        if x == nome:
            break
        else:
            raise InputError('Nome inválido')
    except InputError as ex:
        print(ex)

try:
    divisao = 10 / 0
except ArithmeticError:
    erro = 'Houve um erro ao realizar uma operação aritmética'
except Exception:
    erro = 'Ocorreu um erro desconhecido'
else:
    erro = False
finally:
    if erro:
        print(erro)
    else:
        print(divisao)

bandas_metal = ['Iron Maiden', 'Angra', 'Slayer', 'Megadeth', 'Krisiun']
nova_banda = 'Caetano Veloso'
if nova_banda not in bandas_metal:
  raise InputError('{} não é metal!'.format(nova_banda))