# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 07:45:00 2020

@author: natar
"""

# Organizando conjuntos e subconjuntos de elementos em Python

c = {1, 2, 3, 4}
print(type(c))
print(c)

c = {1, 2, 3, 4, 2, 4}
print(type(c))
print(c)

c.add(5)
print(c)

c.discard(2)
print(c)

c1 = {1, 2, 3, 4, 5}
c2 = {5, 6, 7, 8}

uniao = c1.union(c2)
print(uniao)

intersecao = c1.intersection(c2)
print(intersecao)

dif_c1c2 = c1.difference(c2)
print(dif_c1c2)

dif_c2c1 = c2.difference(c1)
print(dif_c2c1)

dif_simetrica = c1.symmetric_difference(c2)
print(dif_simetrica)

dif_simetrica = uniao - intersecao
print(dif_simetrica)

valor = 5 in c1 # elemento 5 pertence a c1
print(valor)

valor = 5 in c2 # elemento 5 não pertence a c2
print(valor)

a = {1, 2, 3}
b = {1, 2, 3, 4, 5}

valor = a.issubset(b)  # a está contido em b
print(valor)

valor = b.issubset(a) # b não está contido em a
print(valor)

valor = b.issuperset(a) # b contém a
print(valor)
 
valor = a.issuperset(b) # a não contém b
print(valor)

lista_animais = ['cachorro', 'cachorro', 'gato', 'gato', 'elefante']

conjunto_animais = set(lista_animais)
print(conjunto_animais)

lista_animais = list(conjunto_animais)
print(lista_animais)