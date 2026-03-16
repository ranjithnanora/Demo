import heapq
arr=[5,3,2,1,2,2,1,3,3,5]
arr.sort()
print(arr)
q=[]

i=0
for ele in arr:
    q.append(ele)
    q.sort()
    i+=1
    change=True
    j = 0
    while j < len(q) - 1:
        if q[j] == q[j + 1]:
            change = True
            q[j] += q[j + 1]
            q.pop(j + 1)
        j += 1

    print(q)
print(q)


