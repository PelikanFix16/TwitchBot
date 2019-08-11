import subprocess
import requests
import re
import json
import multiprocessing as mp
import time


import threading
import asyncio
from proxybroker import Broker

proxiesList = []
count = 0

async def show(proxies):
    global count
    while True:
        proxy = await proxies.get()
        if proxy is None: break
        proxiesList.append(proxy.as_json()['types'][0]['type'].lower()+"://"+proxy.as_json()['host']+":"+str(proxy.as_json()["port"]))
        print(proxy)
        count+=1
        print(count)


proxies = asyncio.Queue()
broker = Broker(proxies)
tasks = asyncio.gather(
    broker.find(types=['HTTPS','HTTP'], limit=700),
    show(proxies))

loop = asyncio.get_event_loop()
loop.run_until_complete(tasks)







def request(q,ip):
    while True:
        p = subprocess.Popen("nodejs mv.js", stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        p_status = p.wait()
        print(ip)
        proxies = {
          "https": ip,
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
        }
        try:

            con = requests.get(output,headers=headers,proxies=proxies).content
            x = re.findall("https://\w.+.ts",con.decode("UTF-8"))
            for i in x:
                con1 = requests.get(i,headers=headers,proxies=proxies)
                print(con1.status_code)
        except Exception as e:
            print("failed")
            return








def run(list):

    proc = []
    output1 = mp.Queue()
    while True:
        for i in list:
            proc.append(mp.Process(target=request,args=(output1,i)))

        for p in proc:
            p.start()

        for p in proc:
            p.join()


halfProxies1 = proxiesList[0:175]
halfProxies2 = proxiesList[175:350]
halfProxies3 = proxiesList[350:525]
halfProxies4 = proxiesList[525:700]

print("Start 1 thread")
threading.Thread(target=run,args=[halfProxies1]).start()
print("Start 2 thread")
threading.Thread(target=run,args=[halfProxies2]).start()
print("Start 3 thread")
threading.Thread(target=run,args=[halfProxies3]).start()
print("Start 4 thread")
threading.Thread(target=run,args=[halfProxies4]).start()
