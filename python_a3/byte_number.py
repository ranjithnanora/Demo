"""
Write a function to read in 3 bytes of data from a 24-bit list and return a
tuple of 3 numbers. One for each byte.
"""

def binary_number(binary: list)->int:
    s=""
    for bit in binary:
        s+=str(bit)
    return int(s,2)

def byte_number(arr:list):
    return (binary_number(arr[0:8]), binary_number(arr[8:16]), binary_number(arr[16:24]))
   

print(byte_number([0,0,0,0,1,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,1,1]))