import test
import threading
from random import uniform
from time import sleep
a = 0
while True:
    threading.Thread(target=test.tarrer,args=("104.18.147.40",)).start()
    threading.Thread(target=test.tarrer,args=("104.18.146.40",)).start()
    sleep(uniform(1,2.5))
    if a == 100:
        break
    a += 1 
print(f"finish all code\nsended packet:{test.i}")

