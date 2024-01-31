#For loops
drinks = ["cola", "sprite", "cherry cola"]
for x in drinks:
  print(x)

print(" ")

for x in "cola":
  print(x)

print (" ")

#The break Statement
drinks = ["cola", "sprite", "cherry cola"]
for x in drinks:
  print(x)
  if x == "sprite":
    break
  
print(" ")

drinks = ["cola", "sprite", "cherry cola"]
for x in drinks:
   if x == "sprite":
    break
   print(x)

print(" ")

#The continue Statement
drinks = ["cola", "sprite", "cherry cola"]
for x in drinks:
   if x == "sprite":
    continue
   print(x)

#The range() Function
for x in range(4):
  print(x)

print(" ")

for x in range(1, 4):
  print(x)

print(" ")

for x in range(1, 29, 5):
  print(x)

print(" ")

#Else in For Loop
for x in range(3):
  print(x)
else:
  print("Finally finished!")

print(" ")

for x in range(7):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

print(" ")

#Nested Loops
adj = ["yummy", "sweet", "liquid"]
drinks = ["cola", "fanta", "sprite"]

for x in adj:
  for y in drinks:
    print(x, y)

print(" ")

#The pass Statement
for x in [4, 17, 2]:
  pass