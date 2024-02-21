def Area(base1, base2, height):
    area = ((base1 + base2)*height)/2
    return area
height = int(input("Height: "))
base1 = int(input("Base, first value: "))
base2 = int(input("Base, second value: "))
t_area = Area(base1, base2, height)
print(f"Expected Output: {t_area}")