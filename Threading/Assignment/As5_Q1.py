import threading
import time
"""
1.
Write a Python program that creates two threads.
One thread should print numbers from 1 to 5, and the other thread should print numbers from 6 to 10.
Ensure that the threads run concurrently.
"""

def print_range(start,end):
    for i in range(start, end+1):
        print(threading.current_thread().name," : ",i)
        time.sleep(0.2)


t1=threading.Thread(target=print_range, args=(1,5))
t2=threading.Thread(target=print_range, args=(6,10))
t1.start()
t2.start()
