"""
5. Define a decimal number. Convert to binary and print. 
Do not use any built-in python function to do this. You must write a script to do all logic.
"""

def decimal_binary(num: int) -> str:
    result=""
    while(num>0):
        digit= num&1
        result+=str(digit)
        num=num>>1
    
    return result[::-1]

num=int(input("number: "))
print(decimal_binary(num))