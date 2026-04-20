class Student:
    def __init__(self, mark):
        self._marks=mark

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, mark):
        self._marks=mark

s1=Student(55)
print(s1.marks)
s1.marks=75
print(s1.marks)