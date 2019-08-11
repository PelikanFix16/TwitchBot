import os
command = "python3 test.py"

for i in range(3):
    os.system("gnome-terminal -e 'bash -c \""+command+";bash\"'")
