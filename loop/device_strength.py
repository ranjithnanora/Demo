register_val=int(input("register value: "))
mask=0x03
register_val=register_val>>1
if((register_val&mask)==0):
    print("medium")
elif((register_val&mask)==1):
    print("low")
elif((register_val&mask)==2):
    print("high") 
else:
    print("off")