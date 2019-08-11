import asyncio
from proxybroker import Broker

proxiesList = []

async def show(proxies):
    while True:
        proxy = await proxies.get()
        if proxy is None: break
        proxiesList.append(proxy.as_json()['host']+":"+str(proxy.as_json()["port"]))
        print(proxy)


proxies = asyncio.Queue()
broker = Broker(proxies)
tasks = asyncio.gather(
    broker.find(types=['HTTPS'], limit=100),
    show(proxies))

loop = asyncio.get_event_loop()
loop.run_until_complete(tasks)

print(len(proxiesList))
