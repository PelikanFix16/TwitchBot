import os
command = "python3 account_create.py"
import time
while True:
    for i in range(13):
        os.system("gnome-terminal -e 'bash -c \""+command+";bash\"'")
    time.sleep(2*55)
