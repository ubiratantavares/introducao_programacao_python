# -*- coding: utf-8 -*-

# Construindo métodos, funções e classes em Python

class Televisao:
        
    def __init__(self):
        self.ligada = False
        self.canal = 2
        self.volume = 0
        
    def getLigada(self):
        return self.ligada
    
    def getCanal(self):
        return self.canal

    def getVolume(self):
        return self.volume

    def ligar(self):
        self.ligada = True
        
    def desligar(self):
        self.ligada = False
            
    def aumentarCanal(self):
        if self.ligada and self.canal < 400:
            self.canal += 1
            
    def diminuirCanal(self):
        if self.ligada and self.canal > 2:
                self.canal -= 1
                
    def aumentarVolume(self):
        if self.ligada and self.volume < 100:
            self.volume += 1
            
    def diminuirVolume(self):
        if self.ligada and self.volume > 0:
            self.volume -= 1    
        

def comandos():
    tv = Televisao()
    print('Canal:', tv.getCanal())
    print('Volume:', tv.getVolume())
    print('\n')
    
    tv.aumentarCanal()
    tv.aumentarCanal()
    tv.aumentarCanal()
    
    print('Canal:', tv.getCanal())
    print('Volume:', tv.getVolume())
    print('\n')
    
    tv.aumentarVolume()
    tv.aumentarVolume()
    
    print('Canal:', tv.getCanal())
    print('Volume:', tv.getVolume())
    print('\n')
    
    tv.diminuirCanal()    
    tv.diminuirVolume()
    
    print('Canal:', tv.getCanal())
    print('Volume:', tv.getVolume())
    print('\n')

def main():
    comandos()    
    
if __name__ == '__main__':
    main()
