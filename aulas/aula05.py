# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 07:13:22 2020

@author: natar
"""

# Como organizar os dados em uma lista ou tupla e realizar operações com elas


lista = [1, 3, 5, 7]

lista_animal = ['cachorro', 'gato', 'elefante']

print(lista)

print(lista_animal[1])

for x in lista_animal:
    print(x)

soma = 0
for x in lista:
    soma += x

print(soma)

print(sum(lista))

print(max(lista))

print(min(lista))

print(min(lista_animal))

print(max(lista_animal))

if 'gato' in lista_animal:
    print('Lista contém animal')
else:
    print('Lista não contém animal')
    
if 'lobo' in lista_animal:
    print('Lista contém animal')
else:
    print('Lista não contém animal, mas será incluido.')
    lista_animal.append('lobo')
    print(lista_animal)

    
nova_lista = lista_animal * 3
print(nova_lista)

animal = lista_animal.pop()
print(animal)
print(lista_animal)

animal = lista_animal.pop(1)
print(animal)
print(lista_animal)

lista_animal.remove('elefante')
print(lista_animal)

lista = [12, 10, 7, 5]
lista.sort()
print(lista)

lista_animal = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']
lista_animal.sort()
print(lista_animal)

lista_animal.reverse()
print(lista_animal)

lista_animal[0] = 'macaco'
print(lista_animal)
# tupla é imutável

tupla = (1, 10, 12, 14)
print(tupla)

print(tupla[0])

# tupla[0] = 5

print(len(tupla))
print(len(lista))
print(len(lista_animal))

tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)

lista_numerica = list(tupla)
print(type(lista_numerica))
print(lista_numerica)

lista_numerica[0] = 100
print(lista_numerica)


lista_cores = ['azul', 'amarelo', 'vermelho', 'roxo']
lista_cores.reverse()
print(lista_cores)





