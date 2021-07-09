# https://receitaws.com.br/api


import requests as r


def busca_cnpj(cnpj):
    url = 'https://www.receitaws.com.br/v1/cnpj/{}'.format(cnpj)
    resp = r.get(url)
    return resp


def imprime_cnpj(resp):
    if resp.status_code == 200:
        dados = resp.json()
        print(dados)
    else:
        print('CEP não encontrado')


if __name__ == '__main__':
    resp = busca_cnpj('15301370000136')
    imprime_cnpj(resp)
