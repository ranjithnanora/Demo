# arr=[3,1,12,0,56,7,0,1,0,1]
# i=0
# n=len(arr)
# while i < n and arr[i] != 0:
#     i += 1
#
# for index in range(i, n):
#     if arr[index]!=0:
#         arr[i]=arr[index]
#         i+=1
#
# for j in range(i, n):
#     arr[j]=0
#
# print(arr)
#
# arr=[1,2,3,4,5,6,7,8,9]
# res=list(map(lambda x: x+(x%2==0), arr))
# print(res)
from collections import defaultdict


def func(name, age, **kwargs):
    print(name)
    print(age)
    print(kwargs["gender"])
    print(kwargs.get("location","not provided"))
details=dict()
details["gender"]="male"
details["address"]="chennai"
func("ram", 12, **details)