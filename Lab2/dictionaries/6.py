#Loop dictionaries

thisdict = {
  "name" : "Kate",
  "age" : 42,
  "gender" : "Female"
}

for x in thisdict:
  print(x) #keys

for x in thisdict:
  print(thisdict[x]) #values

for x in thisdict.values():
  print(x) #values

for x in thisdict.keys():
  print(x) #keys

for x, y in thisdict.items():
  print(x, y) #both