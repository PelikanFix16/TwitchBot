import re
import socket


import ast
import json
import multiprocessing as mp

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

channel = "mindrage"
msg = "i'm not a bot"
proc = []
output1 = mp.Queue()

for i in dic:
        username = i['username']
        passw = i['oauth']
        proc.append(mp.Process(target=send_message_proc,args=(output1,channel,username,passw,msg)))
for p in proc:
    p.start()
for p in proc:
    p.join()
