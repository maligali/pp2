#The while Loop
i = 2
while i < 9:
  print(i)
  i += 1

print(" ")

#The break Statement
i = 3
while i < 7:
  print(i)
  if i == 5:
    break
  i += 1

print(" ")

#Continue
i = 2
while i < 7:
  i += 1
  if i == 4:
    continue
  print(i)

print(" ")

i = 3
while i < 8:
  print(i)
  i += 1
else:
  print("i is no longer less than 8")