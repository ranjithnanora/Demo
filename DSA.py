from collections import defaultdict
arr=[1,1,2,5,3,3,6,12]

mp=defaultdict(int)
for ele in arr:
    mp[ele]+=1

change=True
while change:
    change=False
    new_mp=defaultdict(int)
    for key,value in mp.items():
        if value>1:
            new_mp[key*value]+=1
            change=True
        else:
            new_mp[key]+=value

    mp=new_mp.copy()

result=[]
for key in mp.keys():
    result.append(key)

print(result)


