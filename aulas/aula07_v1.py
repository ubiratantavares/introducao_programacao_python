# -*- coding: utf-8 -*-

# Construindo métodos, funções e classes em Python

class Calculadora:
    
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def soma(self):
        return self.a + self.b
    
    def subtracao(self):
        return self.a - self.b
    
    def multiplicacao(self):
        return self.a * self.b
    
    def divisao(self):
        return self.a / self.b


c = Calculadora(10, 2)
print('Soma:', c.soma())
print('Subtração:', c.subtracao())
print('Multiplicação:', c.multiplicacao())
print('Divisão:', c.divisao())

