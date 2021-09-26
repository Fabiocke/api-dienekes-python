
from extract import RequestAPI
import json
import os

# Função baseada no algorítimo QuickSort
def sorter(lista):
    if not len(lista): 
        return lista
    pivo = lista[0]
    return sorter([i for i in lista if i < pivo]) + [i for i in lista if i == pivo] + sorter([i for i in lista if i > pivo])  


def extract():
    api=RequestAPI()
    api.run()
    api.to_json()
    return api.results


def to_json_order(data):
    with open(r'data\order_numbers.json', 'w') as o:
        json.dump(data, o)

# Se o parâmetro extrair for True, a busca na api será refeita, senão retornará os dados salvos no raw_numbers.json, se o arquivo não existir é gerado
def get_order_numbers(update=True):
    if update:
        numbers=extract()
        data = sorter(numbers)
        data={'numbers': data}
        to_json_order(data)
    elif os.path.isfile(r'data\order_numbers.json'):
        data=open(r'data\order_numbers.json', 'r').read()
        data = json.loads(data)
    else:
        data=get_order_numbers(True)
    return data



