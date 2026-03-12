print("Hello world")
arr=[3,1,12,0,56,7,0,1,0,1]
i=0
n=len(arr)
while i < n and arr[i] != 0:
    i += 1

for index in range(i, n):
    if arr[index]!=0:
        arr[i]=arr[index]
        i+=1

for j in range(i, n):
    arr[j]=0

print(arr)