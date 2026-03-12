N=int(input(">"))
if N>0 and (N&(N-1)) == 0:
    print("Power of two")
else:
    print("Not a power of two")