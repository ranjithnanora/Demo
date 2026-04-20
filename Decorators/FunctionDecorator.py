# def decorator(func1):
#     def wrapper():
#         print("after this execute the function ")
#         func1()
#         return
#     return wrapper
#
# @decorator
# def func():
#     print("executing")
#     return
#
# @decorator
# def fuc2():
#     print("i am different function")
#
# func()
# fuc2()
#
# def repeat(num_times):
#     def decorator_repeat(func):
#         def wrapper(*args, ** kwargs):
#             for _ in range(num_times):
#                 result = func(*args, ** kwargs)
#             return result
#         return wrapper
#     return decorator_repeat
#
#
# @repeat(3)
# def greet(name):
#     print(f"Hello, {name}!")
#
# # Calling the decorated function
# greet("Alice")

def dec1(func):
    def wrapper():
        print("decoratore 1")
        func()
    return wrapper

def dec2(name):
    def dec_inner(func):
        def wrapper():
            print(name)
            print("decorator 2")
            func(name)
            return func
        return wrapper
    return dec_inner

@dec1
@dec2("Admin")  #dec1(dec2("admin"))(func)
def func(name):
    print(f"task completed {name}")


func()

from functools import wraps
def decorator_with_wrap(f):

    def before():
        print("i am before logic")

    def after():
        print("i am after logic")
    @wraps(f)
    def wrapper():
        before()
        f()
        after()
        return
    return wrapper


@decorator_with_wrap
def print_hello():
    print("hello")

print(print_hello.__name__)
print_hello()
