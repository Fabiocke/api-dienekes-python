from transform import sorter
from extract import AsyncRequest
import asyncio
import time
import requests

def teste_funcao_sorter():
    lista = [10,9,7,4,2,8,5,6,0,1,3]

    assert sorter(lista)==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    return 'A função sorter funcionou.\n'


def teste_primeira_pagina_api():
    r=requests.get('http://challenge.dienekes.com.br/api/numbers?page=1')
    assert r.status_code==200
    assert 'numbers' in r.json()
    assert r.json()['numbers']

    return 'A primeira página da api funcionando normalmente.\n'

def teste_extraçao_api():
    inicio = time.time()
    api=AsyncRequest(10)
    asyncio.run(api.run_pages('http://challenge.dienekes.com.br/api/numbers?page={}', each=1000, limit=1000))
    fim = time.time()

    assert all([len(i['numbers'])==100 for i in api.results if i['numbers']])
    assert inicio-fim<5

    return 'A função de extração de 1000 páginas rodou corretamente em menos de 5 de segundos.\n\nTodas as páginas extraídas vieram com 100 números.'

if __name__=='__main__':
    print(teste_funcao_sorter())
    print(teste_primeira_pagina_api())
    print(teste_extraçao_api())

