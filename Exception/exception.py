try:
    num1=int(input("num1: "))
    num2=int(input("num2: "))
    result=num1/num2
    print(f"Result: {result}")
    arr = [0]
    index=int(input("i: "))
    print(arr[index])
except ValueError :
    print("enter numbers")
except ZeroDivisionError:
    print("divisor can't be zero")
except Exception as e:
    print(e)
else:
    print("I am else")
finally:
    print("Final: end")