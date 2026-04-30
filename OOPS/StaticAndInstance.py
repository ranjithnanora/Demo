class Car:
    wheel=4
    def __init__(self):
        self.name="BMW"
        self.milage=10

c1=Car()
c2=Car()
c1.name="MG"

# Create Instance variable
# print(dir(c1))
# c1.wheel=2 # create a local instance wheel replace static wheel
# c1.speed=100
# print(dir(c1))

Car.wheel=3 #static modification

print(c1.name, c1.wheel)
print(c2.name, c2.wheel)