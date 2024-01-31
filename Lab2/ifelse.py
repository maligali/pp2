'''Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b'''
# Python If ... Else
a = 8249
b = 5959
if a > b:
  print("a is greater than b")

#elif
a = 111
b = 111
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#else
a = 32443
b = 3332
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#Short Hand If
if a < b: print("a is smaller than b")

#Short Hand If ... Else
a = 2222
b = 555
print("A") if a > b else print("B")

a = 333
b = 333
print("A") if a > b else print("=") if a == b else print("B")

#And
a = 121
b = 17
c = 131
if a > b and c > a:
  print("Both conditions are True")

#OR
a = 121
b = 17
c = 131
if a > b or a > c:
  print("At least one of the conditions is True")

#NOT
a = 111
b = 111
if not a > b:
  print("a is NOT greater than b")

#Nested if
x = 21

if x > 11:
  print("Above eleven,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#The pass Statement
a = 23
b = 223

if b > a:
  pass