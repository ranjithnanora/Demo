X=int(input("first number: "))
Y=int(input("Second number: "))

mask = 255 << 8

result = (X & ~mask) | (Y & mask)
print(result)