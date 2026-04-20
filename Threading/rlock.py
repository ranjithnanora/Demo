import threading
import time

rlock=threading.RLock() #reentrant lock

def function1():
    print("Entered function 1 !!")
    rlock.acquire()
    print("inside func1 rlock")
    time.sleep(0.2)
    rlock.release()
    print("exit rlock func1")

def function2():
    print("Entered function 2 !!")
    rlock.acquire()
    print("inside func2 rlock")
    time.sleep(5)
    function1()
    #function2()
    rlock.release()
    print("exit rlock func2")

t1=threading.Thread(target=function2)
t2=threading.Thread(target=function1)
t1.start()
t2.start()

t1.join()
t2.join()
print("main thread")