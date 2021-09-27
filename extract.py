import asyncio
from aiohttp import ClientSession
import json
import aiohttp

# Como a quantidade de páginas é muito grade, criei essa classe que utiliza metodos assincronos, o que deixa o processo muito mais rápido
class AsyncRequest:
    # attempts é o número de tentantivas em cada requisição em caso de erros e resultados indesejados
    def __init__(self, attempts=1):
        self.attempts=attempts
    
    def test_error(self, r):
        return 'numbers' in r

    def test_page(self, r):
        return len(r['numbers'])
    
    async def request(self, session, url):
        for i in range(self.attempts):
            try:
                async with session.get(url) as r:
                    r=await r.json()
                    if self.test_error(r):
                        self.results.append(r)
                        break
            except aiohttp.ClientConnectionError:
                print("Erro na conexão")
   

    async def request_many(self, urls):
        async with ClientSession() as session:
            tasks = [asyncio.create_task(self.request(session, url)) for url in urls]
            await asyncio.gather(*tasks)

    
    async def run_urls(self, urls):
        self.results=[]
        await self.request_many(urls)
        
    # each é a quantidade de páginas requisitadas por vês
    # init é a página inicial
    # limit é a quantidade máxma de páginas
    async def run_pages(self, url, init=1, each=1000, logs=True, limit=None):
        if not limit: 
            limit=float('inf')
        self.results=[]
        init=1
        while True:
            end = init+each
            urls=[url.format(i) for i in range(init, end) if i <= limit]
            await self.request_many(urls)
            if logs:
                print(f'init: {init} | end: {end} | results: {len(self.results)}', end='\r')
            if limit and end >= limit:
                break
            if not all([self.test_page(r) for r in self.results[each*(-1):]]):
                break
            init+=each



def extract():
    api=AsyncRequest(10)
    asyncio.run(api.run_pages('http://challenge.dienekes.com.br/api/numbers?page={}'))
    data=[i for j in [i['numbers'] for i in api.results] for i in j]
    data={'numbers':data}
    with open(r'data\raw_numbers.json', 'w') as o:
        json.dump(data, o)
    return data

if __name__=='__main__':
    extract()






