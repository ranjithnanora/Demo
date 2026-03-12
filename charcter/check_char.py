arr=['A','a','1','B','2','d']
for c in arr:
    val=ord(c)
    if(val>=65 and val<=90):
        print("Capital")
    elif(val>=97 and val<=122):
        print("Small")
    else:
        print("Not a letter")