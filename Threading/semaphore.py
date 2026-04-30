import threading
import time

semLock=threading.Semaphore(3)
def print_function():
    semLock.acquire()
    print(threading.current_thread().name)
    time.sleep(3)
    semLock.release()

threads=[]
for i in range(5):
    t=threading.Thread(target=print_function)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print(f"Main thread")
