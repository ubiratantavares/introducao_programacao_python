def contador_letras(lista):
    contador = []
    for x in lista:
        qtd = len(x)
        contador.append(qtd)
    return contador

if __name__ == '__main__':
    lista = ['cachorro', 'gato']
    print(contador_letras(lista))