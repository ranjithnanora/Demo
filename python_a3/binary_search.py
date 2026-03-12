"""
Write a function to do binary search over an ordered list.
"""

def binarySearch(arr, target):
    low=0
    high=len(arr)-1
    mid=0
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]==target):
            print(f"Target founded at index {mid}")
            return
        elif(arr[mid]<target):
            low=mid+1
        else:
            high=mid-1
    print(f"Target not founded. closest number index is {mid}")

arrays=[[1,2,3,4,6,7,8,9,10],[1,2,3,4,5,6,7,8,9,10],[1,2,3,4,5,6,7,8,9,10]]
targets=[5,9,12]
for i in range(len(arrays)):
    binarySearch(arrays[i],targets[i])