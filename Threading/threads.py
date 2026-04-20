import time
import threading


index=0
def print_hello(num_of_times):
    global index
    time.sleep(0.4)
    for _ in range(num_of_times):
        time.sleep(0.3)
        mylock.acquire()
        index+=1
        temp_index=index
        mylock.release()
        print(temp_index," : ",  threading.current_thread().name)

def print_name(name, num_of_times):
    global index
    for _ in range(num_of_times):
        time.sleep(0.3)
        mylock.acquire()
        index += 1
        temp_index = index
        mylock.release()
        print(temp_index, " : ", threading.current_thread().name)


t1=threading.Thread(target=print_hello, args=(5,))
t2=threading.Thread(target=print_name, args=("ran",5))
mylock=threading.Lock()
t1.start()
t2.start()

print(threading.current_thread().name)
t1.join()
t2.join()


class CalculateSum(threading.Thread):
    def __init__(self, arr):
        self.arr = arr
        self.result = 0
        super().__init__()


    def run(self):
        for ele in self.arr:
            self.result += ele
            time.sleep(0.2)

t1=CalculateSum([3,4,5,6,7])
t2=CalculateSum([1,1,1,1])
t1.start()
t2.start()

t2.join()
t1.join()
print(t1.result)
print(t2.result)

print("=====End========")

