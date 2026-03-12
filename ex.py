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