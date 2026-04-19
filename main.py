import subprocess
from ping3 import ping
from time import time

with open("ipwhitelist.txt", "r") as file:
    ip_lst = file.read().splitlines()
#print(ip_lst)

#ip_lst = ['8.8.8.8', '1.1.1.1', '5.5.5.4']

sp_start = time() 
for ip in ip_lst: 
    exitcode, output = subprocess.getstatusoutput(f'ping -c1 {ip}') 
    if exitcode == 0: 
        with open("results.txt", "a") as f:
            print(f'{ip} is up', file=f)
    # else:
    #     with open("results.txt", "a") as f:
    #         print(f'{ip} is down', file=f)
sp_total = time() - sp_start



ping_start = time() 
for ip in ip_lst: 
    if ping(ip): 
        with open("results.txt", "a") as f:
            print(f'{ip} is up', file=f)
    # else: 
    #     with open("results.txt", "a") as f:
    #         print(f'{ip} is down', file=f)
ping_total = time() - ping_start


