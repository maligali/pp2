import math

def volume(r):
    return (4/3) * math.pi * r**3
radius = int(input())
print(volume(radius))