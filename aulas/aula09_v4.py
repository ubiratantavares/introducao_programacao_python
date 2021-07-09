# -*- coding: utf-8 -*-

def escrever_arquivo(texto):   
    diretorio = 'G:/DIO/introducao a programacao com python/teste.txt'
    arquivo = open(diretorio, 'w')
    arquivo.write(texto)
    arquivo.close()
    
def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()
    
def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)
    
if __name__ == '__main__':
    aluno = 'Rafael,10,10,5,5\n'
    atualizar_arquivo('notas.txt', aluno)
    aluno = 'Felipe,7,8,5,6\n'
    atualizar_arquivo('notas.txt', aluno)
    aluno = 'Galleani,7,8,5,6\n'
    atualizar_arquivo('notas.txt', aluno)
    aluno = 'Cesar,7,9,3,8\n'
    atualizar_arquivo('notas.txt', aluno)
