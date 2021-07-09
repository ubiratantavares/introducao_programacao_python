contador_letras = lambda lista: [len(x) for x in lista]

soma = lambda a, b: a+b
subtracao = lambda a, b: a-b

calculadora = {'soma': lambda a, b:a+b,
               'subtracao': lambda a, b: a-b,
               'multiplicacao': lambda a, b: a*b,
               'divisao': lambda a, b: a/b}

if __name__ == '__main__':
    lista = ['cachorro', 'gato', 'elefante']
    print(contador_letras(lista))
    print(soma(5, 10))    
    print(subtracao(5, 10))
    
    print(type(calculadora))
    
    soma2 = calculadora['soma']
    print(type(soma2))
    print(soma2(5, 10)) 