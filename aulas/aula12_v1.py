'''
Requests: HTTP for Humans
referencia: https://docs.python-requests.org/en/master/
'''


import requests as r

def informe_cep():
    return input('Digite o CEP do cliente: ')


def busca_cep(cep):
    url = 'https://viacep.com.br/ws/{}/json'.format(cep)
    resp = r.get(url)
    return resp


def imprime_endereco(resp):
    if resp.status_code == 200:
        dic = resp.json()
        print('Logradouro: ', dic['logradouro'])
        print('Bairro: ', dic['bairro'])
        print('Município: ', dic['localidade'])
        print('Estado: ', dic['uf'])
    else:
        print('CEP não encontrado')


if __name__ == '__main__':
    cep = informe_cep()
    resp = busca_cep(cep)
    imprime_endereco(resp)
