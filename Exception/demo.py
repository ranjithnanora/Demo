class A:
    def __init__(self):
        self.a=10

class c:
    def __init__(self):
        self.c=10
    pass

class B(A, C):
    def __new__(cls):
        return super().__new__(cls)
    def __init__(self):
        super().__init__()
    pass

print(B.__mro__)
b=B()
print(b.a, b.c)
