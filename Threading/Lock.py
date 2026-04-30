import threading
import time

lock= threading.Lock()
counter=0

def counter_function():
    global counter
    print(threading.current_thread().name)
    time.sleep(0.2)
    lock.acquire()
    counter+=1
    print(f"counter: {counter} [{threading.current_thread().name}]")
    lock.release()

threads=[]
for i in range(5):
    t=threading.Thread(target=counter_function)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print(f"Main thread counter: {counter}")



#No blocking
def func():
    if lock.acquire(blocking=False):
        print("lock acquired")
        lock.release()
    else:
        print("unable to lock")





