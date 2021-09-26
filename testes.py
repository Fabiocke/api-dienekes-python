from transform import sorter, extract
import time
import requests

def teste_funcao_sorter():
    lista = [10,9,7,4,2,8,5,6,0,1,3]

    assert sorter(lista)==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    return 'Função sorter funcionou'


def teste_primeira_pagina_api():
    r=requests.get('http://challenge.dienekes.com.br/api/numbers?page=1')
    assert r.status_code==200
    assert 'numbers' in r.json()
    assert r.json()['numbers']

    return 'Primeira página da api funcionando normalmente'

def teste_extraçao_api():
    inicio = time.time()
    results=extract()
    fim = time.time()

    assert len(results)
    assert inicio-fim<4

    return 'Função de extração rodou corretamente em menos de 4 minutos'

if __name__=='__main__':
    print(teste_funcao_sorter())
    print(teste_primeira_pagina_api())
    print(teste_extraçao_api())

