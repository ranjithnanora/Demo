class MyDecorator:
    def __init__(self, func):
        print("Instance created")
        self.func=func

    def __call__(self,*args, **kwargs):
        print("before execution")
        return self.func(*args, **kwargs)


@MyDecorator
def greet(name):
    print("hello", name)

greet("Bob")

greet("mrg")

def count_class(cls):
    cls.instant_count = 0
    original_init = getattr(cls, "__init__")
    def new_init(self, *args):
        cls.instant_count+=1
        original_init(self, *args)

    cls.__init__=new_init
    return cls

@count_class
class MyClass:
    def __init__(self, name):
        self.name=name
    def greeting(self):
        print("hello", self.name)
    pass

m1=MyClass("ran")
m2=MyClass("man")
m1.greeting()
print(MyClass.instant_count)
