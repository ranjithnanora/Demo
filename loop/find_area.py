option=int(input("Enter option (0:Square, 1:Triangle, 2:Rectangle): "))
if(option==0):
    print("Square")
    a=int(input("Enter side: "))
    print("area of square: ", a*a)
elif(option==1):
    print("Triangle")
    base=int(input("base: "))
    height=int(input("height: "))
    print("area of triangle: ", (1/2)*base*height)
elif(option==2):
    print("Rectangle")
    l=int(input("Length: "))
    b=int(input("breath: "))
    print("area of Rectangle: ",l*b)
else:
    print("invalid input")