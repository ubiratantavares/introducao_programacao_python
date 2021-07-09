lista=[1, 10]

try:
    divisao = 10/0
except ZeroDivisionError:
    print('Não é possível realizar divisão por zero.')
except ArithmeticError:
    print('Erro ao tentar realizar a operação aritmética.')
except Exception as ex:
    print('Erro desconhecido. Erro: {}'.format(ex))
else:
    print(lista[0])
    
print('\n')


try:

    numero=lista[3]
except IndexError:
    print('Erro ao tentar um indice invalido da lista.')
except Exception as ex:
    print('Erro desconhecido. Erro: {}'.format(ex))

print('\n')

try:
    arquivo = open('teste.txt', 'r')
    #divisao = 10/0
    texto = arquivo.read()
    print(texto)
except ZeroDivisionError:
    print('Não é possível realizar divisão por zero.')
except ArithmeticError:
    print('Erro ao tentar realizar a operação aritmética.')
except Exception as ex:
    print('Erro desconhecido. Erro: {}'.format(ex))
finally:
    print('Fechando o arquivo...')
    arquivo.close()

