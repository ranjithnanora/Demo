"""
Create an abstract class called Character, it should have
a private variable for health,
an instance variable for position (2D vector)
a class variable that keeps track of the total characters created
Constructor takes health and position as args, pos should be an instance of Vector class and must be 2D
two abstract methods,
attack(self, other),
move(self, new_pos)
concrete methods,
take_damge(self, dmg), it should reduce the self's health and raise and handle exception if health goes negative, set it to 0 when you catch it
get_health(self)
get_position(self)
is_alive(self)
"""
from Vector import Vector
from abc import ABC, abstractmethod

class LowHealthException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
class Character(ABC):
    __total_character=0
    def __init__(self, health, position):
        if not isinstance(position, Vector) or position.n!=2:
            raise Exception
        self.__health=health
        self.position=position
        Character.__total_character+=1


    @abstractmethod
    def attack(self, other):
        pass

    @abstractmethod
    def move(self, new_pos):
        pass

    def take_damage(self, dmg):
        try:
            self.__health -= dmg
            if self.__health < 0:
                raise LowHealthException("health is negative")
        except LowHealthException as e:
            print(e)
            self.__health=0

    def get_health(self):
        return self.__health

    def get_position(self):
        return self.position

    @classmethod
    def get_total_character(cls):
        return cls.__total_character

    def is_alive(self):
        return self.__health>0

"""
Create two derived classed from the character class
Warrior,
    can only attack if
    Target is in the same row or column,
    and Distance is <=3
    Damage: 15
Archer,
    Damage: 8 if Distance is <=5
    Damage: 4 if Distance is > 5
 
"""
def print_function_name(func):
    def wrapper(*args):
        print(f"Function called {func.__name__}")
        return func(*args)
    return wrapper


class Warrior(Character):
    def __init__(self, health, position):
        super().__init__(health,position)

    @print_function_name
    def attack(self, other):
        if not isinstance(other, Character):
            return "Invalid"
        x1,y1=self.get_position()
        x2,y2=other.get_position()

        if x1==x2 or y1==y2 and Vector.distance_between_two_vector(self.position, other.position)<=3:
            other.take_damage(15)
        else:
            return "condition not satisfied"

        return "successful"

    @print_function_name
    def move(self, new_pos):
        if not isinstance(new_pos, Vector):
            raise Exception
        self.position=new_pos

class Archer(Character):
    def __init__(self, health, position):
        super().__init__(health, position)

    @print_function_name
    def attack(self, other):
        if not isinstance(other, Character):
            return "Invalid"

        distance=Vector.distance_between_two_vector(self.position, other.get_position())
        if distance<=5:
            other.take_damage(8)
        else:
            other.take_damage(4)

        return "successful"

    @print_function_name
    def move(self,new_pos):
        if not isinstance(new_pos, Vector):
            raise Exception
        self.position=new_pos


if __name__ == "__main__":
    warrior1 = Warrior(health=7, position=Vector(0,0))
    archer1 = Archer(health=80, position=Vector(0, 2))
    print("Warrior Health:", warrior1.get_health())
    print("Archer Health:", archer1.get_health())
    warrior1.attack(archer1)
    archer1.attack(warrior1)
    print("After Round 1")
    print("Warrior Health:", warrior1.get_health())
    print("Archer Health:", archer1.get_health())
    print("Warrior isAlive: ", warrior1.is_alive())
    print("Total character: " ,Character.get_total_character())


