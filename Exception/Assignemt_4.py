"""
1. Write a function that takes a list of numbers and returns their average.
Use exception handling to manage cases where the list is empty or contains
non-numeric values.
"""
from io import UnsupportedOperation

print("\n","==="*5,1,"==="*5)
def find_average(arr):
    arr_len = len(arr)
    total = 0
    for ele in arr:
        total += ele

    return total / arr_len

try:
    avg = find_average([1,2,3,4,5])
    print(avg)

    avg2 = find_average([1, 2, "3", 4, 5])
    print(avg)
except ZeroDivisionError :
    print("minimum 1 element Array is required")

except TypeError:
    print("element in arr can't be str")

except Exception as E:
    print(E)

"""
2. Define a custom exception called NegativeNumberError. 
Write a function that raises this exception if a negative number is passed to it. 
Handle this exception gracefully in your code.

"""
print("\n","==="*5,2,"==="*5)

class NegativeNumberError(Exception):
    def __init__(self):
        super().__init__("can't pass negative number")


def function_print_number(num):
    if num<0:
        raise NegativeNumberError

    print(num)

try:
    function_print_number(5)
    function_print_number(-1)

except NegativeNumberError as e:
    print(e)

"""
3. Create a function that reads a file and prints its content. 
Use nested exception handling to manage potential errors such as 
the file not existing, 
permission issues, and any other unforeseen errors.
"""
print("\n","==="*5,3,"==="*5)

def filewrite(filepath, permission):
    try:
        with open(filepath, permission) as file:
            try:
                file.write("Hello user")
            except UnsupportedOperation:
                print("Unsupported operation")
            else:
                print("Completed")

    except FileNotFoundError:
        print(f"No file found in {filepath}")

    except PermissionError:
        print("required write permission")

    except Exception as e:
        print(e)



filewrite("assignment4", "r")
filewrite("assi_ex_2", "r")
filewrite("ass_ex_3", "w")

print("\n","==="*5,"END","==="*5)