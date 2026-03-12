x=int(input("Enter value: "))
result=0
digit=(x>>7)&1
result=result|(digit<<7)
digit=(x>>11)&1
result=result|(digit<<11)
print(result)
