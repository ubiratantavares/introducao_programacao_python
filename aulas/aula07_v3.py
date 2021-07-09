# -*- coding: utf-8 -*-

# Construindo métodos, funções e classes em Python

class Calculadora:
        
    def soma(self, a, b):
        return a + b
    
    def subtracao(self, a, b):
        return a - b
    
    def multiplicacao(self, a, b):
        return a * b
    
    def divisao(self, a, b):
        return a / b


if __name__ == '__main__':
    c = Calculadora()
    a = 10
    b = 2
    print('Soma:', c.soma(a, b))
    print('Subtração:', c.subtracao(a, b))
    print('Multiplicação:', c.multiplicacao(a, b))
    print('Divisão:', c.divisao(a, b))

