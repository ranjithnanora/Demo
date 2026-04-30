class A:
    def __init__(self, name):
        self.name=name
        print("A executed")

class B:
    def __init__(self, name,age):
        self.age=age
        self.name=name
        print("B executed")

class C(A,B):
    def __init__(self, name,age):
        super().__init__(name)
        B.__init__(self,name, age)
        print("C executed")


print(C.__mro__s)
d=C("hari",12)

