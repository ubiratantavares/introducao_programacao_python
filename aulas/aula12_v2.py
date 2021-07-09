import requests as r


def busca_pokemon(pokemon):
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon)
    resp = r.get(url)
    return resp


def imprime_pokemon(resp):
    if resp.status_code == 200:
        dados = resp.json()
        print(dados['sprites']['front_shiny'])
    else:
        print('Não encontrado')


if __name__ == '__main__':
    resp = busca_pokemon('pikachu')
    imprime_pokemon(resp)
