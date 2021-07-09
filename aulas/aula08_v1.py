from aula07_v4 import Televisao
from aula07_v1 import Calculadora
from aula08_v2 import contador_letras

if __name__ == '__main__':
    tv = Televisao()
    print(tv.getLigada())
    
    calculadora = Calculadora(5, 10)
    print(calculadora.soma())
    
    lista = ['cachorro', 'gato', 'elefante']
    print(contador_letras(lista))