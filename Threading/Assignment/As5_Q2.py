import threading
import time

"""
2.
Implement a Python program that uses a thread to calculate the sum of a list of numbers. 
The main thread should wait for the calculation to complete and then print the result.
"""

class CalculateSum(threading.Thread):
    def __init__(self,arr):
        self.arr=arr
        self.result=0
        super().__init__()

    def run(self):
        for ele in self.arr:
            self.result+=ele

t1=CalculateSum([3,4,5,6,7])
t2=CalculateSum([1,1,1,1])
t1.start()
t2.start()

t2.join()
t1.join()
print(t1.result)
print(t2.result)