class Demo:
    pass
class Example:

    def __init__(self, name,backlog):
        self.name=name
        self.backlog=backlog

    def duplicate(self):
        return self.__class__(self.name, self.backlog)

    def __delattr__(self, item):
        print(f"deleting {item}")
        super().__delattr__(item)

    def __getattribute__(self, name):
        #print(f"Accessing {name}")
        return super().__getattribute__(name)

    def __getstate__(self):
        print("getstate")
        super().__getstate__()


# print(dir(Example))
# print(dir(object))
# print(dir(type))
# print(Example.__mro__)
ex=Example("hari",4)
print(dir(ex))
print(ex.__class__)  #class used to create the object type(ex)==ex.__class__
e2=ex.duplicate()
print(e2.name)

del ex.backlog  # execute the code in __delattr__

#print(type(Example))

print(ex.__dict__, e2.__dict__)
mp=ex.__dict__
print(mp["name"])

#__dir__ define what get return when dir(obj) is called
#__eq__ when you do obj1==obj2 this __eq__ is called
#__format__ when you so f"{obj}" this is called
#__ge__ when you do obj>=obj2
#__gt__ obj>obj2
print(ex.name) #__getattribute__ is executed when ever a attribute is executed

import pickle
pickle.dumps(ex)  #getState executed when serialization happens

#__hash__ executed when obj is used a key for set or dict

#__le__ obj<=obj2
#__lt__ obj<obj2
#__ne__ obj1!=obj2
#__new__ / __init__ while __init__ initialize object __new__ create a the object before __init___

#__setattr__ called every time attribute is set
#__sizeof()__ executed when sizeof(obj) is called
#__str__ executed when print(obj) is called

"""
operator methods in python:
+	__add__	__radd__	__iadd__
-	__sub__	__rsub__	__isub__
*	__mul__	__rmul__	__imul__
/	__truediv__	__rtruediv__	__itruediv__
//	__floordiv__	__rfloordiv__	__ifloordiv__
%	__mod__	__rmod__	__imod__
**	__pow__	__rpow__	__ipow__

+	__add__	__radd__	__iadd__
-	__sub__	__rsub__	__isub__
*	__mul__	__rmul__	__imul__
/	__truediv__	__rtruediv__	__itruediv__
//	__floordiv__	__rfloordiv__	__ifloordiv__
%	__mod__	__rmod__	__imod__
**	__pow__	__rpow__	__ipow__
&	__and__	__rand__	__iand__
`	`	__or__	__ror__
^	__xor__	__rxor__	__ixor__
<<	__lshift__	__rlshift__	__ilshift__
>>	__rshift__	__rrshift__	__irshift__
@  __matmul__

-a	__neg__
+a	__pos__
abs(a)	__abs__
~a	__invert__

int(a)	__int__
float(a)	__float__
str(a)	__str__
repr(a)	__repr__

len(a)	__len__
a[i]	__getitem__
a[i] = v	__setitem__
del a[i]	__delitem__
x in a	__contains__

a()	__call__
with a:	__enter__, __exit__
"""




