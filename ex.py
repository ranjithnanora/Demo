x=[5,6,7,8,7]
mp={}
m=map(lambda x: {mp.update({x:0})} , x)

print(mp)

tuple(m)

print(mp)

def func(arr=[]):
    arr.append(1)
    return arr

print(func())
print(func())
print(func())



x = 10
def outer():
    x=20
    def inner():
        print(x)
    inner()

outer()

print("hello world")

for i in range(100):
    print(i)

# arr=["eat","tea","tan","ate","nat","bat"]
# mp={}
# for val in arr:
#     a=list(val)
#     a.sort()
#     key=str(a)
#     if key not in mp:
#         mp[key]=[]
#     mp[key].append(val)
# for value in mp.values():
#     print(value)

