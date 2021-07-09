import requests as r


def retorna_response(url):
    response = r.get(url)
    return response.text


if __name__ == '__main__':
    response = retorna_response('http://cnpj.info/15301370000136')
    print(response)