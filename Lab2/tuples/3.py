#Update tuples

#Change Tuple Values
x = ("juice", "cola", "sprite")
y = list(x)
y[0] = "water"
x = tuple(y)
print (x)

#1. Convert into a list
tup = ("juice", "cola", "sprite")
y = list(tup)
y.append("fanta")
print(type(tup))
tup = tuple(y)
print(type(tup))

#2. Add tuple to a tuple
tup = ("juice", "cola", "sprite")
y = ("fanta",)
tup += y
print (tup)

#Remove Items
tup = ("juice", "cola", "sprite")
y = list(tup)
y.remove("juice")
tup = tuple(y)
print (tup)

tup = ("juice", "cola", "sprite")
del tup
print(tup) #this will raise an error because the tuple no longer exists

