import subprocess
import requests
import re
import json
import multiprocessing as mp
import time

def request(q,ip):
        p = subprocess.Popen("nodejs mv.js", stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        p_status = p.wait()


        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
        }

        try:
            con = requests.get(output,headers=headers).content
            x = re.findall("https://\w.+.ts",con.decode("UTF-8"))
            while True:
                for i in x:
                    con1 = requests.get(i,headers=headers)
                    print(con1.status_code)
        except:
            print("Failed")
            return

with open("raw.txt") as f:
    lines = f.readlines()
def run():

    proc = []
    output1 = mp.Queue()
    while True:
        for i in lines:
            iP = i.replace("\n","")
            proc.append(mp.Process(target=request,args=(output1,iP)))

        for p in proc:
            p.start()

        for p in proc:
            p.join()

run()
