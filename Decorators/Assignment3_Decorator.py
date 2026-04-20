print("==="*5, 1, "==="*5)
"""
1. Write a decorator function that logs the execution time of a function. 
Apply this decorator to a function that calculates the factorial of a number.
"""
import time
def cal_time_taken(func):
    def wrapper(n):
        start_time=time.perf_counter()
        result=func(n)
        end_time=time.perf_counter()
        duration=end_time-start_time
        print(f"Function '{func.__name__}' executed in {duration:8f} seconds")
        return result
    return wrapper

@cal_time_taken
def factorial(n):
    result=1
    for i in range(2,n+1):
        result*=i
    return result


print(factorial(10))
print(factorial(20))

"""
2.  Create a decorator named repeat that takes an argument num_times 
and repeats the execution of the decorated function num_times times. 
Apply this decorator to a function named greet that prints “Greetings!”.
"""
print("==="*5, 2, "==="*5)
def repeat_decorator(func):
    def wrapper(n):
        for _ in range(n):
            func()
    return wrapper

@repeat_decorator
def greet():
    print("Greetings!")

greet(3)

"""
3.  Implement a class decorator named CountCalls that counts the number of 
times a function is called. Apply this decorator to a function named say_goodbye 
that prints “Goodbye!” and demonstrate its usage.
"""

print("==="*5, 3, "==="*5)

class MyClassDecorator:
    def __init__(self,func):
        self.call_count=0
        self.func=func

    def __call__(self):
        self.call_count+=1
        self.func()

@MyClassDecorator
def say_goodbye():
    print("Goodbye!")


say_goodbye()
say_goodbye()
say_goodbye()
print("Total call: ",say_goodbye.call_count)

"""
4.  Implement two decorators: one that converts the output of a function 
to uppercase and another that reverses the string. Apply both decorators 
to a function that returns a greeting message and observe the order of execution.
"""
print("==="*5, 4, "==="*5)

def reverse_string(func):
    def wrapper():
        string=func()
        print(string[::-1])
        return string
    return wrapper

def upper_string(func):
    def wrapper():
        string=func()
        print(string.upper())
        return string
    return wrapper

@reverse_string
@upper_string
def greet():
    return "Greetings!"

print(greet())

print("==="*5, "END", "==="*5)
