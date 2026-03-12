arr=['a','b','c','d','e','z']
for c in arr:
    val=ord(c)
    if(val>=97 and val<=122):
        print(chr(val-32))
    