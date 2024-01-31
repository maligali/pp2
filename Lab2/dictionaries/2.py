#Accessing items

#Get keys
thisdict = {
  "name" : "Malik",
  "age" : 17,
  "gender" : "Male"
}
x = thisdict["name"]
print(x)
x = thisdict.get("name")
print(x)

passport = {
  "name" : "Malik",
  "age" : 17,
  "gender" : "Male"
}
x = passport.keys()
print(x)
passport["country"] = "KZ"
print(x)

#Get values
thisdict = {
  "name" : "Malik",
  "age" : 17,
  "gender" : "Male"
}
x = thisdict.values()
print(x)

x = thisdict.values()
print(x) #b4
thisdict["age"] = 18
thisdict["School"] = "NIS"
print (x) #after

#Get items
thisdict = {
  "name" : "Malik",
  "age" : 17,
  "gender" : "Male"
}
x = thisdict.items()
print(x) #b4
thisdict["age"] = 22
thisdict["hair color"] = "black"
print (x) #after

#Check if Key Exists
thisdict = {
  "name" : "Malik",
  "age" : 17,
  "gender" : "Male"
}
if "name" in thisdict:
  print("Yes, 'name' is one of the keys in the thisdict dictionary")