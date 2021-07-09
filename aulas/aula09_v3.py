# -*- coding: utf-8 -*-

def escrever_arquivo(texto):   
    diretorio = 'G:/DIO/introducao a programacao com python/teste.txt'
    arquivo = open(diretorio, 'w')
    arquivo.write(texto)
    arquivo.close()
    
def atualizar_arquivo(texto):
    arquivo = open('teste.txt', 'a')
    arquivo.write(texto)
    arquivo.close()
    
def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)
    
if __name__ == '__main__':
    #escrever_arquivo('Primeira linha.\n')
    #atualizar_arquivo('Segunda linha.\n')
    #atualizar_arquivo('Terceira linha.\n')
    ler_arquivo('teste.txt')
