'''There are three numeric types in Python:

int
float
complex'''

x = 8    # int
y = 8.2  # float
z = 1j   # complex

print(type(x))
print(type(y))
print(type(z))


#INT

x = 3
y = 9999999999999999
z = -2772722

print(type(x))
print(type(y))
print(type(z))

#FLOAT

x = 3.90
y = 4.0
z = -47.48

print(type(x))
print(type(y))
print(type(z))

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

#COMPLEX
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

#Type conversion
x = 192    # int
y = 27.7  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#Random number

import random

print(random.randrange(1, 10))