"""
1. Write a function to take a list of numbers and an integer as input. Use list comprehension 
to produce a list where each member is raised to the power of the input integer.
"""

def rise_pow(arr: list, pow: int)->list:
    return [x**pow for x in arr]
arr=list(map(int, input("enter arr: ").split()))
pow=int(input("enter integer: "))

result=rise_pow(arr,pow)
print(result)