import test
import threading
from time import sleep
from datetime import datetime
now = datetime.now()
with open("runner.txt","w") as f:
    f.write(f"run in :\nminute:{now.minute}\nsecond:{now.second}")
for count in range(10):
    with open("test.txt","a") as f:
        f.write(f"\n run new thread : {count}\nnumber send packet : {test.i}")
    threading.Thread(target=test.tarrer,args=("104.18.147.40",)).start()
    sleep(5)
    
print("finish all code")