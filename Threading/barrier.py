import threading
import time

barrier=threading.Barrier(2) #when two thread hit barrier it will resume execution

def execution(name, sleeptime):
    print(f"{name} entered execution")
    for i in range(3):
        time.sleep(sleeptime)
        print(f"{name} waiting in barrier\n")
        barrier.wait()
        print(f"{name} resumed execution\n")

t1=threading.Thread(target=execution,args=("bot1",3))
t2=threading.Thread(target=execution, args=("bot2",5))

t1.start()
t2.start()
t1.join()
t2.join()