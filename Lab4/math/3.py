import math
def area_of_regular_polygon(n, s):
    return n * s**2 / (4*math.tan(math.pi / n))
n = int(input("Input number of sides: "))
s = int(input("Input the length of a side: "))
area = area_of_regular_polygon(n, s)
print(f"Area of the polygon is: {area}")