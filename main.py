#import subprocess
import traceback
from ping3 import ping
from time import time

try:
    with open("ipwhitelist.txt", "r") as file:
        ip_lst = file.read().splitlines()

    # sp_start = time() 
    # for ip in ip_lst:
    #     #print(f"Проверено {count} из {len(ip_lst)}")   
    #     exitcode, output = subprocess.getstatusoutput(f'ping -c1 {ip}') 
    #     if exitcode == 0: 
    #         with open("results.txt", "a") as f:
    #             print(f'{ip} is up', file=f)
            
    #     # else:
    #     #     with open("results.txt", "a") as f:
    #     #         print(f'{ip} is down', file=f)
    #sp_total = time() - sp_start

    ping_start = time() 
    for count, ip in enumerate(ip_lst, start =1):
        print(f"Проверено {count} из {len(ip_lst)}")
        if ping(ip): 
            with open("results.txt", "a") as f:
                print(f'{ip} is up', file=f)
        # else: 
        #     with open("results.txt", "a") as f:
        #         print(f'{ip} is down', file=f)
    ping_total = time() - ping_start

    with open("time.txt", "w") as f:
    #    print(f'{sp_total = }', file =f) # subprocess.getstatusoutput общее время 
        print(f'{ping_total = }', file =f) # ping общее время
except Exception:
    traceback.print_exc()
    input("Ошибка, нажмите enter для выхода")

input("Завершено. Нажмите Enter, чтобы выйти...")

