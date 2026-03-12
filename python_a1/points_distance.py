"""
2. Define two tuples. Each representing a point in the cartesian coordinate system (x1, y1), (x2, y2).
Print the distance between the two points.
"""

import math
def cal_distance(p1: tuple, p2: tuple) -> float:
    return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)

x1,y1 = map(int, input("Enter x1 and y1: ").split(" "))
p1=(x1,y1)
x2,y2 = map(int, input("Enter x2 and y2: ").split(" "))
p2=(x2,y2)

print(cal_distance(p1,p2))

