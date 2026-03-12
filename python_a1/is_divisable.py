"""
1. Write a script to declare two numbers. Print True if the first number is divisible by second
number. Print false otherwise.

"""
import sys
def is_divisable(x: int, y: int) -> bool:
    return x%y==0

x=int(input("Enter number 1: "))
y=int(input("Enter number 2: "))

if(y==0):
    print("divisor can't be Zero")
    sys.exit(1)

if(is_divisable(x,y)):
    print(f"{x} is divisable by {y}")
else:
    print(f"{x} is not divisable by {y}")
