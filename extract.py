import asyncio
from aiohttp import ClientSession
import json

# Como a quantidade de páginas é muito grade, criei essa classe que utiliza metodos assincronos, o que deixa o processo muito mais rápido
class RequestAPI:
    async def request_api(self, session, url):
        # faz 10 tentativas para o caso da resposta vir com erro
        for i in range(10):
            async with session.get(url) as result:
                r=await result.json()
                if 'numbers' in r:
                    if r['numbers']:
                        self.results+=r['numbers']
                    else:
                        self.finish=1  
                    break

    async def request_all(self, urls):
        async with ClientSession() as session:
            tasks = []
            for url in urls:
                task = asyncio.ensure_future(self.request_api(session, url))
                tasks.append(task)
            await asyncio.gather(*tasks)

    def run(self):
        self.results=[]
        self.finish = 0
        ini=1
        while not self.finish:
            fim=ini+1000
            urls=['http://challenge.dienekes.com.br/api/numbers?page='+str(page) for page in range(ini, fim)]

            asyncio.set_event_loop(asyncio.SelectorEventLoop())
            asyncio.get_event_loop().run_until_complete(self.request_all(urls))

            print(f'{ini} | {fim} | {len(self.results)}', end='\r')
            ini+=1000
            

    def to_json(self):
        data={'numbers':self.results}
        with open(r'data\raw_numbers.json', 'w') as o:
            json.dump(data, o)


