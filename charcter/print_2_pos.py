arr=['a','b','c','d','e','z']
for c in arr:
    val=ord(c)
    if(val<125):
        print(chr(val+2))


    