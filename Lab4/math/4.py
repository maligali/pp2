def Area(l, h):
    area = l * h
    return area
l = int(input("Length of base: "))
h = int(input("Height of parallelogram: "))
area = Area(l, h)
print(f"Expected Output: {area}")