import threading
import time

"""
3.
Write a Python program that demonstrates the use of a thread lock to prevent race conditions. 
Create two threads that both increment a shared counter variable 1000 times. 
Use a lock to ensure that the final value of the counter is correct
"""

shared_counter=0
Lock=threading.Lock()
def counter():
    global shared_counter
    for i in range(1000):
        Lock.acquire()
        shared_counter+=1
        Lock.release()


t1=threading.Thread(target=counter())
t2=threading.Thread(target=counter())
t1.start()
t2.start()
t1.join()
t2.join()

print(shared_counter)

