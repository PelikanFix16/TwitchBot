import re
import socket


import ast
import json
import multiprocessing as mp
import random
import time
lines = 0

with open('dict.txt','r') as f:
    lines = f.readlines()

dic = []


for i in range(len(lines)):
    obj = ast.literal_eval(lines[i])
    dic.append(obj)



def send_message_proc(q,channel,nick,passw,msg):
    HOST = "irc.twitch.tv"
    PORT = 6667
    CHAN = "#"+channel
    NICK = nick
    PASS = passw


    con = socket.socket()
    con.connect((HOST, PORT))
    con.send(bytes('PASS %s\r\n' % PASS, 'UTF-8'))
    con.send(bytes('NICK %s\r\n' % NICK, 'UTF-8'))
    con.send(bytes('JOIN %s\r\n' % CHAN, 'UTF-8'))
    con.send(bytes('PRIVMSG %s :%s\r\n' % (CHAN, msg), 'UTF-8'))

channel = "dullciaa"

msg = ["zrób śmigło pls","lubisz disa ? ","siema","elo","ale fajny stream","ile już streamujesz","co dzisiaj robisz ?","D:","xD","XD","+1","?","??","???","monkaS","residentsleeper","PogChamp","mmm szparka","JD"," TriHard TriHard JAJAJE KOKO DŻAMBO","POLSKA GUROM BloodTrail POLSKA GUROM BloodTrail POLSKA GUROM BloodTrail POLSKA GUROM BloodTrail POLSKA GUROM BloodTrail POLSKA GUROM BloodTrail","S Z M A T A peepoWTF","U mnie minęłą","burza monkaW","siema ile mam !iq","ALE NUDY ResidentSleeper","TANCZ Z NAMI JAK MALPA TriDance TANCZ Z NAMI JAK MALPA TriDance TANCZ Z NAMI JAK MALPA TriDance TANCZ Z NAMI JAK MALPA TriDance","OK","PogU","RarePope RarePope RarePope RarePope RarePope RarePope RarePope RarePope RarePope RarePope RarePope RarePope RarePope RarePope"]
#msg = ["Jest tutaj miejsce dla 50 botów ? BloodTrail"]
proc = []
output1 = mp.Queue()

for i in dic:
        username = i['username']
        passw = i['oauth']
        send_message_proc(output1,channel,username,passw,random.choice(msg))
        #proc.append(mp.Process(target=send_message_proc,args=(output1,channel,username,passw,random.choice(msg))))
        time.sleep(5)

'''
for p in proc:
    p.start()
for p in proc:
    p.join()

'''
