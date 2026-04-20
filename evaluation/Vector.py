class Vector:
    def __init__(self,*args):
        self.v=args
        self.n=len(self.v)

    @classmethod
    def from_list(cls, arr):
        return cls(*arr)

    @classmethod
    def from_tuple(cls, tup):
        return cls(*tup)

    def __add__(self, v2):
        result=[]
        if len(v2.v)!=self.n:
            self.__str__()
        for i in range(self.n):
            result.append(self.v[i]+v2.v[i])

        return tuple(result)

    def __sub__(self, v2):
        result = []
        if len(v2.v)!=self.n:
            self.__str__()
        for i in range(self.n):
            result.append(self.v[i] - v2.v[i])

        return tuple(result)

    def __str__(self):
        return "Invalid vector size"

    def __mul__(self, val):
        mul_result=[]
        for i in range(self.n):
            mul_result.append(self.v[i]*val)
        return tuple(mul_result)

    def __rmul__(self, val):
        return self.__mul__(val)

    def __pow__(self, v2):
        if self.n!=len(v2.v):
            self.__str__()
            return "Invalid vector size"
        dot_product=0
        for i in range(self.n):
            dot_product+=self.v[i]*v2.v[i]
        return dot_product

    def __matmul__(self, v2):
        if self.n==2 :
            if len(v2.v)!=2:
                return self.__str__()
            a1,a2=self.v
            b1,b2=v2.v
            return a1*b2-a2*b1
        if self.n!=3 or len(v2.v)!=3:
            return self.__str__()
        a1,a2,a3=self.v
        b1,b2,b3=v2.v
        return (a2*b3-a3*b2, a3*b1-a1*b3, a1*b2-a2*b1)

    def __gt__(self, v2):
        for i in range(self.n):
            if self.v[i]<=v2.v[i]:
                return False
        return True

    def __lt__(self, v2):
        for i in range(self.n):
            if self.v[i] >= v2.v[i]:
                return False
        return True


    def __ge__(self, v2):
        for i in range(self.n):
            if self.v[i]<v2.v[i]:
                return False
        return True

    def __le__(self,v2):
        for i in range(self.n):
            if self.v[i] >= v2.v[i]:
                return False
        return True

    def __iter__(self):
        self.i=0
        return self

    def __next__(self):
        if self.i>=self.n:
            raise StopIteration
        self.i+=1
        return self.v[self.i-1];

    @staticmethod
    def are_perpendicular(cross_product, V):
        result=0
        for i in range(len(V.v)):
            result+=cross_product[i]*V.v[i]
        return result==0

    @staticmethod
    def are_parallel(v1, v2):
        if len(v1.v)==3:
            cross_product=v1.__matmul__(v2)
            for ele in cross_product:
                if ele!=0:
                    return False
            return True
        elif len(v1.v)==2:
            return v1.__matmul__(v2)==0
        return "Invalid vector size"

    @staticmethod
    def distance_between_two_vector(v1,v2):
        if len(v1.v)!=2 or len(v2.v)!=2:
            return "Invalid vector length"
        x1,x2=v1.v
        y1,y2=v2.v
        return ((x2-x1)**2 + (y2-y1)**2)**0.5




#
# v1=Vector.from_list([1,2,3])
# v2=Vector(4,5,6)
# v3=Vector.from_tuple((2,2,3))
#
#
# # Scalar multiplication
# print("Scalar multiplication v1*3 : ",v1*3)
# print("Scalar multiplication 3*v1 : ",3*v1)
#
# #Dot product
# print("Dot product v1**v2 : ",v1**v2)
#
# #cross product
# print("Cross product (v1@v2): ", v1 @ v2)
#
# #Verify cross product is perpendicular to both inputs
# print("are_perpendicular((v1@v2),v1) : ", Vector.are_perpendicular((v1@v2),v1))
# print("are_perpendicular((v2@v1),v2) : ",Vector.are_perpendicular((v2@v1),v2))
#
# #Versify cross product is parallel
# print("is_parallel((1,-3),(3,-9)) : ",Vector.are_parallel(Vector(1,-3), Vector(3, -9)))
#
# # Comparisons
# print("v1 > v2 : ",v1 > v2)
# print("v1 < v2 : ",v1 < v2)
# print("(1,1,1)<=(1,1,1): ",Vector(1,1,1)<=Vector(1,1,1))
#
# #Iteration
# for ele in v2:
#     print(ele)